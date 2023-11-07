# Description: A simple test case runner for Python
# Author: Patsagorn Yuenyong (ptsgrn.dev)
# License: MIT
# Documentation: README.md

import sys
import os
import subprocess
import requests
# get problem id from argv
problem_id = sys.argv[1]
api_token = ""
if os.path.exists("api_token.txt"):
    with open("api_token.txt", "r") as f:
        api_token = f.read().strip()
if not api_token:
    print("API Token not found. Please put your API Token in api_token.txt")

# check if problem and testcase exists
if not os.path.exists("problems/" + problem_id + ".py"):
    if not "--create" in sys.argv:
        # prompt to create problem file
        print("Problem and testcases file not found. Create one? [Y/n]")
    if "--create" in sys.argv or input().lower() == 'y':
        with open("problems/" + problem_id + ".py", "w") as f:
            f.write("# Path: problems/" + problem_id + ".py\n")
            f.write("# Your code here")
            print("Problem file created")
    else:
        print("Aborted")
        exit(0)
if not os.path.exists("problems/" + problem_id + ".tc.md"):
    print("Testcases file not found")
    if not "--create" in sys.argv:
        # prompt to create testcase file
        print("Problem and testcases file not found. Create one? [Y/n]")
    if ("--create" in sys.argv) or input().lower() == 'y':
        print("Fetching problem data...")
        testcase_file_content = ""
        testcase_file_content = "# Path: problems/" + problem_id + ".tc.md\n"
        problem_data = requests.get(
            "https://api-d3cwvqj26q-as.a.run.app/api/course/problem/" + problem_id, headers={"Authorization": "Bearer " + api_token})
        print("Fetching problem data...")
        if problem_data.status_code != 200:
            print("Problem not found")
        else:
            problem_data = problem_data.json()["data"][0]
            # write problem title
            testcase_file_content += "# " + \
                problem_data["problem_title"] + "\n"
            # write problem description
            testcase_file_content += problem_data["problem_description"] + "\n"
            # write problem input specification
            testcase_file_content += "## Input\n"
            testcase_file_content += problem_data["problem_input_specification"] + "\n"
            # write problem output specification
            testcase_file_content += "## Output\n"
            testcase_file_content += problem_data["problem_output_specification"] + "\n"
            # write problem sample input
            testcase_file_content += "## Testcases\n"
            testcase_data = requests.get(
                "https://api-d3cwvqj26q-as.a.run.app/api/course/problem/testcase/" + problem_id, headers={"Authorization": "Bearer " + api_token})
            if testcase_data.status_code != 200:
                print("Testcases from api not work")
                testcase_file_content += "##### 1\n"
                testcase_file_content += "```\n"
                testcase_file_content += "```\n"
                testcase_file_content += "----\n"
                testcase_file_content += "```\n"
                testcase_file_content += "```\n"
                print("Testcases file created")
            else:
                testcase_data = testcase_data.json()["data"]
                for i, tcd in enumerate(testcase_data):
                    testcase_file_content += "##### " + str(i+1) + "\n"
                    testcase_file_content += "```\n"
                    testcase_file_content += tcd["testcase_input"] + "\n"
                    testcase_file_content += "```\n"
                    testcase_file_content += "----\n"
                    testcase_file_content += "```\n"
                    testcase_file_content += tcd["testcase_output"] + "\n"
                    testcase_file_content += "```\n"
            if testcase_file_content == "":
                testcase_file_content = """# Path: problems/""" + problem_id + """.tc.md
# Your testcases here
##### 1
```
Input here
```
----
```
Output here
```
"""

        with open("problems/" + problem_id + ".tc.md", "w") as f:
            f.write(testcase_file_content)
            print("Testcases file created")


class c:
    RED = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'


os.system("clear")
print("Problem ID:", problem_id)
# get testcase from .tc2 file
testcase = ""
with open("problems/" + problem_id + ".tc.md", "r") as f:
    testcase = f.read().replace("```", "").replace('\n\n', '\n').split("##### ")
testcase = testcase[1:]

testcase = [[item2.strip() for item2 in item.strip().split('----')]
            for item in testcase]
testcase_dict = {key[0]: key[1] for key in testcase}
count = {
    "PASS": 0,
    "FAIL": 0,
    "ALL": len(testcase_dict)
}

options = {
    "show_input_output": False,
    "no_box": False,
    "show_got_only": False,
}

with open("problems/" + problem_id + ".py", "r") as f:
    lines = f.readlines()
    if len(lines) == 0:  # empty file
        print(c.RED+"[ERR] Empty file"+c.END)
        exit(0)
    if lines[0].startswith('#debug: '):
        fl = lines[0].replace('#debug: ', '').strip().split(' ')
        options = {item: item in fl for item in options}


def boxDrawer(content) -> str:
    if options["no_box"]:
        return "----\n" + "\n".join(content) + "\n----\n"
    border = {
        "TOP_LEFT": "┏",
        "TOP_RIGHT": "┓",
        "BOTTOM_LEFT": "┗",
        "BOTTOM_RIGHT": "┛",
        "HORIZONTAL": "━",
        "VERTICAL": "┃",
    }
    # get max length of content
    max_length = max([len(item) for item in content])
    # draw top border
    top_border = border["TOP_LEFT"] + \
        border["HORIZONTAL"] * (max_length + 2) + border["TOP_RIGHT"]
    # draw bottom border
    bottom_border = border["BOTTOM_LEFT"] + \
        border["HORIZONTAL"] * (max_length + 2) + border["BOTTOM_RIGHT"]
    # draw content
    content = [border["VERTICAL"] + " " + item.ljust(max_length) + " " +
               border["VERTICAL"] for item in content]
    # return result
    return "\n".join([top_border] + content + [bottom_border])


for key in testcase_dict:
    testcase_input = "\n".join(key.split('\n')[1:])
    result = subprocess.run(
        ["python", "problems/" + problem_id + ".py"], input=testcase_input, capture_output=True, text=True)
    testcase_expected = testcase_dict[key]
    if result.stderr:
        print(c.RED+"[ERR] Testcase #" + key.split()[0] + c.END)
        print(result.stderr.strip())
        continue
    if result.stdout.strip() != testcase_expected.strip():
        print(c.RED+"[FAIL] Testcase #" + key.split()[0] + c.END)
        count["FAIL"] += 1
        if not options["show_got_only"]:
            print("Input")
            print(boxDrawer(testcase_input.strip().split('\n')))
            print("Expected")
            print(boxDrawer(testcase_expected.strip().split('\n')))
        print("Got")
        print(boxDrawer(result.stdout.strip().split('\n')))
        continue
    print(c.GREEN+"[PASS] Testcase #" + key.split()[0] + c.END)
    if options['show_input_output']:
        if not options["show_got_only"]:
            print("Input")
            print(boxDrawer(testcase_input.strip().split('\n')))
            print("Expected")
            print(boxDrawer(testcase_expected.strip().split('\n')))
        print("Got")
        print(boxDrawer(result.stdout.strip().split('\n')))
    count["PASS"] += 1
print("Result:", count["PASS"], "/", count["ALL"])
