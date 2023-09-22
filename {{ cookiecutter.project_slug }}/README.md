# {{ cookiecutter.project_name }}

## Overview

{{ cookiecutter.project_description }}

## Requirements
 * min Python 3.10,
 * conda, conda-lock

## Setup

1. Create conda env and activate it: `conda create -n {{ cookiecutter.project_slug }} python=3.9`
2. Install dependencies: `conda-lock install conda-lock.yml` 
3. Update configs in `config.yaml`
4. Start working with the notebooks: run Jupyter lab: `jupyter lab` (or use your IDE to run the notebooks)

Update dependencies:
1. Update version in `environment.yaml`
2. Recreate lock file:  `conda-lock -f environment.yml`

## Problem formulation

## Data sources

## Baseline

## Model

## Experiments

To change the default tracking location to another folder you can use put the following to your `.env` file:
`MLFLOW_TRACKING_URI="file:///home/<path>/mlruns"`

To see the experiments:
1. (Optional) Load your environment variable from the .env file: `source .env`
2. Run `mlflow ui --backend-store-uri $MLFLOW_TRCKING_URI` to view the tracked experiments. (If you did not change the MLFLOW_TRCKING_URI, just run `mlflow ui`)

## Evaluation

## Next steps