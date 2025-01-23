import os
from dotenv import load_dotenv
from os_computer_use.llm_provider import LLMProvider
from os_computer_use.osatlas_provider import OSAtlasProvider
from os_computer_use.showui_provider import ShowUIProvider

# Load environment variables from .env file
load_dotenv()

# LLM providers use the OpenAI specification and require a base URL:


class GroqProvider(LLMProvider):
    base_url = "https://api.groq.com/openai/v1"
    api_key = os.getenv("GROQ_API_KEY")
    aliases = {"llama3.2": "llama-3.2-90b-vision-preview", "llama3.3": "llama-3.3-70b-versatile"}


# grounding_model = ShowUIProvider()
grounding_model = OSAtlasProvider()

vision_model = GroqProvider("llama3.2")

action_model = GroqProvider("llama3.3")
