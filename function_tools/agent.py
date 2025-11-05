from typing import Any, Dict

import requests
from google.adk.agents import LlmAgent


def fetch_user_data(user_id: int) -> Dict[str, Any]:
    """
    Fetches user data from the JSONPlaceholder API for a given user ID.

    This tool makes an HTTP GET request to the /users endpoint of JSONPlaceholder API.

    Args:
        user_id (int): The ID of the user to fetch (valid range: 1-10).

    Returns:
        Dict[str, Any]: A dictionary containing the user's data if found, otherwise a dictionary with an 'error' message.
    """

    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}", timeout=5)
        response.raise_for_status()
        user_data = response.json()

        if user_data and isinstance(user_data, dict):
            return {"status": "success", "user_data": user_data}
        else:
            return {"status": "error", "message": f"User with ID {user_id} not found."}

    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"Network error: {e}"}
    except Exception as e:
        return {"status": "error", "message": f"Unexpected error: {e}"}

def format_user_profile(user_data_json: Dict[str, Any]) -> str:
    """
    Formats user data (from fetch_user_data) into a Markdown profile string.

    Args:
        user_data_json (Dict[str, Any]): The 'user_data' field from fetch_user_data output.

    Returns:
        str: Markdown string for the user profile, or error message if input is invalid.
    """
    if not isinstance(user_data_json, dict):
        return "Error: Invalid user data provided for formatting."

    name = user_data_json.get("name", "N/A")
    username = user_data_json.get("username", "N/A")
    email = user_data_json.get("email", "N/A")
    phone = user_data_json.get("phone", "N/A").split(' ')[0]
    website = user_data_json.get("website", "N/A")
    company_name = user_data_json.get("company", {}).get("name", "N/A")
    city = user_data_json.get("address", {}).get("city", "N/A")

    return (
        f"## User Profile: {name}\n\n"
        f"**Username:** {username}\n\n"
        f"**Email:** {email}\n\n"
        f"**Phone:** {phone}\n\n"
        f"**Website:** {website}\n\n"
        f"**Company:** {company_name}\n\n"
        f"**Location:** {city}\n\n"
    )

root_agent = LlmAgent(
    name="UserProfileViewer",
    model="gemini-2.0-flash",
    instruction=(
        "You are a helpful assistant for user profile lookup. "
        "When a user requests a profile by ID, always use the 'fetch_user_data' tool first. "
        "If the fetch is successful, pass ONLY the 'user_data' field to the 'format_user_profile' tool. "
        "If there is an error, present the error message to the user. "
        "Always display the formatted profile in Markdown. "
        "If any step fails, clearly inform the user of the error and suggest a valid user ID (1-10)."
    ),
    description="Fetches and formats user profile information from JSONPlaceholder API.",
    tools=[fetch_user_data, format_user_profile]
)

# Example usage
if __name__ == "__main__":
    # Simulate fetching and formatting user profile for user ID 1
    result = fetch_user_data(1)
    if result.get("status") == "success":
        print(format_user_profile(result["user_data"]))
    else:
        print(result.get("message", "Unknown error."))
