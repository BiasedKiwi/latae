"""All methods related to parsing"""
from typing import Dict, List


def get_disallowed(robots_file: str) -> Dict[str, List[str]]:
    """
    Check if a user agent is allowed to access a website.
    
    ## Returns
    
    Returns a dictionnary containing all forbidden paths. Returns an empty tuple if the `Disallow` rule is not found or is set to `*`.
    
    ## Examples:
    >>> with open("robots.txt", "r") as f:
            # robots.txt contents: "User-Agent: *\n Disallow: /"
    ...     is_allowed("*", f.readlines())  # Returns {"*": ["/"]}
    
    ## Parameters:
    `robots_file` (str): The contents of the robots.txt file to check.
    """
    disallows = {}
    current_agent = ""
    
    for line in robots_file:
        if line.startswith("User-Agent: "):
            current_agent = line.replace("User-Agent: ", "").strip("\n")
            disallows[current_agent] = []
        elif line.startswith("Disallow: "):
            disallows[current_agent].append(line.replace("Disallow: ", "").strip("\n"))
        else:
            continue
    
    return disallows


def get_sitemap(robots_file: str) -> str:
    """
    Get the sitemap URL from a robots.txt file.
    
    ## Returns
    
    Returns the sitemap URL if found, otherwise returns an empty string.
    
    ## Examples:
    >>> with open("robots.txt", "r") as f:
            # robots.txt contents: "Sitemap: https://example.com/sitemap.xml"
    ...     get_sitemap(f.readlines())  # Returns "https://example.com/sitemap.xml"
    
    ## Parameters:
    `robots_file` (str): The contents of the robots.txt file to check.
    """
    for line in robots_file:
        if line.startswith("Sitemap: "):
            return line.replace("Sitemap: ", "").strip("\n")
    
    return ""
