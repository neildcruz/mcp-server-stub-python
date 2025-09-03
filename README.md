# mcp-server-stub-python
This is a base MCP server implementation using the MCP Python SDK which can be extended with tool or agent integrations.

## Prerequisites
- Python 3.10 or higher installed.
- You must use the Python MCP SDK 1.2.0 or higher.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mcp-server-stub-python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd mcp-server-stub-python
   ```
3. Install the required dependencies:
   ```bash
   uv install -r requirements.txt
   ```

## Running the Server
1. In VS code
   ```json
   {
   "mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\ABSOLUTE\\PATH\\TO\\PARENT\\FOLDER\\weather",
        "run",
        "server.py"
      ]
    }
   }
   ```