# Google Agent Developer Kit - Projects & Examples

A collection of AI agent examples built with the [Google Agent Developer Kit (ADK)](https://google.github.io/adk-docs/). This repository demonstrates various agent architectures and use cases using Gemini 2.0 Flash.

## Projects

### 1. **Parallel Agent**
Multi-platform content generation pipeline that runs multiple content generators simultaneously:
- Tweet Generator (Twitter/X)
- Instagram Caption Generator
- Blog Post Intro Generator
- Content Consolidator (aggregates outputs)

### 2. **Sequential Agent**
Content ideation pipeline with step-by-step workflow:
- Idea Generator (brainstorms content ideas)
- Content Creator (develops full content)
- Optimizer (refines and improves)

### 3. **Function Tools Agent**
User profile fetcher with external API integration:
- Fetches user data from JSONPlaceholder API
- Formats profiles into Markdown
- Demonstrates tool chaining and error handling

### 4. **Travel Advisor**
Travel planning assistant with custom tools:
- Distance calculator between cities
- Restaurant recommendations
- Hotel finder
- Itinerary planner

### 5. **YouTube Helper**
YouTube content strategy assistant:
- Video idea generator based on trends
- Title optimizer for SEO
- Description writer
- Thumbnail suggestions

### 6. **Loop Agent** & **Built-in Tools**
Additional examples exploring ADK capabilities and standard tool usage.

## Architecture Patterns

- **LlmAgent**: Individual AI agents with specific instructions
- **ParallelAgent**: Run multiple agents concurrently
- **SequentialAgent**: Chain agents with dependent workflows

## Key Features

✓ Tool integration and chaining
✓ Error handling and validation
✓ Markdown formatting
✓ Multi-platform content generation
✓ Custom tool implementations
✓ API integration examples
