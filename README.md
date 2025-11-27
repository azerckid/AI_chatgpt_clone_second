# AI Agent Masterclass: ChatGPT Clone

A powerful AI assistant built with Streamlit, capable of Web Search, File Search, Code Execution, Image Generation, and MCP (Model Context Protocol) integration.

## 🌟 Features

- **Advanced Chat Interface**: Built with Streamlit for a smooth user experience.
- **Multi-Modal Capabilities**:
  - **Web Search**: Real-time internet search using DuckDuckGo.
  - **File Search**: RAG (Retrieval-Augmented Generation) for uploaded documents.
  - **Code Interpreter**: Writes and executes Python code in a sandboxed environment.
  - **Image Generation**: Creates images using DALL-E 3.
- **MCP Integration**:
  - **Hosted MCP Tool (Client)**: Connects to external MCP servers (e.g., Context7) to extend knowledge.
  - **Local MCP Server (Server)**: Exposes the agent's own tools to other MCP-compliant clients (like Claude Desktop).
- **Session Management**: Persistent chat history with SQLite and session reset functionality.

## 🛠️ Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (for dependency management)
- OpenAI API Key

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd chatgpt-clone
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Configure Environment**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=sk-...
   VECTOR_STORE_ID=vs_...  # Optional: For persistent file search
   ```

## 💻 Usage

This application supports two distinct modes of operation.

### 1. Web App Mode (Client)
Run the interactive chat interface in your browser.

```bash
streamlit run main.py
```

- **Functionality**: Chat with the agent, upload files, generate images, and run code.
- **MCP Client**: The agent can connect to external MCP servers defined in the configuration.

### 2. MCP Server Mode (Server)
Run the agent as a local MCP server. This allows other applications to use this agent's tools.

```bash
python main.py mcp
```

- **Functionality**: Runs headlessly and communicates via Stdio.
- **Integration**: Configure your MCP client (e.g., Claude Desktop) to run this command to access tools like Web Search and Code Interpreter.

## 📂 Project Structure

- `main.py`: The entry point for both the Streamlit app and the MCP server.
- `agents/`: Core logic for the AI agent, tools, and session management.
- `chat-gpt-clone-memory-new.db`: SQLite database for storing chat history.
- `.env`: Configuration file for API keys.

## ❓ Troubleshooting

**"Container is expired" Error**
If you encounter this error, it means the OpenAI Code Interpreter session has timed out.
- **Fix**: Click the **"Reset memory"** button in the sidebar to clear the session and start fresh.
