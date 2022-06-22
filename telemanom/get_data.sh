#!/bin/bash
curl -O https://s3-us-west-2.amazonaws.com/telemanom/data.zip && unzip data.zip
curl -o data/labeled_anomalies.csv https://raw.githubusercontent.com/khundman/telemanom/26831a05d47857e194a7725fd982d5dea5402dd4/labeled_anomalies.csv data/
