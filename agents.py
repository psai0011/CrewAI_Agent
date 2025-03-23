from crewai import Agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from crewai_tools import YoutubeChannelSearchTool

# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    model_name="llama3-70b-8192",  
    temperature=0.7,
    groq_api_key=os.environ["GROQ_API_KEY"]
)

# Define YouTube tool since it's imported but not defined
yt_tool = YoutubeChannelSearchTool()

# Create a senior blog content researcher
blog_researcher = Agent(
    role="Blog Researcher from Youtube Videos",
    goal="Get the relevant video content for the topic {topic} from yt channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding Videos in AI Data Science, Machine Learning and GEN AI and providing suggestion "
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

# Create a senior writer agent with YT tool
blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video {topic} from yt channel",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)