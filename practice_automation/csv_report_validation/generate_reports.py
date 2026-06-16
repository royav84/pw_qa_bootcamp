# Dictionary containing all CSV test scenarios
# Each key = CSV file name
# Each value = CSV file content
reports = {

    # ===== HAPPY FLOW =====

    # Valid CSV file
    # Contains correct header and valid data rows
    "valid_report.csv": [

        # Header row
        ["id", "name", "email"],

        # Valid user row
        ["1", "Roi", "roi@test.com"],

        # Another valid user row
        ["2", "Dan", "dan@test.com"]
    ],

    # ===== EDGE CASES =====

    # CSV file contains only header row
    # No actual data rows exist
    "empty_data_report.csv": [

        # Header only
        ["id", "name", "email"]
    ],

    # Completely empty CSV file
    # File contains 0 rows
    "empty_file_report.csv": [

    ],

    # CSV row with broken structure
    # First data row contains only 2 columns instead of 3
    "broken_columns_report.csv": [

        # Valid header
        ["id", "name", "email"],

        # Broken row missing email column
        ["1", "Roi"],

        # Valid row
        ["2", "Dan", "dan@test.com"]
    ],

    # Invalid CSV header
    # Header names do not match expected structure
    "bad_header_report.csv": [

        # Wrong header names
        ["identifier", "fullname", "mail"],

        # Valid data row
        ["1", "Roi", "roi@test.com"]
    ],

    # Invalid email format
    # Email missing '@' symbol
    "invalid_email_report.csv": [

        # Valid header
        ["id", "name", "email"],

        # Invalid email row
        ["1", "Roi", "roi-test.com"]
    ]
}