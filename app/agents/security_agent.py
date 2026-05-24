from app.services.gemini_services import ask_gemini
from app.services.parser import parse_json_response

import traceback

def security_agent(state):

    try:

        prompt = f"""
        Analyze this PR diff for:
        
        - SQL injection
        - XSS
        - SSRF
        - auth bypass
        - secrets leakage
        - unsafe deserialization
        
        Return ONLY JSON ARRAY.

        DIFF:
        {state['diff']}
        """

        response = ask_gemini(prompt)

        findings = parse_json_response(response)

        state["findings"].extend(findings)

    except Exception as e:

        print("Security Agent Error")

        print(str(e))

        traceback.print_exc()

    return state