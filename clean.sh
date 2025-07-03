#!/bin/bash

# Description: Recursively remove common Python build/cache/junk files

echo "Cleaning Python project trash files..."

# List of patterns to remove
patterns=(
    "__pycache__"
    "*.pyc"
    "*.pyo"
    "*.egg"
    "*.egg-info"
    ".pytest_cache"
    ".mypy_cache"
    ".coverage"
    "htmlcov"
    ".tox"
    "build"
    "dist"
)

# Remove each pattern
for pattern in "${patterns[@]}"; do
    echo "Removing $pattern..."
    find . -name "$pattern" -exec rm -rf {} +
done

echo "Cleanup complete."
