# -*- coding: utf-8 -*-
"""Logger controller."""
import json
import os

import pandas as pd
import requests

FILENAME = "logs.txt"
open(FILENAME, "w").close()


def create_log(body):
    """
    Creates a log entry in logs file.

    Parameters
    ----------
    body : dict
    """
    if "data" in body:
        ndarray = pd.DataFrame(body["data"]["ndarray"])
        if "names" in body["data"]:
            names = body["data"]["names"]
            ndarray.columns = names
        body = ndarray.to_json(orient="records", lines=True).rstrip("\n")

    with open(FILENAME, "a") as f:
        f.write(f"{json.dumps(body)}\n")

    # sends latest data to broker
    data = pd.read_json(FILENAME, lines=True)
    latest_data = data.iloc[-30:].values.tolist()

    BROKER_URL = os.getenv("BROKER_URL", "http://default-broker.anonymous.svc.cluster.local")
    requests.post(
        BROKER_URL,
        json={
            "data": {
                "ndarray": latest_data,
            },
        },
    )

    return body
