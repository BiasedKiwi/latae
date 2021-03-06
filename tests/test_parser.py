from latae import *


def test_get_disallowed_single_agent():
    """Test the `get_disallowed()` method on a single user agent."""
    with open("./tests/samples/robots_one_agent.txt") as f:
        robots = f.readlines()
        
    assert get_disallowed(robots) == {"*": ["/"]}
    
def test_get_disallowed_multiple_agents():
    with open("./tests/samples/robots_multiple_agents.txt", "r") as f:
        robots = f.readlines()
        
    assert get_disallowed(robots) == {"Test": ["/"], "*": ["foo"]}
    
def test_get_disallowed_multiple_agents_comments():
    with open("./tests/samples/robots_multiple_agents_comments.txt", "r") as f:
        robots = f.readlines()
        
    assert get_disallowed(robots) == {"Test": ["/"], "*": ["foo"]}
    
    
def test_get_disallowed_no_directive():
    with open("./tests/samples/robots_no_directive.txt", "r") as f:
        robots = f.readlines()
        
    assert get_disallowed(robots) == {}
    
def test_trim_comments():
    with open("./tests/samples/robots_comments.txt", "r") as f:
        robots = f.readlines()
        
    assert _trim_comments(robots) == ["User-Agent: *", "Disallow: /"]
    
def test_get_crawl_delay():
    with open("./tests/samples/robots_crawl_delay.txt", "r") as f:
        robots = f.readlines()
        
    assert get_crawl_delay(robots) == 5
    

def test_get_crawl_delay_no_directive():
    with open("./tests/samples/robots_no_directive.txt") as f:
        robots = f.readlines()
        
    assert get_crawl_delay(robots) == 0
    
def test_get_sitemap():
    with open("./tests/samples/robots_sitemap.txt", "r") as f:
        robots = f.readlines()
        
    assert get_sitemap(robots) == ["https://example.com/sitemap.xml"]
    
def test_get_sitemap_multiple():
    with open("./tests/samples/robots_sitemap_multiple.txt", "r") as f:
        robots = f.readlines()

    assert get_sitemap(robots) == ["https://foo.com/sitemap.xml", "https://bar.com/sitemap.xml"]
    

def test_get_sitemap_no_directive():
    with open("./tests/samples/robots_sitemap_no_directive.txt", "r") as f:
        robots = f.readlines()
        
    assert get_sitemap(robots) == []


def test_get_host_normal_case():
    with open("./tests/samples/robots_host.txt", "r") as f:
        robots = f.readlines()

    assert get_host(robots) == "example.com"
    

def test_get_host_no_case():
    with open("./tests/samples/robots_host_case_insensitive.txt", "r") as f:
        robots = f.readlines()
        
    assert get_host(robots) == "example.com"
    
    
def test_get_host_no_directive():
    with open("./tests/samples/robots_host_no_directive.txt", "r") as f:
        robots = f.readlines()
        
    assert get_host(robots) == ""
