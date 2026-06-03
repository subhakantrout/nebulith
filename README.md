# Nebulith

> **A self-hosted AI workspace. Chat with local models, run autonomous agents, and manage your documents, emails, and tasks with privacy-first AI.**

![Topics](https://img.shields.io/badge/Topics-ai%20%7C%20self--hosted%20%7C%20workspace%20%7C%20llm%20%7C%20agents%20%7C%20local--first%20%7C%20privacy-blue?style=flat-square)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg?style=flat-square)
![Docker](https://img.shields.io/badge/docker-ready-2496ED.svg?logo=docker&style=flat-square)
[![GitHub Stars](https://img.shields.io/github/stars/subhakantrout/nebulith?style=social)](https://github.com/subhakantrout/nebulith/stargazers)

Nebulith is an advanced, self-hosted AI workspace designed to provide a comprehensive, local-first alternative to cloud-based AI assistants. Run autonomous agents, serve local models, and manage your intelligence workflows directly on your own hardware, ensuring complete data privacy and security.

## Key Features

- **Conversational AI Interface**
  Seamlessly chat with local models or external APIs. Easily integrate providers such as vLLM, llama.cpp, Ollama, OpenRouter, and OpenAI.
  
- **Autonomous Agents**
  Empower agents with extensive tooling, allowing them to autonomously execute multi-step tasks across web browsing, file management, shell execution, and persistent memory.

- **Model Cookbook**
  Intelligently scan your hardware for optimal model recommendations. Download and serve VRAM-aware models (GGUF, FP8, AWQ) with a single click.

- **Deep Research Capabilities**
  Execute multi-step research runs that gather, read, and synthesize extensive source material into comprehensive visual reports.

- **Model Comparison**
  Conduct blind, side-by-side A/B tests between multiple models to objectively evaluate performance without bias.

- **Intelligent Document Editing**
  A robust multi-tab editor supporting Markdown, HTML, and CSV, enhanced with syntax highlighting, AI-driven edits, and contextual suggestions.

- **Persistent Memory & Skills**
  Agents evolve over time through persistent vector memory and keyword retrieval, powered by ChromaDB and fastembed (ONNX).

- **AI-Augmented Email**
  A fully integrated IMAP/SMTP inbox featuring AI triage: auto-tagging, urgency reminders, draft generation, and intelligent spam filtering.

- **Notes, Tasks, & Calendar Integration**
  Manage daily workflows with scheduled tasks, cron-style jobs, and CalDAV synchronization across multiple platforms.

- **Mobile Responsive Design**
  A fully responsive, installable Progressive Web App (PWA) optimized for touch gestures and on-the-go access.

- **Additional Utilities**
  Built-in image and theme editors, vision model support, PDF parsing, web search capabilities, session management, and Two-Factor Authentication (2FA).

## Quick Start

### Docker Setup (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SubhakantaRout/nebulith.git
   cd nebulith
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   ```

3. **Deploy the stack:**
   ```bash
   docker compose up -d --build
   ```

4. **Access the application:**
   Navigate to `http://localhost:7000`. On the first boot, an admin account is created. Retrieve the temporary password from the Docker logs:
   ```bash
   docker compose logs nebulith
   ```

### Native Installation (Linux / macOS)

Requirements: Python 3.11+.

```bash
git clone https://github.com/SubhakantaRout/nebulith.git
cd nebulith
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python setup.py
python -m uvicorn app:app --host 127.0.0.1 --port 7000
```

### Apple Silicon

For GPU-accelerated Cookbook serving on an M-series Mac:

```bash
git clone https://github.com/SubhakantaRout/nebulith.git
cd nebulith
./start-macos.sh
```
The application will launch at `http://127.0.0.1:7860`.

### Windows Installation

Run the automated setup script in PowerShell:

```powershell
git clone https://github.com/SubhakantaRout/nebulith.git
cd nebulith
powershell -ExecutionPolicy Bypass -File .\launch-windows.ps1
```

## Security & Architecture

Nebulith grants powerful capabilities including shell access, file operations, and external API integrations. Treat your deployment as an administrative console. 

- Keep `AUTH_ENABLED=true` for all network-accessible deployments.
- Expose the application strictly via a trusted reverse proxy with HTTPS enabled.
- Avoid exposing internal service ports (e.g., ChromaDB, SearXNG, Ollama) directly to the internet.

### System Architecture

```text
app.py                   # FastAPI application entry point
core/                    # Authentication, database management, middleware
src/                     # LLM orchestration, agent loops, search processors
routes/                  # API endpoints (chat, sessions, documents, memory)
services/                # Core services (memory, hardware diagnostics)
static/                  # Modular frontend UI (HTML, JS, CSS)
```

## Configuration

Nebulith's environment can be configured via the `.env` file for deployment-level settings, while user preferences and model configurations are managed directly within the UI settings panel.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
