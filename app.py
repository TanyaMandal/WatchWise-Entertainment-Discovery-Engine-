import os
from dotenv import load_dotenv
from google import genai
import json

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
gemini_model = os.getenv("GEMINI_MODEL")

# Validate Gemini API key
if not api_key:
    raise ValueError("GEMINI_API_KEY is not configured in environment variables.")

# Create the Gemini API client
client = genai.Client(api_key=api_key)

# Generation configuration
generation_config = {
    'max_output_tokens': 2000,
    'thinking_level': 'medium',
}

# Strict JSON Schema for WatchWise recommendations
watch_recommendation_schema = {
    "type": "object",
    "properties": {
        "curator_note": {
            "type": "string",
            "description": "A brief, engaging introductory note from the AI film curator matching the user's vibe."
        },
        "recommendations": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Title of the movie or web series"
                    },
                    "genre": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Genres associated with the title"
                    },
                    "runtime_or_seasons": {
                        "type": "string",
                        "description": "Runtime for movies or number of seasons for series"
                    },
                    "ott_platform": {
                        "type": "string",
                        "description": "Popular streaming platform where it is available"
                    },
                    "match_reason": {
                        "type": "string",
                        "description": "Explanation of why this matches the user's vibe or query"
                    }
                },
                "required": ["title", "genre", "runtime_or_seasons", "ott_platform", "match_reason"]
            },
            "description": "List of curated movie or show recommendations"
        }
    },
    "required": ["curator_note", "recommendations"]
}

def get_watch_recommendations(user_query, preferred_platform, max_runtime):
    """
    Sends the user's entertainment query and constraints to Gemini and returns structured recommendations.
    """
    prompt = f"""
    ROLE:
    You are WatchWise, an expert AI entertainment curator and personal recommendation engine.

    OBJECTIVE:
    Analyze the user's natural language vibe/query and constraints to recommend the best movies or web series.

    USER PREFERENCES & CONSTRAINTS:
    - User Query / Vibe: {user_query}
    - Preferred OTT Platform: {preferred_platform}
    - Runtime / Length Constraint: {max_runtime}

    RULES:
    - Provide accurate titles, genres, and realistic streaming platforms.
    - Ensure the recommendations strictly align with the user's emotional tone or vibe request.
    - Keep match explanations concise, engaging, and directly tied to the user's input.
    """

    response = client.interactions.create(
        model=gemini_model,
        input=prompt,
        generation_config=generation_config,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": watch_recommendation_schema
        }
    )
    
    return json.loads(response.output_text)