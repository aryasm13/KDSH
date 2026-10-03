import json

# 1. Read the novel into a variable
with open("/Users/kavyajain/Downloads/KdshRag-main_7/dataset/KDSH/monte_cristo/novel.txt", "r", encoding="utf-8") as f:
    novel_text = f.read()

# 2. Create the object in YOUR format
record = {
    "id": 0,
    "doc_id": 1,
    "title": "castaways",
    "contents": novel_text
}


# 3. Write JSON safely
with open("/Users/kavyajain/Downloads/KdshRag-main_7/dataset/KDSH/monte_cristo/corpus.jsonl", "w", encoding="utf-8") as f:
    json.dump(record, f, ensure_ascii=False)

print("✅ dataset.json written correctly")
