from google.adk.agents import LlmAgent, LoopAgent,SequentialAgent
from google.adk.tools.tool_context import ToolContext

GEMINI_MODEL = "gemini-2.0-flash"

def exit_loop(tool_context: ToolContext):
  tool_context.actions.escalate = True
  return "Exiting loop and escalating to human agent."

# STEP 1: Initial Recipe Writer Agent (Runs ONCE at the beginning)
initial_recipe_writer_agent = LlmAgent(
    name="InitialRecipeWriterAgent",
    model=GEMINI_MODEL,
    instruction="""You are a basic Recipe Writer.
Write a *simple, initial draft* of a recipe for a meal entered by the user.
Include very basic ingredients and steps (3-5 items each).
Do not make it too complex, as this is just a starting point.
Respond in the following JSON format:
{{
  "recipe_name": string,
  "ingredients": [string],
  "steps": [string]
}}
""",

description="Generates an initial draft of a recipe based on user input.",

output_key="current_recipe"
)


#  STEP 2a: Recipe Critic Agent (Inside the Refinement Loop)
critic_agent_in_loop = LlmAgent(
    name="RecipeCriticAgent",
    model=GEMINI_MODEL,
    instruction="""You are an expert Culinary Critic AI.
You are reviewing a recipe draft and providing constructive feedback for improvement. Assess the recipe for clarity, common sense, and potential for improvement (e.g., healthiness, flavor enhancement, missing details).

**Recipe to Review:**
{current_recipe}

**Task:**
Review the recipe for clarity, common sense, and potential for improvement (e.g., healthiness, flavor enhancement, missing details). Then provide your critique.

IF you identify 1-2 *clear and actionable* suggestions for improvement (e.g., "Add more vegetables", "Specify cooking temperature", "Suggest a healthier alternative for butter"):
Provide these specific suggestions concisely. Output *only* the critique text.

ELSE IF the recipe is clear, functional, and requires no obvious major improvements for its basic form:
Respond *exactly* with the phrase "Recipe looks great!" and nothing else. Avoid purely subjective stylistic preferences if the core recipe is sound.

Do not add explanations. Output only the critique OR the exact completion phrase.

You must follow these rules strictly.
""",
    description="Reviews the current recipe and provides constructive feedback for improvement.",
    output_key="critique_feedback"
)

# STEP 2b: Recipe Refiner Agent (Inside the Refinement Loop)
refiner_agent_in_loop = LlmAgent(
    name="RecipeRefinerAgent",
    model=GEMINI_MODEL,
    instruction="""You are a Recipe Refinement Assistant.
Your goal is to improve the given recipe based on the provided critique OR to exit the process if the critique indicates the recipe is satisfactory.

**Current Recipe:**
{current_recipe}

**Critique/Suggestions:**
{critique_feedback}

**Task:**
Analyze the 'Critique/Suggestions'.
IF the critique is *exactly* "Recipe looks great!":
You MUST call the 'exit_loop' function. Do not output any text.
ELSE (the critique contains actionable feedback):
Carefully apply the suggestions to improve the 'Current Recipe'. Output *only* the refined recipe text.
Avoid adding unnecessary complexity; keep the recipe clear and straightforward.


Do not add explanations. Either output the refined recipe OR call the exit_loop function.
""",
    description="Refines the recipe based on critique, or calls exit_loop if critique indicates completion.",
    tools=[exit_loop],
    output_key="current_recipe"
)


# STEP 3: Recipe Refinement Loop Agent
refinement_loop_agent = LoopAgent(
  name="RecipeRefinementLoopAgent",
  sub_agents=[
    critic_agent_in_loop,
    refiner_agent_in_loop
  ],
  max_iterations=5,
  description="A loop agent that refines a recipe based on critique until it meets quality standards or exits the loop."
)


# STEP 4: Overall Sequential Agent
root_agent = SequentialAgent(
  name ="RecipeCreationAgent",
  sub_agents=[
    initial_recipe_writer_agent,
    refinement_loop_agent
  ],
  description="An agent that creates and refines a recipe based on user input through an initial draft and iterative critique."
  
)
