import urllib.parse
import json
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

# Accept user input for the GraphQL query in JSON format
graphql_json_str = input("Enter your GraphQL query in JSON format: ")

# Parse the user-provided JSON
try:
    graphql_json = json.loads(graphql_json_str)
except json.JSONDecodeError as e:
    print(Fore.RED + "Invalid JSON format:", str(e))
    exit(1)

# Convert the JSON to www-url-form-encoded format
encoded_query = urllib.parse.urlencode({
    "query": json.dumps(graphql_json["query"]),
    "operationName": graphql_json["operationName"],
    "variables": json.dumps(graphql_json["variables"])
})

# Colored output
print(Fore.GREEN + "URL-encoded query:")
print(Fore.CYAN + encoded_query)
print(Style.RESET_ALL)
