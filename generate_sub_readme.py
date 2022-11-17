import snakemd
import yaml
import urllib.request
from urllib.error import HTTPError
import os
import sys
from collections import OrderedDict

def doi2bib(doi):
    #adapted from https://scipython.com/blog/doi-to-bibtex/
    baseurl = 'http://dx.doi.org/'
    url = baseurl + doi
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/x-bibtex')
    
    bibtex = "Not found: " + doi
    try:
        with urllib.request.urlopen(req) as f:
            bibtex = f.read().decode()
    except HTTPError as e:
        if e.code == 404:
            print('DOI not found.')
        else:
            print('Service unavailable.')
    return bibtex

def exists(info, key):
    result = True
    try:
        lookup = info[key]
    except KeyError:
        result = False
    return result

def get(info, key):
    result = ""
    try:
        result = info[key]
    except KeyError:
        pass
    return result

def generate_sub_readme(datasetpath):

    infopath = os.path.join(datasetpath, "info.yaml")
    with open(infopath, "r") as infofile:
        info = yaml.safe_load(infofile)

    headerdoc = snakemd.new_doc("README")
    if 'name' in info.keys():
        headerdoc.add_header(info['name'])
    else:
        headerdoc.add_header("Dataset Description")  

    headerdoc.add_paragraph("Problem type: " + get(info, "data_type") + " " + get(info, "problem_type"))

    if "note" in info.keys():
        headerdoc.add_paragraph("Note: " + info['note'])

    possibletablecols = OrderedDict([
        ("sizegb", "Size (GB)"),
        ("features", "Features"),
        ("rows", "Rows"),
        ("missing_data", "Contains missing data?"),
        ("target", "Target Column"),
        ("num_classes", "Number of classes"),
        ("time_series_all_same_length", "Are all time series the same length?"),
        ("average_time_series_length", "Avg. time series length"),
        ("time_series_length", "Time series length"),
    ])

    tablecols = [x for x in possibletablecols.keys() if (x in info.keys())]

    tableheader = []
    tablebody = []

    for colkey in tablecols:
        tableheader = tableheader + [possibletablecols[colkey]]
        tablebody = tablebody + [info[colkey]]

    headerdoc.add_table(tableheader, [tablebody])

    if "ml_performance_benchmarks" in info.keys():
        headerdoc.add_header("Performance Benchmarks", level=2)

        rows = []
        for benchmark in info["ml_performance_benchmarks"]:
            
            if exists(benchmark, "source_link"):
                
                if not exists(benchmark, "source_name"):
                    benchmark['source_name'] = "source"
                    
                name = "[" + benchmark["source_name"] + "](" + benchmark["source_link"] + ")"
            else:
                name = get(benchmark, "source_name")
            
            rows =  rows + [[
                get(benchmark, "benchmark"),
                get(benchmark, "metric"),
                name,
                get(benchmark, "algorithm_used")
            ]]

        headerdoc.add_table(
            ["Benchmark", "Metric", "Source", "Algorithm Used"],
            rows
        )

    sourcesdoc = snakemd.new_doc("README")
    sourcesdoc.add_header("Sources", level=2)

    sourcesdoc.add_paragraph("Data location: " + info['location'])
    if 'data_citation' in info.keys():
        sourcesdoc.add_paragraph("If you use this dataset for your research please cite it with:")
        sourcesdoc.add_unordered_list([info['data_citation']])
    elif 'data_doi' in info.keys():
        sourcesdoc.add_paragraph("If you use this dataset for your research please cite it with:")
        sourcesdoc.add_unordered_list([doi2bib(info['data_doi'])])
    else:
        sourcesdoc.add_paragraph("No data citation available")

    if 'license_name' in info.keys() and 'license_link' in info.keys():
        sourcesdoc.add_paragraph("Data License: [" + info['license_name'] + "](" + info['license_link'] + ")")
    elif 'license_name' in info.keys():
        sourcesdoc.add_paragraph("Data License: " + info['license_name'])
    elif 'license_link' in info.keys():
        sourcesdoc.add_paragraph("Data License [here](" + info['license_link'] + ")")
    else:
        sourcesdoc.add_paragraph("No data license available.")

    if 'papers_doi' in info.keys() or 'papers_with_no_doi' in info.keys():
        sourcesdoc.add_paragraph("Papers that use this dataset:")

        papers = []
        if 'papers_doi' in info.keys():
            for paper_doi in info['papers_doi']:
                papers = papers + [doi2bib(paper_doi)]

        if 'papers_with_no_doi' in info.keys():
            for paper_citation in info['papers_with_no_doi']:
                papers = papers + [paper_citation]
        
        sourcesdoc.add_unordered_list(papers)

    if 'benchmark_code_links' in info.keys():
        codes = []
        sourcesdoc.add_paragraph("Links to code analyzing the dataset or providing benchmark performance:")
        for link in info['benchmark_code_links']:
            codes = codes + [link]

        sourcesdoc.add_unordered_list(codes)
    
    custom_writeup_path = os.path.join(datasetpath, "custom_writeup.md")
    if os.path.exists(custom_writeup_path):
        sourcesdoc.add_header("Additional information", level=2)
        with open(custom_writeup_path, 'r') as custom_writeup:
            output_file = "\n".join([
                headerdoc.render(),  
                sourcesdoc.render(),
                custom_writeup.read()
                ])
    else:
        output_file = "\n".join([headerdoc.render(), sourcesdoc.render()])

    readme_path = os.path.join(datasetpath, "README.md")
    with open(readme_path, 'w') as readme_file:
        readme_file.write(output_file)

#sys.argv[1:] should be a list of paths of changed info.yaml files or custom_writeup.md files
#go thru each argument and extract the path to the dataset folder
#os.path.split(filepath)[0] returns the path for the folder containing the file at filepath

datasetpaths = [os.path.split(filepath)[0] for filepath in sys.argv[1:]]

#if both info.yaml and custom_writeup.md were modified for the same dataset, there will be duplicates
#remove these so we dont generate the same README twice
datasetpaths = list(set(datasetpaths))

for datasetpath in datasetpaths:
    generate_sub_readme(datasetpath)