import sys

sys.path.append("./package")

import requests


def lambda_handler(event, context):
    # Make a sample HTTP GET request using requests library
    response = requests.get(
        "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2024-03-21&end_date=2024-04-04&hourly=temperature_2m&daily=temperature_2m_max"
    )

    # Get the response JSON
    data = response.json()

    return {"statusCode": 200, "body": data}
