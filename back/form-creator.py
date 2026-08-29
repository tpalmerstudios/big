import json

def output_select(name, label, options):
    print(f'<label for="{name}">{label}:</label>')
    print(f'    <select id="{name}-select" name="{name}">')
    print(f'        <option value="">--Choose One or Randomize--</option>')
    
    for option in options:
        value = option["value"]
        option_label = option["label"]
        
        print(f'        <option value="{value}">{option_label}</option>')

    print(" </select>")


with open("book-data/book-concepts.json", "r", encoding="utf-8") as file:
    data = json.load(file)

variables = data["variables"]

for variable in variables:
    if variable["type"] == "select":
        output_select(
            variable["name"],
            variable["label"],
            variable["options"]
        )
