from google.adk.agents import LlmAgent
from google.adk.tools.langchain_tool import LangchainTool
from google.genai import types
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# step 1: Initialize Wikipedia API Wrapper
wikipedia_api = WikipediaAPIWrapper(top_k_results=3, doc_content_char_max=1000)

# step 2: Define Wikipedia Search Tool
wikipedia_tool = WikipediaQueryRun(api_wrapper=wikipedia_api)

# step 3: Create ADK-compatible Wikipedia Tool
adk_wikipedia_tool = LangchainTool(tool=wikipedia_tool)

wikipedia_summarizer_agent = LlmAgent(
    name="WikipediaSummarizer",
    model="gemini-2.0-flash",
    instruction=(
        "You are an expert assistant specializing in retrieving and summarizing information from Wikipedia. "
        "When given a topic, use the Wikipedia tool to search for relevant articles. "
        "Summarize the key points from the top articles into a concise summary of 3-5 sentences. "
        "Ensure the summary is clear, informative, and captures the essence of the topic."

    ),
    description="Fetches and summarizes information from Wikipedia articles on a given topic.",
    tools=[adk_wikipedia_tool],
    generate_content_config=types.GenerateContentConfig(
        max_output_tokens=500,
        temperature=0.3,
        top_p=0.9,
        frequency_penalty=0,
        presence_penalty=0,
    )
)

root_agent = wikipedia_summarizer_agent
