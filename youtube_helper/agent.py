from google.adk.agents import LlmAgent
from typing import List, Dict
from google.genai import types


# -------------------------------------------------------------------
# Tools
# -------------------------------------------------------------------

def generate_video_ideas(topic: str, trends: List[str], num_ideas: int = 3) -> List[str]:
    """
    Generate creative video ideas based on the given topic and current trends.

    Args:
        topic (str): The main topic for the video ideas.
        trends (List[str]): A list of current trends to consider.
        num_ideas (int): Number of video ideas to generate.

    Returns:
        List[str]: A list of generated video ideas.
    """
    topic_lower = topic.lower()
    ideas = []

    if not trends:
        trends = ["current trend", "latest topic"]

    if "technology" in topic_lower:
        ideas = [
            f"Top {num_ideas} Emerging Technologies in 2025",
            f"How {trends[0]} Is Changing the Tech Landscape",
            "The Future of AI: What to Expect in the Next Decade",
        ]
    elif "lifestyle" in topic_lower:
        ideas = [
            f"{num_ideas} Lifestyle Hacks for a Healthier You",
            f"Exploring the Latest {trends[0]} Trends in Lifestyle",
            f"How to Incorporate {trends[min(1, len(trends) - 1)]} Into Your Daily Routine",
        ]
    elif "gaming" in topic_lower:
        ideas = [
            f"Top {num_ideas} Upcoming Games to Watch in 2025",
            f"How {trends[0]} Is Revolutionizing the Gaming Industry",
            "The Evolution of Multiplayer Gaming: What’s Next?",
        ]
    else:
        ideas = [
            f"{num_ideas} Unique Video Ideas for {topic.title()}",
            f"Exploring {trends[0]} in the Context of {topic.title()}",
            f"How to Make Engaging Content About {topic.title()}",
        ]

    return ideas


def get_channel_optimization_tips(channel_type: str) -> Dict[str, Dict[str, str]]:
    """
    Provide optimization tips for a YouTube channel based on its type.

    Args:
        channel_type (str): The type of YouTube channel (e.g., tech, lifestyle, gaming).

    Returns:
        Dict[str, Dict[str, str]]: A dictionary containing optimization tips.
    """
    tips = {
        "tech": {
            "upload_schedule": "Post new videos every Tuesday and Thursday at 5 PM.",
            "engagement": "Encourage viewers to comment on their favorite tech gadgets.",
            "thumbnails": "Use high-contrast images with bold text highlighting key features.",
        },
        "lifestyle": {
            "upload_schedule": "Post new videos every Monday, Wednesday, and Friday at 6 PM.",
            "engagement": "Ask viewers to share their own lifestyle tips in the comments.",
            "thumbnails": "Use bright, inviting images with a focus on people and activities.",
        },
        "gaming": {
            "upload_schedule": "Post new videos every Saturday and Sunday at 4 PM.",
            "engagement": "Host live streams and Q&A sessions to interact with the gaming community.",
            "thumbnails": "Use action-packed images featuring popular game characters.",
        },
    }

    default_tips = {
        "upload_schedule": "Post consistently based on audience activity.",
        "engagement": "Engage with your audience through comments and polls.",
        "thumbnails": "Create eye-catching thumbnails relevant to your content.",
        "additional_tip": "Analyze competitor channels for more tailored strategies.",
    }

    return {
        "status": "success",
        "tips": tips.get(channel_type.lower(), default_tips),
    }


# -------------------------------------------------------------------
# Root Agent
# -------------------------------------------------------------------

root_agent = LlmAgent(
    name="youtube_helper_agent",
    model="gemini-2.0-flash",
    description=(
        "An agent that assists with YouTube-related tasks — generating video ideas, "
        "writing scripts, suggesting tags, and optimizing channels for better reach."
    ),



    instruction="""
You are a YouTube Helper Expert Agent. Your tasks include generating video ideas, writing video scripts,
suggesting tags, and optimizing YouTube channels for better reach.

When performing tasks:
1. Research current YouTube trends and popular content in the target niche.
2. Understand the target audience's preferences and interests.
3. Ensure all content is original and adheres to YouTube's community guidelines.
4. Provide actionable, concise, and creative recommendations for optimization.

Always aim to deliver engaging, trend-aligned, and high-quality YouTube content.
""",
    tools=[generate_video_ideas, get_channel_optimization_tips],

    generate_content_config = types.GenerateContentConfig(
        temperature=0.3,
        max_output_tokens=1024,
        
    )
)
