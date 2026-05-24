from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.2
)


def ask_gemini(prompt: str):

    response = llm.invoke(prompt)

    return response.content