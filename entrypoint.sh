#!/bin/bash

if [ ! -f ".env" ]; then
  echo "Creating .env file with placeholders..."
  cat <<EOT >> .env
OPENAI_API_KEY=your-openai-api-key
REDDIT_CLIENT_ID=your-reddit-client-id
REDDIT_CLIENT_SECRET=your-reddit-client-secret
REDDIT_USER_AGENT=your-reddit-user-agent
CRUNCHBASE_API_KEY=your-crunchbase-api-key
HUGGINGFACE_HUB_TOKEN=your-huggingface-hub-token

EOT
  echo ".env file created. Please update it with your API keys."
fi

python src/docker.py
