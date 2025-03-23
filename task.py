from crewai import Task, Crew 
from dotenv import load_dotenv
import os
from tools import yt_tool
from agents import blog_researcher, blog_writer
from langchain_groq import ChatGroq  

# Load environment variables
load_dotenv()

# Ensure Groq API key is set
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Research task
research_task = Task(
    description=(
        "Identify the video on {topic}."
        "Get detailed information about video from the channel."
    ),
    expected_output="A comprehensive 3 paragraph long report based on the topic {topic} of video content.",
    tools=[yt_tool],
    agent=blog_researcher,
)

# Writing task with language model configuration
write_task = Task(
    description=(
        "Get the info from the youtube channel on the topic {topic}"
    ),
    expected_output="Summarize the info from the youtube channel video on the topic {topic} and create the content for the blog",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)

# Create the crew
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    verbose=2
)

# Execute the crew's tasks for a specific topic
result = crew.kickoff(inputs={"topic": "GenAI Trends 2025"})  # Replace with your desired topic
print(result)