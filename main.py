import requests

# Make a GET request to the API endpoint for 100 male users
response = requests.get("https://randomuser.me/api/?results=100&gender=male")

# Parse the response JSON data
data = response.json()

# Extract the user data from the response
users = data['results']

# Filter the male users
male_users = [user for user in users if user['gender'] == 'male']

# Print the top 100 male users
for i, user in enumerate(male_users[:100]):
    print(f"{i+1}. {user['name']['first']} {user['name']['last']} ({user['email']})")




