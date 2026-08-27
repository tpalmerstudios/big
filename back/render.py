from pathlib import Path
from jinja2 import Environment, FileSystemLoader

BACKEND_DIR = Path(__file__).parent
PROJECT_ROOT = BACKEND_DIR.parent

TEMPLATES_DIR = PROJECT_ROOT / "back" / "templates"
PARTIALS_DIR = PROJECT_ROOT / "back" / "templates" / "partials"
SOURCE_DIR = PROJECT_ROOT / "src"
FRONT_DIR = PROJECT_ROOT / "front"

file_loader = FileSystemLoader([TEMPLATES_DIR, SOURCE_DIR, PARTIALS_DIR])
env = Environment(loader=file_loader)

def build_pages ():
    FRONT_DIR.mkdir(parents=True, exist_ok=True)
    for page_path in SOURCE_DIR.glob("*.html"):
        template = env.get_template(page_path.name)
        data = {
            "author": "Isaiah Palmer",
            "keywords": "book, author, writer, ideas, writers-block, creative",
            "description": "The BIG is designed to help create ideas for authors and others, by chance and by choice.",
            "title": "The Book Idea Generator"
}

        rendered_html = template.render(data)

        output_file = FRONT_DIR / page_path.name
        output_file.write_text(rendered_html)
        print(f"Compiled: source/{page_path.name} -> front/{output_file.name}")

if __name__ == "__main__":
    build_pages()
