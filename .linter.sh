#!/bin/bash
cd /home/kavia/workspace/code-generation/taskpilot-pro-98697-933b1389/taskpilot_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

