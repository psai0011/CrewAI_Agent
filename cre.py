from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

## Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.Sequential,  # Optimal: Sequential task execution is default
    verbose=True,  # Added verbose flag for better logging
    memory=True,
    share_crew=True
)

## Start the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL VS Data Science'})  # Fixed 'input' to 'inputs'
print(result)