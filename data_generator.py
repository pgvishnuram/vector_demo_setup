import json
from random import randint


for i in range(1000):
    dictionary = {
        "asctime": "2022-05-09 17:51:14,381",
        "filename": "taskinstance.py",
        "lineno": randint(0, 10000),
        "levelname": "INFO",
        "message": "Dependencies all met for <TaskInstance: branch_and_subdag.subdag_1 manual__2022-05-09T17:49:43.711425+00:00 [queued]>",
        "offset": 1652118674381508608,
        "dag_id": "branch_and_subdag",
        "task_id": "subdag_1",
        "execution_date": "2022_05_09T17_49_43_711425",
        "try_number": "1",
        "log_id": "branch_and_subdag_subdag_1_2022_05_09T17_49_43_711425_1",
    }

    with open("vector/data/out.log", "a") as f:
        json_object = json.dump(dictionary, f)
        f.write("\n")
