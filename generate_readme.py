import snakemd
import yaml
import os

readme = snakemd.new_doc("README")
readme.add_header("Predictive and Prognostics Maintence Data Repository")
readme.add_paragraph("Predictive Maintenance poses a number of challenges for machine learning. The general types of machine learning problems encountered in predictive maintenance are:")
readme.add_ordered_list([
    "Time to failure prediction", 
    "Anomaly detection",
    "Clustering",
    "Fault detection and root cause analysis"])
readme.add_paragraph("This repository is to help researchers start working on predictive maintenance quickly. It provides an overview of relevant predictive maintenance data and 'quick start' scripts for researchers. We call it the Predictive and prOgnostics maiNtenance data repositorY or (PONY) for short.")

infoTable = []

def safe_info_lookup(info, key):
    result = ""
    try:
        result = info[key]
    except KeyError:
        pass
    return result

for dirname in os.listdir("pmx_data"):

    infopath = os.path.join("pmx_data", dirname, "info.yaml")
    with open(infopath, "r") as infofile:
        info = yaml.safe_load(infofile)

    name = safe_info_lookup(info, "name")
    description = safe_info_lookup(info, "description")
    problems = safe_info_lookup(info, "problem_type")

    infoTable = infoTable + [[name, description, problems]]

readme.add_table(
    ["**Dataset**", "**Description**", "**Problems**"],
    infoTable
)

readme.add_header("Adding a dataset")
readme.add_paragraph("The minimum requirements to add a dataset to this repository are:")
readme.add_ordered_list([
    "Create a directory for the data",
    "Adding a row in the index table, including what type of problem the data set is used for and its relevance to predictive maintenance",
    "Writing a script to download the data",
    "Providing a sample script to load the data"
])

readme.add_header("Additional Resources")
readme.add_paragraph("https://data.phmsociety.org/")

readme.add_header("Wishlist")
readme.add_paragraph("It would be good to have some visual inspection data here, a graphical data modality. I know there are people doing PMx with microscopy or aerial inspection. Not what WE do, but it certainly falls under the PMx bucket.")

readme.output_page()

'''
headerdoc = snakemd.new_doc("headerdoc")
headerdoc.add_header("DATASET DESCRIPTION")

headerdoc.add_table(
    ["Size (GB)", "Features", "Rows"],
    [[info['sizegb'], info['features'], info['rows']]]
)

sourcesdoc = snakemd.new_doc("sourcesdoc")
sourcesdoc.add_header("SOURCES")
sourcesdoc.add_paragraph("If you use this dataset for your research please cite it with:")
sourcesdoc.add_paragraph(doi2bib(info['data_doi']))
sourcesdoc.add_paragraph("Papers that use this dataset:")

for paper_doi in info['papers_doi']:
    sourcesdoc.add_paragraph(doi2bib(paper_doi))

with open("custom_writeup.md", 'r') as custom_writeup:
    readme = "\n".join([headerdoc.render(), custom_writeup.read(), sourcesdoc.render()])

with open("README.md", 'w') as readmefile:
    readmefile.write(readme)
'''