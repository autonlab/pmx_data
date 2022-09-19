#!/bin/bash
wget https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/fddp3dvvzr-1.zip
unzip fddp3dvvzr-1.zip
rm fddp3dvvzr-1.zip
mv DeltaRobot_ParameterReadings datasets