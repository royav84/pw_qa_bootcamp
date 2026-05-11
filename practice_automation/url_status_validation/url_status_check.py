import requests

TEST_CASES = [

    {
        "name": "Google Homepage Returns 200",
        "url": "https://www.google.com",
        "expected": 200
    },

    {
        "name": "GitHub Homepage Returns 200",
        "url": "https://www.github.com",
        "expected": 200
    },

    {
        "name": "Microsoft Homepage Returns 200",
        "url": "https://www.microsoft.com",
        "expected": 200
    },

    {
        "name": "Wikipedia Returns 403",
        "url": "https://www.wikipedia.org",
        "expected": 403
    }
]

TIMEOUT = 5

for test_case in TEST_CASES:

    test_name = test_case["name"]
    url = test_case["url"]
    expected = test_case["expected"]

    print(f"\nTEST CASE | {test_name}")

    try:

        response = requests.get(url, timeout=TIMEOUT)

        actual_result = response.status_code

        if actual_result == expected:

            print("URL Validation | PASS")

        else:

            print(
                f"URL Validation | FAIL | "
                f"Expected: {expected} "
                f"Actual: {actual_result}"
            )

    except Exception as error:

        print(f"URL Validation | FAIL | {error}")