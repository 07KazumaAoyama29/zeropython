from pathlib import Path
import json

numbers = [2,3,2,4,4,6]

path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)