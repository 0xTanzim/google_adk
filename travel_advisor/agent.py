from google.adk import Agent


def get_distance(from_city: str, to_city: str) -> dict:
    """Get the distance between two cities in kilometers.

    Args:
        from_city (str): The starting city.
        to_city (str): The destination city.

    Returns:
        dict: A dictionary containing the distance information.
    """
    if from_city.lower() == "san francisco" and to_city.lower() == "miami":
        return {
            "status": "success",
            "response": [
                "The distance between San Francisco and Miami is approximately 4,130 kilometers.",
                "The weather in Miami is approximately 42 degrees Fahrenheit."
            ]
        }
    else:
        return {
            "status": "error",
            "message": "Distance information for the specified cities is not available."
        }


def get_restaurants(city: str) -> list:
    """Get a list of popular restaurants in a given city.

    Args:
        city (str): The city to search for restaurants.
    Returns:
        list: A list of popular restaurants in the city.
    """
    if city.lower() == "miami":
        return ["Joe's Stone Crab", "Versailles Restaurant", "La Mar by Gastón Acurio"]
    elif city.lower() == "san francisco":
        return ["The House", "Sotto Mare", "Zuni Café"]
    else:
        return ["No restaurant data available for this city."]


root_agent = Agent(
    name="TravelAdvisor",
    model="gemini-2.0-flash",
    description=(
        "An agent that provides travel advice including distances between cities, "
        "popular restaurants, and weather information."
    ),
    instruction=(
        "You are a travel advisor agent. You can provide information about distances between cities "
        "and popular restaurants in a given city along with weather information. "
        "Use the provided functions to get the required information based on user queries. "
        "If the information is not available, respond with an appropriate message."
    ),
    tools=[get_distance, get_restaurants],
)
