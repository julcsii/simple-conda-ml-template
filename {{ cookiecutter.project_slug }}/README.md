# {{ cookiecutter.project_name }}

## Overview

## Requirements
 * min Python 3.10, pip
 * Poetry

## Setup
1. Install dependencies: `poetry install` (This will create a poetry.lock file, which contains exact versions of the dependencies and should be committed to the repo.)
2. Activate environment: `poetry shell`
3. Update configs in `config.yaml`
4. Start working with the notebooks: run Jupyter lab: `jupyter lab` (or use your IDE to run the notebooks)

To add new dependencies run `poetry add <pkg>` update dependencies run `poetry update`.

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