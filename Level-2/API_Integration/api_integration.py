"""Codveda Level 2 - API Integration.

Sends an HTTP GET request to JSONPlaceholder, retrieves sample user records,
and displays selected fields while handling common request and response errors.
"""

# Import the requests library so Python can communicate with websites and APIs.
import requests


# This is the API endpoint (web address) that provides sample user information.
API_URL = "https://jsonplaceholder.typicode.com/users"

# We will display only the first five users returned by the API.
USER_LIMIT = 5


def fetch_users():
    """Fetch user records from the API and display selected information."""

    # The try block lets us handle problems without letting the program stop unexpectedly.
    try:
        print("Connecting to API...")

        # Send a GET request to the API.
        # timeout=10 means Python will wait up to 10 seconds for a response.
        response = requests.get(API_URL, timeout=10)

        # Display the HTTP status code returned by the server.
        # A status code of 200 means the request was successful.
        print("Status Code:", response.status_code)

        # Raise an HTTPError if the server returns an unsuccessful status (such as 404 or 500).
        response.raise_for_status()

        # Convert the JSON response from the API into Python data.
        # The returned user records are stored in a Python list of dictionaries.
        users = response.json()

        # Check that the API returned a list before trying to loop through it.
        if not isinstance(users, list):
            print("Error: Unexpected API response format.")
            return  # Stop this function because the response is not in the expected format.

        print("\nUSER INFORMATION")
        print("========================")

        # Loop through and display only the first five users in the returned list.
        for user in users[:USER_LIMIT]:

            # Each user is a dictionary. The address value is another dictionary.
            # get() safely retrieves a value and supplies a fallback if the key is missing.
            address = user.get("address", {})

            # Retrieve the city from the address dictionary.
            city = address.get("city", "Not available")

            # Display the user's name and email address.
            print("Name:", user.get("name", "Not available"))
            print("Email:", user.get("email", "Not available"))

            # Display the city retrieved from the nested address dictionary.
            print("City:", city)
            print("------------------------")

        # This message appears after the user records have been displayed successfully.
        print("Data retrieved successfully!")

    # Handle a request that takes longer than the 10-second timeout.
    except requests.exceptions.Timeout:
        print("Error: The API request timed out.")

    # Handle a failure to connect to the API, for example when the internet is unavailable.
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect. Check your internet connection.")

    # Handle unsuccessful HTTP responses such as 404 (not found) or 500 (server error).
    except requests.exceptions.HTTPError as error:
        print("HTTP Error:", error)

    # Handle a response that cannot be decoded as valid JSON.
    except ValueError:
        print("Error: The API returned invalid JSON data.")

    # Catch other request-related errors that were not handled above.
    except requests.exceptions.RequestException as error:
        print("Request Error:", error)


# This condition makes the function run when this file is executed directly.
# It prevents fetch_users() from running automatically if this file is imported elsewhere.
if __name__ == "__main__":
    fetch_users()
