from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("BlogPostServer")

# Resource exposing the blog post
@mcp.resource("blog://post")
async def get_blog_post() -> str:
    try:
        with open("blog_post.txt", "r", encoding="utf-8") as f:
            content = f.read()
            print(f"Blog post read successfully: {len(content)} characters")
            return content  # Return string directly, not a tuple
    except FileNotFoundError:
        print("blog_post.txt not found!")
        return "Error: blog_post.txt missing!"

if __name__ == "__main__":
    # Run the server using streamable HTTP transport
    mcp.run(transport="streamable-http")
