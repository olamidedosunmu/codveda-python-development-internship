# API Integration

**Codveda Technologies — Python Development Internship**  
**Level 2 project**

## Overview

This Python program sends an HTTP GET request to the JSONPlaceholder sample API, retrieves user data in JSON format, and displays selected information for the first five users.

## Features

- Sends a GET request using the `requests` library.
- Checks the HTTP response status with `raise_for_status()`.
- Converts the JSON response into Python data.
- Displays each user's name, email address, and city.
- Handles timeouts, connection failures, unsuccessful HTTP responses, invalid JSON, and other request errors.

## API endpoint

`https://jsonplaceholder.typicode.com/users`

JSONPlaceholder is a public sample API intended for testing and learning. The returned user records are demonstration data.

## Requirements

- Python 3
- `requests` library

Install the dependency with:

```bash
pip install -r requirements.txt
```

## How to run

From this folder, run:

```bash
python api_integration.py
```

The program prints the HTTP status code and selected information for up to five users.

## Files

- `api_integration.py` — source code.
- `requirements.txt` — Python dependency list.
