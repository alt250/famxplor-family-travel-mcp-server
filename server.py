import os
from typing import Any
from dotenv import load_dotenv
import httpx
from mcp.server.fastmcp import FastMCP
import argparse
import sys
import traceback
import logging

# Initialize FastMCP server
mcp = FastMCP("famxplor")


class Config:
    """Configuration for Famxplor MCP server."""
    def __init__(self, api_base: str, api_key: str | None):
        self.api_base = api_base
        self.api_key = api_key

        if self.api_key is None:
            raise ValueError("API key is required for Famxplor API.")

CONFIG = Config(
    api_base=os.getenv("FAMXPLOR_API_HOST", "https://api.famxplor.com"), 
    api_key=os.getenv("FAMXPLOR_API_KEY", None)
)

USER_AGENT = "famxplor-mcp-server"


async def make_famxplor_request(url: str, json: Any) -> dict[str, Any] | None:
    """Make a request to the Famxplor API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        "api-key": CONFIG.api_key,
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, timeout=30.0, json=json)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error during Famxplor API request: {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            return None


def format_activity(activity: dict) -> str:
    """Format an activity into a readable string."""
    return (
        f"Title: {activity.get('title', 'No title')}\n"
        f"More info URL: {activity.get('url', 'No URL')}\n"
        f"Image URL: {activity.get('img_url', 'No image')}\n"
        f"Location: ({activity.get('lat', 0)}, {activity.get('lon', 0)})\n"
    )

@mcp.tool()
async def search_family_activities(lat: float, lon: float, max_dist: float, user_query: str) -> str:
    """
    Retrieves family activities that are geographically close to the specified location.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
        max_dist (float): Maximum distance from the provided coordinates in meters.
        user_query (str): The precise user's query for which activities are being searched. Used to return relevant activities.

    Returns:
        str: A formatted string containing the information of the family activities. Each activity has a title, more info URL, image URL, and location.
    """
    logging.info(f"search_family_activities lat={lat} lon={lon} max_dist={max_dist} user_query='{user_query}'")

    url = f"{CONFIG.api_base}/v1/nearest-activities"
    params = {
        "lat": lat,
        "lon": lon,
        "max_distance": max_dist
    }
    data = await make_famxplor_request(url, params)

    if not data or "activities" not in data:
        return "Unable to fetch activities."

    if not data["activities"]:
        return "No activities found for this location."

    activities = [format_activity(activity) for activity in data["activities"]]
    return "\n---\n".join(activities)


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="famxplor-mcp-server")
    parser.add_argument("--api-host", type=str, default="https://api.famxplor.com", help="Famxplor API base URL")
    parser.add_argument("--api-key", type=str, help="Famxplor API key")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    load_dotenv(verbose=True)

    # Initialize and run the server
    mcp.run(transport="streamable-http")

