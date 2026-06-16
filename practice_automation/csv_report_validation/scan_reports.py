# Import Python built-in CSV module
# Used for reading CSV files
import csv


# Import OS module
# Used for folder and file operations
import os


# Path to reports folder
REPORTS_FOLDER = (
    "practice_automation/"
    "csv_report_validation/reports"
)


# Expected CSV header structure
EXPECTED_HEADER = ["id", "name", "email"]


# ===== FAILURE DETAILS BUILDER =====

# Helper function used for building
# readable failure analysis details
def build_failure_details(

    validation_type,

    expected_result,

    actual_result,

    file_name,

    row_number="N/A"
):

    return (

        f"Validation Type:\n"
        f"{validation_type}\n\n"

        f"Expected Result:\n"
        f"{expected_result}\n\n"

        f"Actual Result:\n"
        f"{actual_result}\n\n"

        f"File Name:\n"
        f"{file_name}\n\n"

        f"Row Number:\n"
        f"{row_number}"
    )


# ===== FILE LOOP =====

# Loop through all files in reports folder
for file_name in os.listdir(REPORTS_FOLDER):

    # Skip non-CSV files
    if not file_name.endswith(".csv"):
        continue

    # Build full file path
    file_path = os.path.join(

        REPORTS_FOLDER,

        file_name
    )

    # Print current test case
    print(f"TEST CASE | {file_name}")

    try:

        # Open CSV file
        with open(

            file_path,

            newline='',

            encoding="utf-8"

        ) as file:

            # Create CSV reader object
            reader = csv.reader(file)

            # Convert rows into list
            rows = list(reader)

            # ===== EMPTY FILE VALIDATION =====

            if len(rows) == 0:

                failure_details = build_failure_details(

                    validation_type="Empty File",

                    expected_result=(
                        "CSV file should contain "
                        "header and data rows"
                    ),

                    actual_result="File contains 0 rows",

                    file_name=file_name
                )

                print(

                    "Validate report file is not empty | "

                    "FAIL | "

                    "Remove all content from CSV file | "

                    f"{failure_details}"
                )

                continue

            print(

                "Validate report file is not empty | "

                "PASS"
            )

            # Get header row
            header = rows[0]

            # ===== HEADER VALIDATION =====

            if header != EXPECTED_HEADER:

                failure_details = build_failure_details(

                    validation_type="Header Structure",

                    expected_result=EXPECTED_HEADER,

                    actual_result=header,

                    file_name=file_name
                )

                print(

                    "Validate report header structure | "

                    "FAIL | "

                    "Modify CSV header columns | "

                    f"{failure_details}"
                )

                continue

            print(

                "Validate report header structure | "

                "PASS"
            )

            # ===== DATA ROWS VALIDATION =====

            if len(rows) == 1:

                failure_details = build_failure_details(

                    validation_type="Missing Data Rows",

                    expected_result=(
                        "CSV file should contain "
                        "at least 1 data row"
                    ),

                    actual_result="Only header row exists",

                    file_name=file_name
                )

                print(

                    "Validate report contains data rows | "

                    "FAIL | "

                    "Delete all rows except header | "

                    f"{failure_details}"
                )

                continue

            print(

                "Validate report contains data rows | "

                "PASS"
            )

            # ===== ROW VALIDATION =====

            for row_index, row in enumerate(

                rows[1:],

                start=2
            ):

                # ===== COLUMN COUNT VALIDATION =====

                if len(row) != len(EXPECTED_HEADER):

                    failure_details = build_failure_details(

                        validation_type="Column Count",

                        expected_result=(
                            f"{len(EXPECTED_HEADER)} columns"
                        ),

                        actual_result=(
                            f"{len(row)} columns\n"
                            f"Failed Row: {row}"
                        ),

                        file_name=file_name,

                        row_number=row_index
                    )

                    print(

                        f"Validate Row {row_index} "
                        f"column count | "

                        "FAIL | "

                        f"Remove one column from row "
                        f"{row_index} | "

                        f"{failure_details}"
                    )

                    break

                print(

                    f"Validate Row {row_index} "
                    f"column count | "

                    "PASS"
                )

                # ===== EMAIL VALIDATION =====

                email = row[2]

                if "@" not in email or "." not in email:

                    failure_details = build_failure_details(

                        validation_type="Email Format",

                        expected_result=(
                            "Valid email containing "
                            "'@' and '.'"
                        ),

                        actual_result=email,

                        file_name=file_name,

                        row_number=row_index
                    )

                    print(

                        f"Validate Row {row_index} "
                        f"email format | "

                        "FAIL | "

                        "Replace email with invalid value | "

                        f"{failure_details}"
                    )

                    break

                print(

                    f"Validate Row {row_index} "
                    f"email format | "

                    "PASS"
                )

    # ===== UNEXPECTED ERRORS =====

    except Exception as error:

        failure_details = build_failure_details(

            validation_type="Unexpected Runtime Error",

            expected_result="Script should run successfully",

            actual_result=str(error),

            file_name=file_name
        )

        print(

            "Unexpected Error | "

            "FAIL | "

            "Check application logs | "

            f"{failure_details}"
        )