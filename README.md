# JSON Verification Program

This `json_verify` program is used to verify JSON data according to specified conditions. The program checks whether the `"Resource"` fields in an AWS IAM policy (`"Statement"`) meet specific security criteria. 
Specifically, it verifies that no single asterisk `"*"` is used as the sole Resource, helping prevent overly permissive policies.

## Requirements
- Python 3.x
- No external libraries required (uses built-in `json` module).

## Installation

1. Download the `json_verify.py` file to your local environment.
2. Make sure you have a Python interpreter installed.
3. You can use the program in your environment via command line or by incorporating it into your Python code.

## Usage

There are sample json files included in the repository. To use the `json_verify` function, follow these steps:

1. Open a command prompt or a python interpreter.
2. Change `json_file_path` inside the script to point to your JSON file, or leave it as it is to run the defaults.
3. Run the program:

```bash
python json_verify.py
```

### Expected Output:
- The script will return `True` if the resource fields are safe (they do not contain a single `"*"`).
- The script will return `False` if it detects an overly permissive `"*"` resource.
