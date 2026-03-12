import asyncio
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio

server_params = StdioServerParameters(command="uv", args=["run", "server.py"])

async def run():
    print("🚀 Starting MCP Python Client...")

    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                print("📡 Connecting to MCP server...")

                # Initialising the connection
                await session.initialize()
                print("✅ Connected to MCP server successfully!")

                # List available tools
                tools_result = await session.list_tools()
                print("Listing tools")
                for tool in tools_result.tools:
                    #print(f"Tool name: {tool.name}")
                    print(f"Tool description: {tool.description}")
                    
                
                # List available resources
                resources_result = await session.list_resources()
                print("Listing resources")
                for resource in resources_result.resources:
                    print(f"Resource name: {resource.name}")
                    print(f"Resource description: {resource.description}")
                
                # Invoking a tool
                print("Calling addition tool")
                addResult = await session.call_tool("add", arguments={"a": 1, "b": 3})
                print(f"Result of addition: {addResult.content[0].text}")

                # Reading a resource
                print("Reading greeting resource")
                read_result = await session.read_resource("greeting://Nomaan")
                for content in read_result.contents:
                    print(f"Content: {content.text}")
                    print(f"MIME Type: {content.mimeType}")

                print("\n✨ Client operations completed successfully!")

    except Exception as ex:
        print(f"❌ Error running MCP client: {ex}")
        raise

if __name__ == "__main__":
    asyncio.run(run())