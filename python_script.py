import requests

# Replace with your Github username, repository name, and personal access token
username = "aryaparasharmrt"
repo = "temp1"
token = "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"

# Github API endpoint for listing issues
api_url = f"https://api.github.com/repos/{username}/{repo}/issues"

# Headers with the personal access token
headers = {
  "Authorization": f"Bearer {token}",
  "Accept": "application/vnd.github.v3+json"
}

# Make the API request
response = requests.get(api_url, headers=headers)

# Print the results
if response.status_code == 200:
     issues = response.json()
     for issue in issues:
       print(f"Issue #{issue[3]}: {issue['Write API']}")
else:
  print(f"Error: {response.status_code} - {response.text}")
      
