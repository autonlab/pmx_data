import snakemd
import yaml
import urllib.request
from urllib.error import HTTPError
import os

#modify this and run this script to generate a README for the dataset you specify
dataset_name = "scania_trucks_air_pressure_system_failure"
dataset_path = os.path.join("pmx_data", dataset_name)

def doi2bib(doi):
    #adapted from https://scipython.com/blog/doi-to-bibtex/
    baseurl = 'http://dx.doi.org/'
    url = baseurl + doi
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/x-bibtex')
    
    bibtex = "Not found"
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

infopath = os.path.join(dataset_path, "info.yaml")
with open(infopath, "r") as infofile:
    info = yaml.safe_load(infofile)

headerdoc = snakemd.new_doc("headerdoc")
headerdoc.add_header("Dataset Description")  

headerdoc.add_paragraph("Problem type: " + get(info, "data_type") + " " + get(info, "problem_type"))

headerdoc.add_table(
    ["Size (GB)", "Features", "Rows", "Contains missing data?", "Target Column", "Notes"],
    [[
        get(info, 'sizegb'), 
        get(info, 'features'), 
        get(info, 'rows'), 
        get(info, 'missing_data'), 
        get(info, 'target'), 
        get(info, 'note')
    ]]
)

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

headerdoc.add_horizontal_rule()

sourcesdoc = snakemd.new_doc("sourcesdoc")
sourcesdoc.add_header("Sources")

sourcesdoc.add_paragraph("If you use this dataset for your research please cite it with:")

if exists(info, 'data_doi'):
    sourcesdoc.add_paragraph(doi2bib(info['data_doi']))
else:
    sourcesdoc.add_paragraph(get(info,'data_citation'))

sourcesdoc.add_paragraph("Data License: [" + get(info, 'license_name') + "](" + get(info, 'license_link') + ")")

sourcesdoc.add_paragraph("Papers that use this dataset:")

if exists(info, 'papers_doi'):
    for paper_doi in info['papers_doi']:
        sourcesdoc.add_paragraph(doi2bib(paper_doi))

if exists(info, 'papers_with_no_doi'):
    for paper_citation in info['papers_with_no_doi']:
        sourcesdoc.add_paragraph(paper_citation)

with open(os.path.join(dataset_path, "custom_writeup.md"), 'r') as custom_writeup:
    readme = "\n".join([headerdoc.render(), custom_writeup.read(), sourcesdoc.render()])

with open(os.path.join(dataset_path, "README.md"), 'w') as readmefile:
    readmefile.write(readme)