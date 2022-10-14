import snakemd
import yaml
import os

def safe_info_lookup(info, key):
    result = ""
    try:
        result = info[key]
    except KeyError:
        pass
    return result

readme = snakemd.new_doc("README")
readme.add_header("Predictive and Prognostics Maintence Data Repository")
readme.add_paragraph("Predictive Maintenance poses a number of challenges for machine learning. The general types of machine learning problems encountered in predictive maintenance are:")
readme.add_ordered_list([
    "Time to failure prediction", 
    "Anomaly detection",
    "Clustering",
    "Fault detection and root cause analysis"])
readme.add_paragraph("The purpose of this repository is to help researchers start working on predictive maintenance quickly. It provides an overview of relevant predictive maintenance data and 'quick start' scripts for researchers. We call it the Predictive and prOgnostics maiNtenance data repositorY or (PONY) for short.")

infoTable = []

for dirname in os.listdir("pmx_data"):

    infopath = os.path.join("pmx_data", dirname, "info.yaml")
    with open(infopath, "r") as infofile:
        info = yaml.safe_load(infofile)

    name = safe_info_lookup(info, "name")
    description = safe_info_lookup(info, "description")
    problems = safe_info_lookup(info, "problem_type")
    equipment = safe_info_lookup(info, "equipment_type")
    note = safe_info_lookup(info, "note")

    infoTable = infoTable + [[name, description, problems, equipment, note]]

readme.add_table(
    ["**Dataset**", "**Description**", "**Problems**", "**Equipment Type**", "**Note**"],
    infoTable
)

readme.add_header("Adding a dataset")
readme.add_paragraph("The minimum requirements to add a dataset to this repository are:")
readme.add_ordered_list([
    "Create a directory for the data.",
    "Write an 'info.yaml' file containing basic information about your dataset that will be used to generate a README (see existing datasets for examples).",
    "Write a 'get_data.sh' script to download the data and unpack it into a standard csv format.",
    "Write a 'load_data.py' sample script to load the data into a pandas dataframe."
])

readme.add_header("Additional Resources")
readme.add_paragraph("https://data.phmsociety.org/")

readme.add_header("Wishlist")
readme.add_paragraph("It would be good to have some visual inspection data here, a graphical data modality. I know there are people doing PMx with microscopy or aerial inspection. Not what WE do, but it certainly falls under the PMx bucket.")

readme.output_page()