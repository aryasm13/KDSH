import csv

input_csv = "input.csv"     # your original file
output_csv = "output.csv"   # converted file

with open(input_csv, "r", newline="", encoding="utf-8") as infile, \
     open(output_csv, "w", newline="", encoding="utf-8") as outfile:

    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        if row["prediction"].lower() == "consistent":
            row["prediction"] = "1"
        elif row["prediction"].lower() == "contradict":
            row["prediction"] = "0"
        writer.writerow(row)

print("✅ Conversion complete. Saved to", output_csv)
