import robotspy


def test_get_disallowed_single_agent():
    """Test the `get_disallowed()` method on a single user agent."""
    with open("./tests/samples/robots_one_agent.txt") as f:
        robots = f.readlines()
        
    assert robotspy.get_disallowed(robots) == {"*": ["/"]}
    
def test_get_disallowed_multiple_agents():
    with open("./tests/samples/robots_multiple_agents.txt", "r") as f:
        robots = f.readlines()
        
    assert robotspy.get_disallowed(robots) == {"Test": ["/"], "*": ["foo"]}
    
def test_get_disallowed_multiple_agents_comments():
    with open("./tests/samples/robots_multiple_agents_comments.txt", "r") as f:
        robots = f.readlines()
        
    assert robotspy.get_disallowed(robots) == {"Test": ["/"], "*": ["foo"]}
    
def test_trim_comments():
    with open("./tests/samples/robots_comments.txt", "r") as f:
        robots = f.readlines()
        
    assert robotspy._trim_comments(robots) == ["User-Agent: *", "Disallow: /"]
    
def test_get_crawl_delay():
    with open("./tests/samples/robots_crawl_delay.txt", "r") as f:
        robots = f.readlines()
        
    assert robotspy.get_crawl_delay(robots) == 5
    
def test_get_sitemap():
    with open("./tests/samples/robots_sitemap.txt", "r") as f:
        robots = f.readlines()
        
    assert robotspy.get_sitemap(robots) == ["https://example.com/sitemap.xml"]
    
def test_get_sitemap_multiple():
    with open("./tests/samples/robots_sitemap_multiple.txt", "r") as f:
        robots = f.readlines()

    assert robotspy.get_sitemap(robots) == ["https://foo.com/sitemap.xml", "https://bar.com/sitemap.xml"]
