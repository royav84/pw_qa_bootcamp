reports = {

    # ===== HAPPY FLOW =====

    "valid_report.csv": [
        ["id", "name", "email"],
        ["1", "Roi", "roi@test.com"],
        ["2", "Dan", "dan@test.com"]
    ],

    # ===== EDGE CASES =====

    # Header only
    "empty_data_report.csv": [
        ["id", "name", "email"]
    ],

    # Completely empty file
    "empty_file_report.csv": [],

    # Broken column count
    "broken_columns_report.csv": [
        ["id", "name", "email"],
        ["1", "Roi"],
        ["2", "Dan", "dan@test.com"]
    ],

    # Invalid header
    "bad_header_report.csv": [
        ["identifier", "fullname", "mail"],
        ["1", "Roi", "roi@test.com"]
    ],

    # Invalid email
    "invalid_email_report.csv": [
        ["id", "name", "email"],
        ["1", "Roi", "roi-test.com"]
    ]
}