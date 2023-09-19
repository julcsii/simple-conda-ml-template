# simple-ml-template
Cookiecutter template to kick off your machine learning experiments with MLflow, Jupyter and more.

## About this template

The template makes it easy to kick off simple machine learning experiments (xgboost, sklearn) conducted in Jupyter notebooks and tracked with MLflow. 

It contains an example notebook to train and evaluate machine learning models compatible with the sklearn API.

Tools used in the generated project:
* [Poetry](https://python-poetry.org/docs/) for dependency and environment management.
  * Basic data science dependencies are included (see in the pyproject.toml)
* [Omegaconf](https://omegaconf.readthedocs.io/en/2.3_branch/index.html) for configuration management
* [Jupyter](https://docs.jupyter.org) for running notebooks 
* [Mlflow](https://mlflow.org/docs/latest/index.html) to track experiments
* `.env` files for configuring environment variables

## Requirements

* Python 3
* cookiecutter (tested with 2.3, see installation notes [here](https://cookiecutter.readthedocs.io/en/stable/installation.html#install-cookiecutter))
* cruft (tested with 2.15, see installation notes [here](https://cruft.github.io/cruft/#installation))

## How to generate a project with this template
`cruft create git@github.com:julcsii/simple-ml-template.git`

## How to update downstream projects
`cruft update`

### To regenerate with different user values
`cruft update --variables-to-update '{ "<variable>": "<new value>" }'`