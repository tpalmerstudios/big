#!/usr/bin/python3

import json
import os
import random

from pathlib import Path
from urllib.parse import parse_qs


DATA_FILE = (Path(__file__).resolve().parent.parent / "book-data" / "book-concepts.json")


def respond(data, status="200 OK"):
    print(f"Status: {status}")
    print("Content-Type: application/json; charset=utf-8")
    print("Cache-Control: no-store")
    print()
    print(json.dumps(data))


def main():
    query = os.environ.get("QUERY_STRING", "")
    parameters = parse_qs(query)

    category = parameters.get("category", [None])[0]

    if category is None:
        respond(
            {"error": "Missing category parameter"},
            "400 Bad Request"
        )
        return

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

    except OSError as error:
        respond(
            {"error": f"Unable to open generator data: {error}"},
            "500 Internal Server Error"
            )
        return

    except json.JSONDecodeError as error:
        respond(
            {"error": f"Invalid JSON: {error}"},
            "500 Internal Server Error"
            )
        return

    variables = data.get("variables")

    if not isinstance(variables, list):
        respond(
            {"error": "Generator data does not contain a valid variables list"},
            "500 Internal Server Error"
            )
        return
    
    selected_variable = None
    for variable in variables:
        if variable.get("name") == category:
            selected_variable = variable
            break

    if selected_variable is None:
        respond(
            {"error": f"Unknown category: {category}"},
            "404 Not Found"
        )
        return

    options = selected_variable.get("options")

    if not isinstance(options, list) or not options:
        respond(
            {"error": f"Category '{category}' has no options"},
            "404 Not Found"
        )
        return

    choice = random.choice(options)

    if not isinstance(choice, dict):
        respond(
            {"error": f"Invalid option format for category '{category}'"},
            "500 Internal Server Error"
        )
        return

    value = choice.get("value")
    label = choice.get("label")

    if value is None or label is None:
        respond(
            {"error": f"Option in category '{category}' is missing value or label"},
            "500 Internal Server Error"
        )
        return

    respond({
        "category": category,
        "value": value,
        "label": label
    })

if __name__ == "__main__":
    main()