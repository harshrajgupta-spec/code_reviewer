import json


def parse_json_response(response):

    try:

        response = response.strip()

        if response.startswith("```json"):

            response = response.replace("```json", "")
            response = response.replace("```", "")

        return json.loads(response)

    except Exception:

        return []