# Reflection Question 1:Python can automate reading, transforming, and writing data much faster than  Excel when working with large files or repetitive tasks. Excel is easier for quick visual analysis and manual editing, while Python is better for reusable workflows that can be run repeatedly without user interaction.
# Reflection Question 2: A retail store could use an append-mode log file to track daily sales reports.Append mode is useful because it preserves all previous records and adds new entries over time, creating a complete history that can be reviewed later.
import csv
from datetime import datetime
INPUT_FILE = "data/sales.csv"
OUTPUT_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"
# EXERCISE 2
print("=" * 50)
print("EXERCISE 2 - Read and Print Raw Rows")
print("=" * 50)
with open(INPUT_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# EXERCISE 3 
print("\n" + "=" * 50)
print("EXERCISE 3 - Skip the Header")
print("=" * 50)
with open(INPUT_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)
# EXERCISE 4
print("\n" + "=" * 50)
print("EXERCISE 4 - Compute Totals")
print("=" * 50)
total_revenue = 0
with open(INPUT_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue += line_total
        print(
            f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}"
        )
print(f"\nOverall Total Revenue: ${total_revenue:.2f}")
# EXERCISE 5 - Filter and Write
print("\n" + "=" * 50)
print("EXERCISE 5 - Filter and Write")
print("=" * 50)
original_count = 0
written_count = 0
with open(INPUT_FILE, "r") as infile, open(
    OUTPUT_FILE, "w", newline=""
) as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        original_count += 1
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        if total > 100:
            writer.writerow(
                [product, f"{price:.2f}", quantity, f"{total:.2f}"]
            )
            written_count += 1
print(f"Rows in original file: {original_count}")
print(f"Rows written to cleaned.csv: {written_count}")
# EXERCISE 6 - DictReader
print("\n" + "=" * 50)
print("EXERCISE 6 - DictReader")
print("=" * 50)
dict_total_revenue = 0
with open(INPUT_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        dict_total_revenue += price * quantity
print(f"Total Revenue Using DictReader: ${dict_total_revenue:.2f}")
# csv.reader is useful when you know the column positions and want simpler code.
# DictReader is easier to read and maintain because columns are accessed by name.
# EXERCISE 7 - Sales Summary by Product
print("\n" + "=" * 50)
print("EXERCISE 7 - Sales Summary by Product")
print("=" * 50)
summary = {}
with open(INPUT_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        revenue = float(row["price"]) * int(row["quantity"])
        if product in summary:
            summary[product] += revenue
        else:
            summary[product] = revenue
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")
# EXERCISE 8 - Append Mode Log
print("\n" + "=" * 50)
print("EXERCISE 8 - Append Mode Log")
print("=" * 50)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as log_file:
    log_file.write(
        f"{timestamp} | Total Revenue = ${total_revenue:.2f}\n"
    )
print("Log entry added to data/run_log.txt")
print(f"Total Revenue Logged: ${total_revenue:.2f}")