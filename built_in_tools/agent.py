from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.genai import types

GEMINI_MODEL = "gemini-2.0-flash"

root_agent = LlmAgent(
    name="WebSearchAgent",
    model=GEMINI_MODEL,
    instruction=(
        "You are a web search agent. Your task is to find information on the web based on user queries."
        " Use the 'google_search' tool to perform searches and provide concise, relevant answers."
        " Always ensure your responses are accurate and based on the search results." \
        "Summarize the findings clearly and informatively."
    ),
    description="An agent that performs web searches and provides summarized answers.",
    tools=[google_search],
    generate_content_config=types.GenerateContentConfig(max_output_tokens=1024,
                                                        temperature=0.4)
)
