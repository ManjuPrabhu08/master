# MCP Blog Summarizer

## Description
This project demonstrates a simple Model Context Protocol (MCP) setup:
- **Server**: Serves a network-related blog post as a resource.
- **Client**: Connects to the MCP server, retrieves the blog post, and uses OpenAI GPT-4 to summarize it.

## Setup Instructions


1.Clone the repository:

```bash
git clone <repo_url>
cd MCP_Assignment


2. Create a Python virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

pip install -r requirements.txt


3.Add your OpenAI API key in the .env file:

OPENAI_API_KEY=sk-your_openai_api_key
OPENAI_BASE_URL=https://api.openai.com/v1


4. Start the MCP server:
python mcp_server.py

5. In a separate terminal, run the client:
python mcp_client.py
