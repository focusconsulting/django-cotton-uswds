# Install the package with demo dependencies

just: 
    just --list
install:
    uv pip install -e ".[demo]"

# Run the demo development server
demo:
    cd demo_project && uv run python manage.py runserver

# Build static site for GitHub Pages
build:
    cd demo_project && uv run python manage.py collectstatic --noinput && uv run python manage.py distill-local dist --force

# Remove built static files
clean:
    rm -rf demo_project/dist demo_project/staticfiles

# Run CI checks locally using act
ci *args:
    act push {{ args }}
