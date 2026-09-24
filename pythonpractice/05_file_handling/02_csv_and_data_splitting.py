"""
================================================================================
   MODULE 05: CSV LOGGING & FILE SPLITTING (EVEN / ODD PARTITIONING)
================================================================================
This script covers:
  1. Writing structured tabular data to CSV
  2. Parsing and reading CSV files
  3. Reading numbers from a file and partitioning into separate evens.txt and odds.txt
================================================================================
"""

import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def banner(title: str):
    print("\n" + "=" * 75)
    print(f"  {title.upper()}")
    print("=" * 75)


def main():
    banner("1. Writing and Appending to CSV")
    csv_file = "students_records.csv"
    students = [
        ("Roll", "Name", "Score"),
        (101, "Sarthak", 95),
        (102, "Rahul", 82),
        (103, "Priya", 91)
    ]

    with open(csv_file, "w", encoding="utf-8") as f:
        for row in students:
            f.write(f"{row[0]},{row[1]},{row[2]}\n")
    print(f"Records saved to '{csv_file}'.")

    print("\nReading CSV file content:")
    with open(csv_file, "r", encoding="utf-8") as f:
        for line in f:
            print("  ", line.strip().split(","))

    banner("2. Partitioning Data into Separate Files (Even / Odd)")
    # Generate source numbers file
    with open("raw_numbers.txt", "w", encoding="utf-8") as f:
        f.write("14\n23\n8\n99\n42\n57\n100\n")

    # Read and split
    with open("raw_numbers.txt", "r", encoding="utf-8") as src, \
         open("evens.txt", "w", encoding="utf-8") as even_file, \
         open("odds.txt", "w", encoding="utf-8") as odd_file:

        for line in src:
            num = int(line.strip())
            if num % 2 == 0:
                even_file.write(f"{num}\n")
            else:
                odd_file.write(f"{num}\n")

    print("Partition complete:")
    with open("evens.txt", "r", encoding="utf-8") as ef:
        print("  evens.txt:", ef.read().split())
    with open("odds.txt", "r", encoding="utf-8") as of:
        print("  odds.txt: ", of.read().split())


if __name__ == "__main__":
    main()
