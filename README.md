# MCP 101 - A Model Context Protocol Playground

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-1.26%2B-orange)](https://modelcontextprotocol.io/)

A hands-on implementation of a **Model Context Protocol (MCP)** server and client. This project serves as a foundational template for building AI-powered tools and resources using the MCP standard and `FastMCP`.

## ✨ Features
- **Arithmetic Tool**: An `add` function registered as an MCP tool for basic calculations.
- **Dynamic Resources**: A `greeting` resource with URL-templated URI scheme (`greeting://{name}`).
- **Bidirectional Communication**: Full setup for `stdio`-based client-server interaction.
- **Modern Tooling**: Managed with `uv` for seamless dependency and environment handling.

## 🛠 Prerequisites
- **Python 3.13+**
- **[uv](https://docs.astral.sh/uv/)** (Recommended Python package manager)

## 📦 Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nomaan-ahmad/MCP-101.git
   cd MCP-101
   ```

2. **Install Dependencies**:
   This project uses `uv` for fast, reproducible environments.
   ```bash
   uv sync
   ```

## 🏃 How to Run

### 1. Run the MCP Server
To start the server in standalone mode (useful for testing manually):
```bash
uv run server.py
```

### 2. Run the MCP Client
The client is configured to automatically spawn and connect to the server. Simply run:
```bash
uv run client.py
```

Upon running, the client will:
- Connect to the server via `stdio`.
- List available tools and resources.
- Execute the `add` tool.
- Read the `greeting` resource.

---

*Made with ❤️ by Nomaan Ahmad*
