import snakemd
import yaml
import os
import sys

def get(info, key):
    result = ""
    try:
        result = info[key]
    except KeyError:
        pass
    return result

#github actions will input branch name as command line arg
branchname = sys.argv[1]

readme = snakemd.new_doc("README")

readme.add_header("Predictive Maintence Metadata Repository")

readme.add_paragraph("Predictive Maintenance poses a number of challenges for machine learning. The general types of machine learning problems encountered in predictive maintenance are:")
readme.add_ordered_list([
    "Time to failure prediction", 
    "Anomaly detection",
    "Clustering",
    "Fault detection and root cause analysis"])
readme.add_paragraph("The purpose of this repository is to help researchers start working on predictive maintenance quickly. It provides an overview of relevant predictive maintenance data and 'quick start' scripts for researchers.  This is a *metadata* repository, so it does not contain the data itself--only information about the data, and scripts for downloading and working with it.")

readme.add_header("Table of Contents", level=2)
readme.add_table_of_contents(range(2,4))
readme.add_header("List of Datasets", level=2)

infoTable = []

for dirname in sorted(os.listdir("pmx_data")):

    infopath = os.path.join("pmx_data", dirname, "info.yaml")
    with open(infopath, "r") as infofile:
        info = yaml.safe_load(infofile)

    name = info["name"]
    namelink = "[" + name + "](https://github.com/autonlab/pmx_data/tree/" + branchname + "/pmx_data/" + dirname + ")"
    description = get(info, "description")
    
    problems = info["problem_type"]
    if "data_type" in info.keys():
        problems = info['data_type'] + " " + problems

    equipment = get(info, "equipment_type")

    note = get(info, "note")

    infoTable = infoTable + [[namelink, description, problems, equipment, note]]

readme.add_table(
    ["**Dataset**", "**Description**", "**Problems**", "**Equipment Type**", "**Note**"],
    infoTable
)

readme.add_header("Downloading a Dataset", level=2)
readme.add_ordered_list([
    "Navigate to that dataset's directory in this repository.",
    "Download the get_data.sh script.",
    "Run the get_data.sh script in the location where you would like to download the data."
])
readme.add_paragraph("This currently only works on Linux.  Some get_data.sh scripts require additional steps before you can run them, which are described in a comment at the top of the file.")

readme.add_header("Adding a Dataset", level=2)
readme.add_ordered_list([
    "If the dataset is not already hosted online: upload it to a data hosting site (we recommend [Mendeley](https://data.mendeley.com)).",
    "Create a fork of this repository."
    "Clone that fork to your local machine.",
    "Make a copy of the [sample_dataset](https://github.com/autonlab/pmx_data/tree/main/sample_scripts/sample_dataset) folder and place it within the pmx_data directory.  This folder contains sample scripts to get you started.",
    "Rename the directory to match the name of your dataset.",
    "Modify the 'get_data.sh' script to download your data and unpack it into a standard csv format within a subfolder called 'datasets'.",
    "Modify the 'info.yaml' file, filling in information about your dataset that will be used to generate a README.",
    "Optional: Write a 'custom_writeup.md' markdown file containing any information about your dataset that is not encapsulated by info.yaml.  This will be added to the generated README.",
    "Optional: Write a 'load_data.py' sample script to load the data into a pandas dataframe or any other python object that is easy to work with ([this sample script](https://github.com/autonlab/pmx_data/blob/main/sample_scripts/load_data_recursive.py) works well in most instances).",
    "Commit your local changes and push them to your fork on GitHub."
    "Create a pull request from your fork into this repository."
])

readme.add_header("Additional Resources", level=2)
readme.add_paragraph("https://data.phmsociety.org/")
readme.add_paragraph("https://www.nasa.gov/content/prognostics-center-of-excellence-data-set-repository")
readme.add_paragraph("https://zenodo.org/")
readme.add_paragraph("UCI repository https://archive.ics.uci.edu/ml/datasets.php")
readme.add_paragraph("https://www.openml.org/")

readme.add_header("Wishlist", level=2)
readme.add_unordered_list([
    "More image datasets, i.e. PmX with microscopy or aerial inspection.",
    "Tracking performance of different autoML tools on datasets over time.",
    "Support for multiple problem types on same dataset (for instance, fault detection can also be anomaly detection if you remove the target variable).",
    "Guide to pros and cons of different data hosting services (mendeley, kaggle, etc) for people who want to upload datasets.",
    "Allow for searching for datasets with different attributes or sorting by attribute.",
    "Github Pages GUI to make downloading and uploading easier for non-technical users.",
    "Support for downloading and unpacking data in Windows and MacOS.",
    "Add domain table for data type, problem type, equipment type",
    "Standardize train/test splits for future benchmarking when possible",
    "More readable display of bibtex citations",
    "Fully fill out info.yaml for all datasets"
])

readme.output_page()