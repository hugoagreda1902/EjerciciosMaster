import json
from datetime import datetime

def log_experiment(
    experiment_name,
    params,
    metrics,
    X=None,
    output_path="experiment_log.json"
):
    log = {
        "experiment": experiment_name,
        "timestamp": datetime.now().isoformat(),
        "params": params,
        "metrics": metrics
    }

    if X is not None:
        log["dataset_info"] = {
            "num_rows": X.shape[0],
            "num_columns": X.shape[1],
            "columns": list(X.columns)
        }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=4, ensure_ascii=False)

    return log
