#!/usr/bin/python3

import json
import os
import random

from pathlib import Path
from urllib.parse import parse_qs


DATA_FILE = Path(__file__).resolve().parent.parent / "book-data" / "book-concepts.json"


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

    except json.JSONDecodeError as error:
        respond(
            {"error": f"Invalid JSON: {error}"},
            "500 Internal Server Error"
            )
        return

    items = data.get(category)

    if not isinstance(items, list):
        respond(
            {"error": f"Unknown category: {category}"},
            "404 Not Found"
            )
        return

    if not items:
        respond(
            {"error": f"Category '{category}' is empty"},
            "404 Not Found"
            )
        return

    respond({
        "category": category,
        "value": random.choice(items)
        })

if __name__ == "__main__":
    main()