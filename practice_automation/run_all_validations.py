# Import subprocess module
import subprocess

# Import datetime module
from datetime import datetime

# Import os module
import os

# Import sys module
# Used for current Python interpreter
import sys


# List containing all automation suites
TESTS = [

    {
        "name": "CSV Column Validation",

        "path": (
            "practice_automation/"
            "csv_column_validation/check_columns.py"
        )
    },

    {
        "name": "URL Status Validation",

        "path": (
            "practice_automation/"
            "url_status_validation/url_status_check.py"
        )
    },

    {
        "name": "CSV Report Validation",

        "path": (
            "practice_automation/"
            "csv_report_validation/scan_reports.py"
        )
    }
]


# List storing suite execution results
results = []


# Print execution title
print("\n========== AUTOMATION PRACTICE SUITE ==========\n")


# Get current Python interpreter
python_executable = sys.executable


print(f"Using Python Interpreter: {python_executable}")


# ===== EXECUTE SUITES =====

for test in TESTS:

    test_name = test["name"]

    test_path = test["path"]

    try:

        result = subprocess.run(

            [python_executable, test_path],

            capture_output=True,

            text=True
        )

        output = result.stdout + "\n" + result.stderr

        print(f"\n===== DEBUG OUTPUT: {test_name} =====")

        print(output)

        if "| FAIL" in output:

            final_status = "FAILED"

        else:

            final_status = "PASSED"

        results.append({

            "suite_name": test_name,

            "suite_status": final_status,

            "output": output
        })

    except Exception as error:

        results.append({

            "suite_name": test_name,

            "suite_status": "ERROR",

            "output": str(error)
        })


# ===== SUMMARY =====

passed_count = len([

    result for result in results

    if result["suite_status"] == "PASSED"
])

failed_count = len([

    result for result in results

    if result["suite_status"] != "PASSED"
])

execution_time = datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S"
)


# ===== HTML REPORT =====

html_content = f"""
<html>

<head>

<title>Automation Practice Report</title>

<style>

body {{
    font-family: Arial;
    background-color: #f4f4f4;
    padding: 30px;
}}

h1 {{
    color: #222;
}}

.summary {{
    background: white;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 30px;
}}

.suite {{
    background: white;
    padding: 20px;
    margin-bottom: 30px;
    border-radius: 10px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}}

.PASSED {{
    border-left: 10px solid green;
}}

.FAILED {{
    border-left: 10px solid red;
}}

.ERROR {{
    border-left: 10px solid orange;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}}

th {{
    background: #333;
    color: white;
    padding: 12px;
    text-align: left;
}}

td {{
    border: 1px solid #ddd;
    padding: 10px;
    vertical-align: top;
    white-space: pre-line;
}}

.pass {{
    color: green;
    font-weight: bold;
}}

.fail {{
    color: red;
    font-weight: bold;
}}

</style>

</head>

<body>

<h1>Automation Practice Report</h1>

<div class="summary">

<h2>Execution Summary</h2>

<p>
<strong>Execution Time:</strong>
{execution_time}
</p>

<p>
<strong>Total Suites:</strong>
{len(results)}
</p>

<p>
<strong>Passed Suites:</strong>
{passed_count}
</p>

<p>
<strong>Failed Suites:</strong>
{failed_count}
</p>

</div>

"""


# ===== SUITES =====

for result in results:

    suite_name = result["suite_name"]

    suite_status = result["suite_status"]

    output = result["output"]

    html_content += f"""

    <div class="suite {suite_status}">

    <h2>{suite_name}</h2>

    <h3>Final Status: {suite_status}</h3>

    <table>

    <tr>
        <th>Test Case</th>
        <th>Result</th>
        <th>Reproduction Steps</th>
        <th>Failure Details</th>
    </tr>

    """

    output_lines = output.splitlines()

    current_test_case = ""

    for line in output_lines:

        clean_line = line.strip()

        if not clean_line:
            continue

        if "|" not in clean_line:
            continue

        parts = clean_line.split("|", maxsplit=3)

        if parts[0].strip() == "TEST CASE":

            if len(parts) >= 2:

                current_test_case = parts[1].strip()

            continue

        validation_name = parts[0].strip()

        result_text = ""
        reproduction_steps = ""
        failure_details = ""

        if len(parts) >= 2:
            result_text = parts[1].strip()

        if len(parts) >= 3:
            reproduction_steps = parts[2].strip()

        if len(parts) >= 4:
            failure_details = parts[3].strip()

        css_class = ""

        if result_text == "PASS":

            css_class = "pass"

        elif result_text == "FAIL":

            css_class = "fail"

        html_content += f"""

        <tr>

            <td>
                <strong>{current_test_case}</strong><br>
                {validation_name}
            </td>

            <td class="{css_class}">
                {result_text}
            </td>

            <td>
                {reproduction_steps}
            </td>

            <td>
                {failure_details}
            </td>

        </tr>

        """

    html_content += """

    </table>

    </div>

    """

html_content += """

</body>
</html>

"""

REPORTS_FOLDER = (
    "practice_automation/test_reports"
)

os.makedirs(REPORTS_FOLDER, exist_ok=True)

existing_reports = [

    file_name for file_name in os.listdir(REPORTS_FOLDER)

    if file_name.endswith(".html")
]

for file_name in existing_reports:

    if file_name.startswith("newest_"):

        old_path = os.path.join(
            REPORTS_FOLDER,
            file_name
        )

        new_name = file_name.replace(
            "newest_",
            "",
            1
        )

        new_path = os.path.join(
            REPORTS_FOLDER,
            new_name
        )

        os.rename(old_path, new_path)

existing_reports = [

    os.path.join(REPORTS_FOLDER, file_name)

    for file_name in os.listdir(REPORTS_FOLDER)

    if file_name.endswith(".html")
]

existing_reports.sort(

    key=os.path.getctime
)

while len(existing_reports) >= 5:

    oldest_report = existing_reports[0]

    os.remove(oldest_report)

    existing_reports.pop(0)

timestamp = datetime.now().strftime(
    "%Y-%m-%d_%H-%M-%S"
)

report_name = (
    f"newest_automation_report_{timestamp}.html"
)

report_file = os.path.join(

    REPORTS_FOLDER,

    report_name
)

with open(report_file, "w", encoding="utf-8") as file:

    file.write(html_content)

print(
    f"\nHTML report created: {report_file}"
)