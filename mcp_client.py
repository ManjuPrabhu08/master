import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

# Load .env
load_dotenv()

# Setup OpenAI client
openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"),base_url=os.getenv("OPENAI_BASE_URL"))

async def main():
    # Fix: unpack the tuple returned by streamablehttp_client correctly
    async with streamablehttp_client("http://localhost:8000/mcp") as rw_tuple:
        read, write, _ = rw_tuple

        async with ClientSession(read, write) as session:
            await session.initialize()

            print("Connected to MCP server, fetching blog resource...")
            content = await session.read_resource("blog://post")

            print("Summarizing content using GPT model..." )
            resp = await openai_client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {"role": "system", "content": "You summarize blog posts."},
                    {"role": "user", "content": f"Summarize the following:\n\n{content}"}
                ],
                max_tokens=300,
                temperature=0.7
            )

            summary = resp.choices[0].message.content
            print("\n--- Summary ---\n")
            print(summary)

if __name__ == "__main__":
    asyncio.run(main())