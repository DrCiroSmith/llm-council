"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - ALL FREE OpenRouter models (verified live May 2026)
COUNCIL_MODELS = [
    "nvidia/nemotron-3-super-120b-a12b:free",
    "qwen/qwen3-coder:free",
    "google/gemma-4-31b-it:free",
    "openai/gpt-oss-120b:free",
]

# Chairman model - synthesizes final response (strongest free reasoner)
CHAIRMAN_MODEL = "nvidia/nemotron-3-super-120b-a12b:free"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
