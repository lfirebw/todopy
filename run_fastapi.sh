#!/bin/bash
source env/bin/activate
uvicorn fastapi_app.main:app --reload --port 8001