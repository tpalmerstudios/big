import json
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
    for page_path in SOURCE_DIR.rglob("*.html"):
        relative_path = page_path.relative_to(SOURCE_DIR)
        
        template = env.get_template(relative_path.as_posix())
        data = {
            "author": "Isaiah Palmer",
            "keywords": "book, author, writer, ideas, writers-block, creative",
            "description": "The BIG is designed to help create ideas for authors and others, by chance and by choice.",
            "title": "The Book Idea Generator"
}

        json_path = page_path.with_suffix(".json")
        if json_path.exists():
                custom_data = json.loads(json_path.read_text(encoding="utf-8"))
                data.update(custom_data)

        data["current_page"] = relative_path.as_posix()
        rendered_html = template.render(data)

        output_file = FRONT_DIR / relative_path

        output_file.parent.mkdir(parents=True, exist_ok=True)

        output_file.write_text(rendered_html)
        print(f"Compiled: src/{relative_path} -> front/{relative_path}")

if __name__ == "__main__":
    build_pages()
