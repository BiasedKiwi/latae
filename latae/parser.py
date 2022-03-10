"""All methods related to parsing"""
from typing import Dict, List, TextIO


def get_disallowed(robots_file: TextIO) -> Dict[str, List[str]]:
    """
    Get all disallowed paths for a given robots.txt file

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
    robots_file = _trim_comments(robots_file)

    for line in robots_file:
        if line.startswith("User-Agent: "):
            current_agent = line.replace("User-Agent: ", "")
            disallows[current_agent] = []
        elif line.startswith("Disallow: "):
            disallows[current_agent].append(line.replace("Disallow: ", ""))
        else:
            continue

    return disallows


def get_sitemap(robots_file: TextIO) -> List[str]:
    """
    Get all the sitemap URLs specified in a given robots.txt file

    ## Returns

    Returns a list of all sitemap URls found in `robots_file`. Returns an empty list if no sitemap are found.

    ## Examples:
    >>> with open("robots.txt", "r") as f:
            # robots.txt contents: "Sitemap: https://example.com/sitemap.xml"
    ...     get_sitemap(f.readlines())  # Returns ["https://example.com/sitemap.xml"]

    ## Parameters:
    `robots_file` (TextIO): The contents of the robots.txt file to check.
    """
    robots_file = _trim_comments(robots_file)  # Trim comments
    sitemaps = []
    
    for line in robots_file:  # Iterate through the file to find the Sitemap rule
        if line.startswith("Sitemap: "):
            sitemaps.append(line.replace("Sitemap: ", ""))

    return sitemaps


def get_crawl_delay(robots_file: TextIO) -> int:
    """
    Returns the crawl delay if found, otherwise returns 0.

    ## Returns

    Returns the crawl delay if found, otherwise returns 0.

    ## Examples:
    >>> with open("robots.txt", "r") as f:
            # robots.txt contents: "crawl_delay: 5"
    ...     get_crawl_delay(f.readlines())  # Returns 5

    ## Parameters:
    `robots_file` (TextIO): The contents of the robots.txt file to check.
    """
    robots_file = _trim_comments(robots_file)  # Trim comments
    
    for line in robots_file:
        if line.startswith("Crawl-Delay: "):
            delay = line.replace("Crawl-Delay: ", "")
            return int(delay)

    return 0  # Returns 0 if the `Disallow` rule is not found


def _trim_comments(robots_file: TextIO) -> List[str]:
    """
    Internal method to trim comments from a robots.txt file using the `partiton()` method.
    
    ## Returns
    
    Returns a list of the lines in `robots_file` without comments.
    
    ## Examples:
    >>> with open("robots.txt", "r") as f:
            # robots.txt contents: "User-Agent: * # This is a comment"
            _trim_comments(f.readlines())  # Returns ["User-Agent: *"]
    
    
    ## Parameters:
    
    `robots_file` (TextIO): The contents of the robots.txt file to check.
    """
    trimmed_full = r""

    for line in robots_file:  # Iterate over all lines
        without_comments = line.partition("#")[0]  # Use the `partition` method to trim everything after the seperator, in this case `#`
        without_comments = without_comments.strip("\n")  # A little bit of a hack but works to suppress the empty strings "" items in `trimmed_full`
        trimmed_full += without_comments.rstrip() + "\n"  # Use `rstrip` to trim the whitespace at the end of the string.

    return trimmed_full.splitlines()
