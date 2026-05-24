from app.services.gemini_services import ask_gemini
from app.services.parser import parse_json_response

import traceback

def perf_agent(state):

    try:

        prompt = f"""
        Detect performance problems:

        - memory leaks
        - nested loops
        - blocking IO
        - expensive rendering

        Return ONLY JSON ARRAY.

        DIFF:
        {state['diff']}
        """

        response = ask_gemini(prompt)

        findings = parse_json_response(response)

        state["findings"].extend(findings)

    except Exception as e:

        print("Perf Agent Error")

        print(str(e))

        traceback.print_exc()

    return state