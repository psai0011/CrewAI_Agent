from crewai_tools import YoutubeChannelSearchTool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up embedchain configuration to use a different embedding model
from embedchain.config import AppConfig, EmbedderConfig

# Configure to use a different embedding model
embedder_config = EmbedderConfig(
    provider="huggingface",
    model="sentence-transformers/all-MiniLM-L6-v2"  # This is a free model that doesn't require API keys
)

app_config = AppConfig(
    embedder=embedder_config
)

# Initialize the tool with a specific youtube channel and custom config
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle='@krishnaik06',
    config=app_config
)