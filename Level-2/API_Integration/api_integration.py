"""Codveda Level 2 - API Integration.

Sends an HTTP GET request to JSONPlaceholder, retrieves sample user records,
and displays selected fields while handling common request and response errors.
"""

import requests


API_URL = "https://jsonplaceholder.typicode.com/users"
USER_LIMIT = 5


def fetch_users():
    """Fetch user records from the API and display selected information."""
    try:
        print("Connecting to API...")

        response = requests.get(API_URL, timeout=10)
        print("Status Code:", response.status_code)

        # Raise an exception for unsuccessful HTTP responses (4xx or 5xx).
        response.raise_for_status()

        users = response.json()

        if not isinstance(users, list):
            print("Error: Unexpected API response format.")
            return

        print("\nUSER INFORMATION")
        print("========================")

        for user in users[:USER_LIMIT]:
            address = user.get("address", {})
            city = address.get("city", "Not available")

            print("Name:", user.get("name", "Not available"))
            print("Email:", user.get("email", "Not available"))
            print("City:", city)
            print("------------------------")

        print("Data retrieved successfully!")

    except requests.exceptions.Timeout:
        print("Error: The API request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect. Check your internet connection.")

    except requests.exceptions.HTTPError as error:
        print("HTTP Error:", error)

    except ValueError:
        print("Error: The API returned invalid JSON data.")

    except requests.exceptions.RequestException as error:
        print("Request Error:", error)


if __name__ == "__main__":
    fetch_users()
