# Generative AI with LangChain - Local Setup

This repository contains experiments and learning projects for working with LangChain and various generative AI models.

**Note:** This setup focuses on traditional Python scripts with live development using Docker volume mounting for instant code changes without rebuilds.

## Quick Start

### Docker with Live Development (Recommended)

1. **Set up your API keys:**

   ```bash
   cp config_template.py config.py
   # Edit config.py and add your actual API keys
   ```

2. **Build the Docker container (one-time setup):**

   ```bash
   docker build -t gen-ai-experiments .
   ```

3. **Run with live code mounting:**

   ```bash
   # This mounts your src/ directory directly into the container
   # Changes to your code are instantly available inside Docker
   docker run -it -v "$(pwd)/src:/src" gen-ai-experiments
   ```

4. **Run your Python scripts:**
   ```bash
   # In the container, you're already in /src so just run:
   python projects/0-test-setup/setup.py
   python projects/1-langchain-basics/basic_example.py
   ```

## Development Workflow

The volume mounting approach gives you the best of both worlds:

- **Edit locally**: Use VS Code or your favorite editor on your host machine
- **Run in container**: Execute in a consistent Python environment with all dependencies

### Example workflow:

```bash
# Terminal 1: Start container with live mounting
docker run -it -v "$(pwd)/src:/workspace/src" gen-ai-experiments

# Terminal 2: Edit code in VS Code
code src/projects/2-chains/my_experiment.py

# Back in Terminal 1: Run immediately (no rebuild needed!)
python src/projects/2-chains/my_experiment.py
```

## API Keys Setup

You'll need API keys for various services. The most important ones are:

### Required for most projects:

- **OpenAI API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)
- **Anthropic API Key**: Get from [Anthropic Console](https://console.anthropic.com/)

### Optional (for specific chapters):

- **Google AI API Key**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **LangSmith API Key**: Get from [LangSmith](https://smith.langchain.com/) (for tracing)
- **Pinecone API Key**: Get from [Pinecone](https://www.pinecone.io/) (for vector databases)

### Setting up API keys:

1. Copy `config_template.py` to `config.py`
2. Edit `config.py` and add your API keys
3. Import and call `set_environment()` at the start of your scripts:
   ```python
   from config import set_environment
   set_environment()
   ```

## Important Security Notes

- **NEVER commit `config.py` files to git**
- The `.gitignore` file is set up to protect your API keys
- Always use the template file as a starting point

## Troubleshooting

### Docker Issues

- Make sure Docker is running
- If you need to restart a container: `docker run -it -v "$(pwd)/src:/workspace/src" gen-ai-experiments`
- To rebuild after dependency changes: `docker build -t gen-ai-experiments .`

### API Key Issues

- Make sure your API keys are valid and have sufficient credits
- Check that you're calling `set_environment()` before using any LangChain components
