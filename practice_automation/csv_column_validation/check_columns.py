# Import Python built-in CSV module
# Used for reading CSV files row by row
import csv


# Path to the CSV file we want to validate
FILE_PATH = (
    "practice_automation/"
    "csv_column_validation/users.csv"
)


# Expected number of columns in the CSV file
EXPECTED_COLUMNS = 3


# Expected CSV header structure
EXPECTED_HEADER = ["id", "name", "email"]


# Print test suite title
print("TEST CASE | CSV Structure Validation")


# Start validation flow
try:

    # Open CSV file in read mode
    # newline='' prevents blank lines issue in CSV parsing
    # encoding='utf-8' supports special characters
    with open(FILE_PATH, newline='', encoding="utf-8") as file:

        # Create CSV reader object
        reader = csv.reader(file)

        # Convert all CSV rows into list
        rows = list(reader)

        # ===== EMPTY FILE VALIDATION =====

        # Check if file contains 0 rows
        if len(rows) == 0:

            # Print FAIL result if file is empty
            print(
                "Validate CSV file is not empty | FAIL | "
                "Open users.csv and remove all content | "
                "File is empty"
            )

            # Stop execution
            exit()

        # Print PASS result if file contains rows
        print(
            "Validate CSV file is not empty | PASS"
        )

        # Get first row from CSV as header row
        header = rows[0]

        # ===== HEADER VALIDATION =====

        # Compare actual header against expected header
        if header != EXPECTED_HEADER:

            # Print FAIL if headers are different
            print(
                "Validate CSV header structure | FAIL | "
                "Open users.csv and modify/remove columns | "
                f"{header}"
            )

            # Stop execution
            exit()

        # Print PASS if header structure is valid
        print(
            "Validate CSV header structure | PASS"
        )

        # Count actual number of columns
        actual_columns = len(header)

        # ===== COLUMN COUNT VALIDATION =====

        # Validate actual column count
        if actual_columns != EXPECTED_COLUMNS:

            # Print FAIL if column count is incorrect
            print(
                "Validate CSV column count | FAIL | "
                "Add or remove columns from users.csv | "
                f"{header}"
            )

            # Stop execution
            exit()

        # Print PASS if column count is correct
        print(
            "Validate CSV column count | PASS"
        )

        # ===== DATA ROWS VALIDATION =====

        # Validate that file contains data rows
        # Header alone is not enough
        if len(rows) <= 1:

            # Print FAIL if only header exists
            print(
                "Validate CSV contains data rows | FAIL | "
                "Delete all rows except header | "
                "No data rows found"
            )

            # Stop execution
            exit()

        # Print PASS if data rows exist
        print(
            "Validate CSV contains data rows | PASS"
        )

        # ===== ROW VALIDATION =====

        # Loop through all rows except header
        # start=2 because CSV row numbering starts after header
        for row_index, row in enumerate(rows[1:], start=2):

            # ===== ROW STRUCTURE VALIDATION =====

            # Validate row contains expected number of columns
            if len(row) != EXPECTED_COLUMNS:

                # Print FAIL if row structure is broken
                print(
                    f"Validate Row {row_index} structure | FAIL | "
                    f"Remove one column from row "
                    f"{row_index} | "
                    f"{row}"
                )

                # Continue checking next rows
                continue

            # Print PASS if row structure is valid
            print(
                f"Validate Row {row_index} structure | PASS"
            )

            # ===== EMAIL VALIDATION =====

            # Get email column from current row
            email = row[2]

            # Validate basic email format
            if "@" not in email or "." not in email:

                # Print FAIL if email format is invalid
                print(
                    f"Validate Row {row_index} email format | FAIL | "
                    f"Replace email in row {row_index} "
                    f"with invalid value | "
                    f"{row}"
                )

                # Continue checking next rows
                continue

            # Print PASS if email format is valid
            print(
                f"Validate Row {row_index} email format | PASS"
            )


# Handle missing file scenario
except FileNotFoundError:

    # Print FAIL if CSV file does not exist
    print(
        "Validate CSV file exists | FAIL | "
        "Delete users.csv file | "
        f"{FILE_PATH}"
    )


# Handle unexpected runtime errors
except Exception as error:

    # Print generic FAIL with error details
    print(
        f"Unexpected Error | FAIL | {error} | "
        "Unknown row"
    )