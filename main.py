import os

FORTUNE = "You will be asked to think outside the box, then graded on staying inside it."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(FORTUNE)
