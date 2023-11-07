import requests
api_token = ""
with open("api_token.txt", "r") as f:
    api_token = f.read()
testcase_data = requests.get(
    "https://api-d3cwvqj26q-as.a.run.app/api/course/problem/testcase/" + str(88), headers={"Authorization": "Bearer " + api_token}).json()["data"]
print(testcase_data)