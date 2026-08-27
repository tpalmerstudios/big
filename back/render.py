from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('layout.html')

data = {
    "author": "Isaiah Palmer",
    "keywords": "book, author, writer, ideas, writers-block, creative",
    "description": "The BIG is designed to help create ideas for authors and others, by chance and by choice.",
    "title": "The Book Idea Generator"
}

output = template.render(data)

print(output)
