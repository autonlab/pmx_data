from email import header
import snakemd
import yaml
import urllib.request
from urllib.error import HTTPError

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

with open("info.yaml", "r") as infofile:
    info = yaml.safe_load(infofile)

headerdoc = snakemd.new_doc("headerdoc")
headerdoc.add_header("Dataset Description")

headerdoc.add_paragraph("Problem type: " + info["data_type"] + " " + info["problem_type"])

headerdoc.add_table(
    ["Size (GB)", "Features", "Rows", "Contains missing data?", "Target Column", "Notes"],
    [[info['sizegb'], info['features'], info['rows'], info['missing_data'], info['target'], info['note']]]
)

headerdoc.add_header("Performance Benchmarks", level=2)

headerdoc.add_table(
    ["Benchmark", "Metric", "Source"],
    [[info['autonml_benchmark'], info['autonml_benchmark_metric'], "AutonML"]]
)

headerdoc.add_horizontal_rule()

sourcesdoc = snakemd.new_doc("sourcesdoc")
sourcesdoc.add_header("Sources")

sourcesdoc.add_paragraph("If you use this dataset for your research please cite it with:")
sourcesdoc.add_paragraph(info['data_citation'])

sourcesdoc.add_paragraph("Data License: GPL 2.0").insert_link("GPL 2.0", info['license'])

sourcesdoc.add_paragraph("Papers that use this dataset:")
for paper_doi in info['papers_doi']:
    sourcesdoc.add_paragraph(doi2bib(paper_doi))

with open("custom_writeup.md", 'r') as custom_writeup:
    readme = "\n".join([headerdoc.render(), custom_writeup.read(), sourcesdoc.render()])

with open("README.md", 'w') as readmefile:
    readmefile.write(readme)