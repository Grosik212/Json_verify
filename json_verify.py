import unittest
import json


def json_verify(json_file):
    try:
        with open(json_file, "r") as f:
            data = json.load(f)
            statements = data.get("PolicyDocument", {}).get("Statement", [])

            if not statements:
                print("No 'Statement' found in the JSON data")
                return False

            for statement in statements:
                resource = statement.get("Resource")

                if resource is None:
                    print(f"Invalid JSON file: 'Resource' field is missing in a statement")
                    print(f"Statement: {statement}")
                    return False

                stripped_resource = resource.strip()
                if stripped_resource == '*':
                    print("Invalid JSON file: 'Resource' field contains only '*'")
                    print(f"Resource: {resource}")
                    return False

            return True

    except json.JSONDecodeError as e:
        print(f"Invalid JSON file: {e}")
        return False
    except FileNotFoundError:
        print(f"File not found: {json_file}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


class TestJsonVerify(unittest.TestCase):

    def test_valid_json(self):
        json_file_path = 'test.json'
        self.assertTrue(json_verify(json_file_path))

    def test_missing_resource_field(self):
        json_file_path = 'missing_resource.json'
        self.assertFalse(json_verify(json_file_path))

    def test_resource_contains_only_star(self):
        json_file_path = 'resource_star.json'
        self.assertFalse(json_verify(json_file_path))

    def test_invalid_json_file(self):
        json_file_path = 'non_existing_file.json'
        self.assertFalse(json_verify(json_file_path))

    def test_invalid_json_format(self):
        json_file_path = 'invalid_json_format.json'
        self.assertFalse(json_verify(json_file_path))


if __name__ == '__main__':
    unittest.main()
