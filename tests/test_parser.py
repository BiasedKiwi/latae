from robotspy import *

with open("./tests/samples/robots_1.txt") as f:
    robots_1 = f.readlines()

def test_get_disallowed_single_agent():
    """Test the `get_disallowed()` method on a single user agent."""
    assert get_disallowed(robots_1) == {"*": ["/"]}