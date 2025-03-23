# CrewAI_Agent

Automates blog content creation from YouTube videos using CrewAI, LangChain, and Groq LLM.

## Features
- Extracts relevant YouTube video content.
- Generates structured blog posts.
- Uses CrewAI agents for research and writing.

## Installation
```sh
pip install -r requirements.txt
```
Create a `.env` file with:
```sh
GROQ_API_KEY=your_api_key_here
```

## Usage
Run the script:
```sh
python cre.py
```
The blog content is saved in `new-blog-post.md`.

## Configuration
- Modify `tools.py` to change the YouTube channel.
- Edit `cre.py` to set a different topic.

## Dependencies
- crewai
- crewai_tools
- langchain
- langchain-groq

## License
MIT License

