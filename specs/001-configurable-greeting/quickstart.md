# Quickstart: Configurable Greeting

This guide explains how to run and test the "Configurable Greeting" application.

## Prerequisites
- Python 3.12 or newer

## Running the Application

1.  Navigate to the project root.
2.  Run the application from the `src` directory:

    ```bash
    # Run with default greeting
    python -m configurable_greeting.main

    # Run with a custom name
    python -m configurable_greeting.main "Your Name"
    ```

## Running Tests

1.  Navigate to the project root.
2.  Run the tests using `unittest`:

    ```bash
    python -m unittest discover -s tests
    ```
