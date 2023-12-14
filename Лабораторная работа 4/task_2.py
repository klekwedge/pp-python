import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    result = sum(item['score'] * item['weight'] for item in data)

    result_rounded = round(result, 3)

    return result_rounded

print(task())
