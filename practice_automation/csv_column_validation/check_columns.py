import csv

FILE_PATH = (
    "practice_automation/"
    "csv_column_validation/users.csv"
)

EXPECTED_COLUMNS = 3
EXPECTED_HEADER = ["id", "name", "email"]

print("TEST CASE | CSV Structure Validation")

try:

    with open(FILE_PATH, newline='', encoding="utf-8") as file:

        reader = csv.reader(file)

        rows = list(reader)

        # ===== EMPTY FILE =====

        if len(rows) == 0:

            print(
                "Validate CSV file is not empty | FAIL | "
                "Open users.csv and remove all content | "
                "File is empty"
            )

            exit()

        print(
            "Validate CSV file is not empty | PASS"
        )

        header = rows[0]

        # ===== HEADER VALIDATION =====

        if header != EXPECTED_HEADER:

            print(
                "Validate CSV header structure | FAIL | "
                "Open users.csv and modify/remove columns | "
                f"{header}"
            )

            exit()

        print(
            "Validate CSV header structure | PASS"
        )

        actual_columns = len(header)

        # ===== COLUMN COUNT =====

        if actual_columns != EXPECTED_COLUMNS:

            print(
                "Validate CSV column count | FAIL | "
                "Add or remove columns from users.csv | "
                f"{header}"
            )

            exit()

        print(
            "Validate CSV column count | PASS"
        )

        # ===== DATA ROWS =====

        if len(rows) <= 1:

            print(
                "Validate CSV contains data rows | FAIL | "
                "Delete all rows except header | "
                "No data rows found"
            )

            exit()

        print(
            "Validate CSV contains data rows | PASS"
        )

        # ===== ROW VALIDATION =====

        for row_index, row in enumerate(rows[1:], start=2):

            # Row structure

            if len(row) != EXPECTED_COLUMNS:

                print(
                    f"Validate Row {row_index} structure | FAIL | "
                    f"Remove one column from row {row_index} | "
                    f"{row}"
                )

                continue

            print(
                f"Validate Row {row_index} structure | PASS"
            )

            # Email validation

            email = row[2]

            if "@" not in email or "." not in email:

                print(
                    f"Validate Row {row_index} email format | FAIL | "
                    f"Replace email in row {row_index} "
                    f"with invalid value | "
                    f"{row}"
                )

                continue

            print(
                f"Validate Row {row_index} email format | PASS"
            )

except FileNotFoundError:

    print(
        "Validate CSV file exists | FAIL | "
        "Delete users.csv file | "
        f"{FILE_PATH}"
    )

except Exception as error:

    print(
        f"Unexpected Error | FAIL | {error} | "
        "Unknown row"
    )