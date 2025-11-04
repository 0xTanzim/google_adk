
from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent

GEMINI_MODEL = "gemini-2.0-flash"

# Agent 1: Tweet Generator
tweet_generator_agent = LlmAgent(
    name="TweetGenerator",
    model=GEMINI_MODEL,
    instruction="""You are a Twitter content creator specializing in engaging social media posts.
Based *only* on the topic provided, write a concise and engaging tweet (max 280 characters).
Include 1-3 relevant hashtags that are trending or commonly used.

Output *only* the complete tweet text with no additional commentary or explanation.""",
    description="Generates optimized tweets with relevant hashtags for a given topic.",
    output_key="generated_tweet"
)

# Agent 2: Instagram Caption Generator
instagram_caption_agent = LlmAgent(
    name="InstagramCaptionGenerator",
    model=GEMINI_MODEL,
    instruction="""You are an Instagram content creator known for crafting engaging captions that build community.
Based *only* on the topic provided, write a compelling and short Instagram caption (2-4 sentences).
Include 3-5 relevant and popular hashtags that align with Instagram best practices.

Output *only* the complete Instagram caption with no additional explanation.""",
    description="Generates engaging Instagram captions with relevant hashtags and emojis.",
    output_key="generated_instagram_caption"
)

# Agent 3: Blog Post Introduction Generator
blog_intro_agent = LlmAgent(
    name="BlogPostIntroGenerator",
    model=GEMINI_MODEL,
    instruction="""You are an experienced blog writer who creates compelling introductions that captivate readers.
Based *only* on the topic provided, write a compelling and informative introductory paragraph (3-5 sentences).
The introduction should hook the reader immediately and clearly state what the blog post will cover.
Use an engaging tone that encourages the reader to continue.

Output *only* the introductory paragraph with no additional commentary.""",
    description="Generates compelling introductory paragraphs for blog posts.",
    output_key="generated_blog_intro"
)


parallel_content_agent = ParallelAgent(
    name="ParallelSocialMediaContent",
    sub_agents=[
        tweet_generator_agent,
        instagram_caption_agent,
        blog_intro_agent
    ],
    description="Generates content simultaneously across multiple platforms for maximum efficiency"
)

content_consolidator_agent = LlmAgent(
    name="ContentConsolidator",
    model=GEMINI_MODEL,
    instruction="""You are a meticulous content editor responsible for organizing and presenting generated content professionally.

Your task is to consolidate the generated social media content drafts into a single, well-formatted summary.

**Input Content:**
- Tweet: {generated_tweet}
- Instagram Caption: {generated_instagram_caption}
- Blog Post Introduction: {generated_blog_intro}

**Desired Output Format:**

## Social Media Content Draft Summary

### Twitter Draft
{generated_tweet}

### Instagram Draft
{generated_instagram_caption}

### Blog Post Introduction Draft
{generated_blog_intro}

Output *only* the structured summary following this exact format. Do not add commentary or additional text.""",
    description="Consolidates and organizes content from multiple platforms into a unified summary."
)

root_agent = SequentialAgent(
    name="MultiPlatformContentPipeline",
    sub_agents=[
        parallel_content_agent,
        content_consolidator_agent
    ],
    description="Orchestrates multi-platform content generation with automatic consolidation"
)


# Example usage
if __name__ == "__main__":
    # Example: Generate content for a given topic
    sample_topic = "Artificial Intelligence in Healthcare"

    # Invoke the root agent with the topic
    result = root_agent.run(input=sample_topic)

    # Display the consolidated output
    print(result)
