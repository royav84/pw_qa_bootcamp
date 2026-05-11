import csv
import os

REPORTS_FOLDER = (
    "practice_automation/"
    "csv_report_validation/reports"
)

EXPECTED_HEADER = ["id", "name", "email"]

for file_name in os.listdir(REPORTS_FOLDER):

    if not file_name.endswith(".csv"):
        continue

    file_path = os.path.join(REPORTS_FOLDER, file_name)

    print(f"\nTEST CASE | {file_name}")

    try:

        with open(file_path, newline='', encoding="utf-8") as file:

            reader = csv.reader(file)

            rows = list(reader)

            # ===== EMPTY FILE =====

            if len(rows) == 0:

                print(
                    "Validate report file is not empty | FAIL | "
                    "Remove all content from CSV file"
                )

                continue

            print(
                "Validate report file is not empty | PASS"
            )

            header = rows[0]

            # ===== HEADER =====

            if header != EXPECTED_HEADER:

                print(
                    "Validate report header structure | FAIL | "
                    "Modify CSV header columns"
                )

                continue

            print(
                "Validate report header structure | PASS"
            )

            # ===== DATA ROWS =====

            if len(rows) == 1:

                print(
                    "Validate report contains data rows | FAIL | "
                    "Delete all rows except header"
                )

                continue

            print(
                "Validate report contains data rows | PASS"
            )

            # ===== ROWS =====

            for row_index, row in enumerate(rows[1:], start=2):

                if len(row) != len(EXPECTED_HEADER):

                    print(
                        f"Validate Row {row_index} column count | "
                        f"FAIL | Remove one column from row "
                        f"{row_index}"
                    )

                    break

                print(
                    f"Validate Row {row_index} column count | PASS"
                )

                email = row[2]

                if "@" not in email or "." not in email:

                    print(
                        f"Validate Row {row_index} email format | "
                        f"FAIL | Replace email with invalid value"
                    )

                    break

                print(
                    f"Validate Row {row_index} email format | PASS"
                )

    except Exception as error:

        print(
            f"Unexpected Error | FAIL | {error}"
        )