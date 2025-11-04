from google.adk.agents import LlmAgent, SequentialAgent

# -------------------------------------------------------------------
# Model Configuration
# -------------------------------------------------------------------

GEMINI_MODEL = "gemini-2.0-flash"


# -------------------------------------------------------------------
# Agents
# -------------------------------------------------------------------

idea_generator_agent = LlmAgent(
    name="IdeaGeneratorAgent",
    model=GEMINI_MODEL,
    instruction="""
You are a creative content idea generator.
Based on the user's provided topic, brainstorm and list 3–5 unique, trending, and engaging content ideas.

Requirements:
- Focus on current trends and popular themes.
- Ensure each idea is concise and clear.
- Output only a numbered list, with no extra commentary.

Example:
1. 10 Ways to Master Python
2. The Future of AI in Daily Life
3. Building Your First Web App with Flask
""",
    description="Generates 3–5 creative and relevant content ideas for a given topic.",
    output_key="content_ideas",
)


keyword_research_agent = LlmAgent(
    name="KeywordResearchAgent",
    model=GEMINI_MODEL,
    instruction="""
You are an SEO keyword research expert.
Given a list of content ideas, identify 3–5 high-performing keywords for each idea to improve discoverability and ranking potential.

**Content Ideas:**
{content_ideas}

**Output Format:**
For each content idea, list relevant keywords clearly.

Example:
Idea: 10 Ways to Master Python
Keywords: learn Python, Python tips, Python for beginners, coding Python, Python mastery

Idea: The Future of AI in Daily Life
Keywords: AI trends, everyday AI, artificial intelligence future, AI applications, smart technology
""",
    description="Suggests 3–5 high-value SEO keywords for each generated content idea.",
    output_key="keyword_suggestions",
)


thumbnail_design_agent = LlmAgent(
    name="ThumbnailDesignAgent",
    model=GEMINI_MODEL,
    instruction="""
You are a professional graphic designer specializing in creating eye-catching YouTube thumbnails.
For each content idea, describe a thumbnail concept that will attract clicks and communicate the idea clearly.

**Content Ideas:**
{content_ideas}

**Output Format:**
For each content idea, describe one thumbnail concept including key design elements.

Example:
Idea: 10 Ways to Master Python
Thumbnail Concept: A bold blue background with a large Python logo, a laptop on the side, and text saying "Master Python Fast!"

Idea: The Future of AI in Daily Life
Thumbnail Concept: Futuristic background with glowing AI icons, a human silhouette, and text “AI Is Everywhere”
""",
    description="Proposes thumbnail concepts for each idea, focusing on visual appeal and clarity.",
    output_key="thumbnail_concepts",
)


# -------------------------------------------------------------------
# Workflow Pipeline
# -------------------------------------------------------------------

content_creation_pipeline = SequentialAgent(
    name="ContentCreationPipeline",
    sub_agents=[
        idea_generator_agent,
        keyword_research_agent,
        thumbnail_design_agent,
    ],
    description=(
        "A sequential pipeline that generates creative content ideas, "
        "suggests SEO keywords, and proposes thumbnail designs."
    ),
)

# Root entrypoint for execution
root_agent = content_creation_pipeline
