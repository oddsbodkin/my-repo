import json

items = json.loads(
    '[{"id":1, "text": "Item 1"}, {"id":2, "text": "Item 2"}, {"id":3, "text": "Item 3"}]'
)

for item in items:
    print(item["text"])

def greet(greeting, name):
    """returns a greeting

    Args:
        greeting (string): a greet world
        name (string): a persons name

    Returns:
        string: a greeting with a name

    """
    return f'{greeting} {name}'

print(greet("hello", "world"))



