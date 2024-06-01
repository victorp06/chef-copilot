#!/bin/bash

# Activate virtual environment if you have one
# source /path/to/your/virtualenv/bin/activate

# Run the FastAPI application with Uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
