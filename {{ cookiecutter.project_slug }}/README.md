# {{ cookiecutter.project_name }}

## Overview

{{ cookiecutter.project_description }}

## Requirements
 * min Python 3.10,
 * conda, conda-lock

## Setup

1. (Optional) Create lock file if not present: `conda-lock -f environment.yml --kind env` 
2. Use conda to create environment: `conda env create -n {{ cookiecutter.conda_env_name }} -f conda-linux-64.lock.yaml`
3. Activate environment: `conda activate {{ cookiecutter.conda_env_name }}`
4. Update configs in `config.yaml`
5. Start working with the notebooks: run Jupyter lab: `jupyter lab` (or use your IDE to run the notebooks)

Update dependencies: `conda-lock --update <package>`
To re-solve the entire environment, e.g. after changing a version constraint in the source file:
`conda-lock -f environment.yaml --lockfile conda-linux-64.lock.yml`

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