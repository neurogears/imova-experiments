git clean -fdx .venv
git clean -fx uv.lock
irm https://astral.sh/uv/install.ps1 | iex
uv sync --all-extras