# MCP Calendar Tool (Claude Integration)

A calendar tool built using Model Context Protocol (MCP) and integrated with Claude Desktop.

## 🚀 What It Does
- Accepts natural language prompts
- Uses MCP structured tool invocation
- Adds calendar events automatically
- Returns confirmation to the user

## 🏗 Architecture Flow
User Prompt → Claude → MCP Tool Invocation → Calendar Event Created → Confirmation

<img width="1920" height="1080" alt="MCP-calendar" src="https://github.com/user-attachments/assets/cefac625-ffdc-4a59-a5d9-c09a823abfed" />


### Example Prompt
"Add an event "Blood Donation Drive" on October 8, 2025 from 11 am to 3 pm."

### Response
"I've added the "Blood Donation Drive" event for October 8, 2025 from 11:00 AM to 3:00 PM (240 minutes duration)."



## 🧰 Tech Stack
- Python
- MCP (Model Context Protocol)
- Claude Desktop
- Structured Tool Invocation

## 📁 Files
- `calendar_tool.py` – Main tool logic
- `pyproject.toml` – Project configuration
- `uv.lock` – Dependency lock file
