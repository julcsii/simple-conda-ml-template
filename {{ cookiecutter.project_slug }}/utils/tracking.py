from typing import Optional

import mlflow


def set_experiment(experiment_name: Optional[str]):
    if experiment_name:
        experiment = mlflow.get_experiment_by_name(name=experiment_name)
        if not experiment:
            mlflow.create_experiment(name=experiment_name)
        mlflow.set_experiment(experiment_name=experiment_name)
