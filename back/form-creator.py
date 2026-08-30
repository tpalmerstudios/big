import json

def output_select(name, label, options):
    print(f'<label for="{name}">{label}:</label>')
    print(f'    <select id="{name}-select" name="{name}">')
    print(f'        <option value="">--Choose One--</option>')
    
    for option in options:
        value = option["value"]
        option_label = option["label"]
        
        print(f'        <option value="{value}">{option_label}</option>')

    print(" </select>")

def output_slider(name, label, minimum, maximum, default):
    print(f'<label for="{name}">{label}:</label>')
    print(f'<input type="range" min="{minimum}" max="{maximum}" value="{default}" class="slider" id="{name}">')

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
    elif variable["type"] == "slider":
                  output_slider(
                      variable["name"],
                      variable["label"],
                      variable["min"],
                      variable["max"],
                      variable.get("default", variable["min"])
                  )
