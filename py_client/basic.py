import requests
# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/"

get_response = requests.get(endpoint, json={"query":
"Hello World"})  # HTTP Request
print(get_response.text)  # Print raw text response


# print(get_response.json()) 
print(get_response.status_code) 