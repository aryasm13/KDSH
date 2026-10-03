import csv
import json

INPUT_CSV = "/Users/kavyajain/Downloads/KdshRag-main_7/test.csv"
OUTPUT_JSONL = "questions.jsonl"


def build_question(char, content, label):
    return (
        f"tell the reason the given character {char} "
        f"back story {content} {label} with the narrative"
    )


def main():
    count = 0

    with open(INPUT_CSV, newline="", encoding="utf-8") as csvfile, \
         open(OUTPUT_JSONL, "w", encoding="utf-8") as outfile:

        reader = csv.DictReader(csvfile)

        for idx, row in enumerate(reader):
            char = row["char"].strip()
            content = row["content"].strip()
            label = row["label"].strip()

            question = build_question(char, content, label)

            record = {
                "id": idx,
                "question": question,
                "golden_answers": []
            }

            # 🔑 JSONL: write ONE JSON per line
            outfile.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1

    print(f"[DONE] Generated {count} questions → {OUTPUT_JSONL}")


if __name__ == "__main__":
    main()
