from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import GEMINI_API_KEY
import os


def get_llm():

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:

        raise ValueError("GEMINI_API_KEY missing")

    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=api_key,
        temperature=0.2
    )


def ask_gemini(prompt: str):

    try:

        llm = get_llm()

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:

        print("Gemini Error:", str(e))

        return "Gemini analysis failed"

