import unittest

from func2llm.annotations import action

# Assuming your action decorator code is defined here or imported

@action(description="Test function", param_descriptions={"x": "An integer parameter", "y": "A string parameter"})
def test_func(x: int, y: str):
    return x, y

class TestActionDecorator(unittest.TestCase):
    def test_decorator_metadata(self):
        expected_metadata = {
            "type": "function",
            "function": {
                "name": "test_func",
                "description": "Test function",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "x": {"type": "integer", "description": "An integer parameter"},
                        "y": {"type": "string", "description": "A string parameter"}
                    },
                    "required": ["x", "y"]
                }
            }
        }
        
        self.assertTrue(hasattr(test_func, '_api_meta'))
        self.assertEqual(test_func._api_meta, expected_metadata)

if __name__ == '__main__':
    unittest.main()
