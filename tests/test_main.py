import unittest
import subprocess
import sys
from src.configurable_greeting.main import greet

class TestMain(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_cli_default(self):
        result = subprocess.run(
            [sys.executable, "src/configurable_greeting/main.py"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), "Hello, World!")
        self.assertEqual(result.returncode, 0)

    def test_cli_custom_name(self):
        result = subprocess.run(
            [sys.executable, "src/configurable_greeting/main.py", "Bob"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), "Hello, Bob!")
        self.assertEqual(result.returncode, 0)
