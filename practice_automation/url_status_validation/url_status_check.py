# Import requests library
# Used for sending HTTP requests
import requests


# List containing URL validation test cases
TEST_CASES = [

    # ===== HAPPY FLOW =====

    # Validate Google homepage returns HTTP 200
    {
        "name": "Google Homepage Returns 200",

        "url": "https://www.google.com",

        "expected": 200
    },

    # Validate GitHub homepage returns HTTP 200
    {
        "name": "GitHub Homepage Returns 200",

        "url": "https://www.github.com",

        "expected": 200
    },

    # Validate Microsoft homepage returns HTTP 200
    {
        "name": "Microsoft Homepage Returns 200",

        "url": "https://www.microsoft.com",

        "expected": 200
    },

    # ===== EDGE CASE =====

    # Validate Wikipedia returns HTTP 403
    {
        "name": "Wikipedia Returns 403",

        "url": "https://www.wikipedia.org",

        "expected": 403
    }
]


# Maximum request timeout in seconds
TIMEOUT = 5


# Loop through all test cases
for test_case in TEST_CASES:

    # Get test case name
    test_name = test_case["name"]

    # Get target URL
    url = test_case["url"]

    # Get expected HTTP status code
    expected = test_case["expected"]

    # Print current test case name
    print(f"TEST CASE | {test_name}")

    try:

        # Send HTTP GET request
        response = requests.get(

            url,

            timeout=TIMEOUT
        )

        # Get actual HTTP status code
        actual_result = response.status_code

        # ===== STATUS CODE VALIDATION =====

        # Compare actual result against expected result
        if actual_result == expected:

            # Print PASS result
            print(
                "Validate URL response status | "
                "PASS | "
                "N/A | "
                f"Expected: {expected}, "
                f"Actual: {actual_result}"
            )

        else:

            # Print FAIL result
            print(
                "Validate URL response status | "
                "FAIL | "
                "Modify expected status code or URL | "
                f"Expected: {expected}, "
                f"Actual: {actual_result}"
            )

    # Handle unexpected runtime/network errors
    except Exception as error:

        # Print FAIL result with actual error
        print(
            "Validate URL response status | "
            "FAIL | "
            "Disconnect internet or use invalid URL | "
            f"{error}"
        )