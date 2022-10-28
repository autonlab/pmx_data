from email import header
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

def generate_sub_readme(info, dataset_path):
    headerdoc = snakemd.new_doc("README")
    headerdoc.add_header("Dataset Description")  

    headerdoc.add_paragraph("Problem type: " + get(info, "data_type") + " " + get(info, "problem_type"))

    possibletablecols = OrderedDict([
        ("sizegb", "Size (GB)"),
        ("features", "Features"),
        ("rows", "Rows"),
        ("missing_data", "Contains missing data?"),
        ("target", "Target Column"),
        ("notes", "Notes"),
        ("time_series_all_same_length", "Are all time series the same length?"),
        ("average_time_series_length", "Avg. time series length"),
        ("time_series_length", "Time series length")
    ])

    tablecols = [x for x in possibletablecols.keys() if (x in info.keys())]

    tableheader = []
    tablebody = []

    for colkey in tablecols:
        tableheader = tableheader + [possibletablecols[colkey]]
        tablebody = tablebody + [info[colkey]]

    headerdoc.add_table(tableheader, [tablebody])

    if exists(info, "ml_performance_benchmarks"):
        headerdoc.add_header("Performance Benchmarks", level=2)

        rows = []
        for benchmark in info["ml_performance_benchmarks"]:
            
            if exists(benchmark, "source_link"):
                name = "[" + get(benchmark, "source_name") + "](" + get(benchmark, "source_link") + ")"
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
    sourcesdoc.add_header("Sources")

    if exists(info, 'data_doi'):
        sourcesdoc.add_paragraph("If you use this dataset for your research please cite it with:")
        sourcesdoc.add_paragraph(doi2bib(info['data_doi']))
    elif 'data_citation' in info.keys():
        sourcesdoc.add_paragraph("If you use this dataset for your research please cite it with:")
        sourcesdoc.add_paragraph(info['data_citation'])
    else:
        sourcesdoc.add_paragraph("Data location: " + info['location'])
        sourcesdoc.add_paragraph("No data citation available")

    sourcesdoc.add_paragraph("Data License: [" + get(info, 'license_name') + "](" + get(info, 'license_link') + ")")

    sourcesdoc.add_paragraph("Papers that use this dataset:")

    if exists(info, 'papers_doi'):
        for paper_doi in info['papers_doi']:
            sourcesdoc.add_paragraph(doi2bib(paper_doi))

    if exists(info, 'papers_with_no_doi'):
        for paper_citation in info['papers_with_no_doi']:
            sourcesdoc.add_paragraph(paper_citation)

    custom_writeup_path = os.path.join(dataset_path, "custom_writeup.md")
    if os.path.exists(custom_writeup_path):
        sourcesdoc.add_horizontal_rule()
        with open(custom_writeup_path, 'r') as custom_writeup:
            output_file = "\n".join([
                headerdoc.render(),  
                sourcesdoc.render(),
                custom_writeup.read()
                ])
    else:
        output_file = "\n".join([headerdoc.render(), sourcesdoc.render()])

    readme_path = os.path.join(dataset_path, "README.md")
    with open(readme_path, 'w') as readme_file:
        readme_file.write(output_file)

#sys.argv[1:] should be a list of paths of changed info.yaml files
#go thru each argument and regenerate the sub-readme for that file

for infopath in sys.argv[1:]:
    datasetpath = os.path.split(infopath)[0]

    with open(infopath, "r") as infofile:
        info = yaml.safe_load(infofile)

    generate_sub_readme(info, datasetpath)

'''
#go through all the datasets
#check if any of them have generate_readme=True set in thier info file
#if so, regenerate their readme

for name in os.listdir("pmx_data"):
    dataset_path = os.path.join('pmx_data', name)

    if os.path.isdir(dataset_path):
        infopath = os.path.join(dataset_path, "info.yaml")

        if os.path.exists(infopath):

            with open(infopath, "r") as infofile:
                info = yaml.safe_load(infofile)

            if "generate_readme" in info.keys() and info["generate_readme"] == True:
                generate_sub_readme(info, dataset_path)
                info["generate_readme"] = False

                with open(infopath, 'w') as infofile:
                    yaml.dump(info, infofile)
'''