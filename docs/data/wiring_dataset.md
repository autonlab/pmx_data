# Predictive Maintenance for Electrical Wiring Faults

Problem type: Image Fault Detection

Note: Data is structured to be ready to used by a yolov5 network.

| Size (GB) | Features | Rows | Contains missing data? |
| --------- | -------- | ---- | ---------------------- |
| 0.8195    | 1        | 300  | False                  |

## Performance Benchmarks

| Benchmark | Metric            | Source                                                    | Algorithm Used |
| --------- | ----------------- | --------------------------------------------------------- | -------------- |
| 0.989     | Overall precision | Automated Optical Inspection of Electrical Wiring Systems | Yolov5         |
## Sources

Data location: https://data.mendeley.com/datasets/g6rbmc2ggc

If you use this dataset for your research please cite it with:

- Edman, Rob; Babb, Aleeya (2022), “Predictive Maintenance for Electrical Wiring Faults”, Mendeley Data, V1, doi: 10.17632/g6rbmc2ggc.1

Data License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Papers that use this dataset:

- Aleeya Babb, Robert Edman, Nicholas Gisolfi, Keith Dufendach and Artur Dubrawski, Automated Optical Inspection of Electrical Wiring System

## Additional information

This dataset contains images of the internal electrical wiring system of a desktop computer and hand-labeled coordinates of faults introduced to the system.

The dataset contains two folders:
- images
- labels

And one .txt file:
- notes

The images folder contains three folders of images that were used to train the original model.
- test01
- train01
- val01

The labels folder contains three folders of label coordinates representing the hand-labeled bounding boxes corresponding to image:
- test01
- train01
- val01

The notes.txt file contains the original test/val image set splits.

This dataset was produced by Auton Lab, Carnegie Mellon University, and is available under the following link:
https://data.mendeley.com/datasets/g6rbmc2ggc
