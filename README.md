# ML/Data Science Project

This project uses machine learning and data science packages.

## Environment

This project uses the **`.venvstk`** virtual environment located at `../.venvstk/`

### Installed Packages
- numpy 2.3.4
- (add more as you install them)

## Setup

### Option 1: Open in VS Code
```bash
code /Users/chuck/gitrepositories/project-ml
```
The Python interpreter will automatically be set to `.venvstk/bin/python`

### Option 2: Activate environment manually
```bash
source ../.venvstk/bin/activate
python testrandom.py
```

### Option 3: Run with uv
```bash
uv run --python ../.venvstk/bin/python testrandom.py
```

## Installing New Packages

Use `uv` for fast package installation:
```bash
uv pip install <package-name> --python ../.venvstk/bin/python
```

## Scripts
- `testrandom.py` - Dice rolling example using numpy
