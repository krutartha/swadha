#!/bin/bash

# Development server script for Swadhā Life
echo "🌿 Starting Swadhā Life Development Server..."

# Check if Python is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Python not found. Please install Python 3.x"
    exit 1
fi

# Check if the live server script exists
if [ -f "live_server.py" ]; then
    echo "🚀 Starting live development server with auto-reload..."
    $PYTHON_CMD live_server.py
else
    echo "🚀 Starting simple development server..."
    $PYTHON_CMD dev_server.py
fi
