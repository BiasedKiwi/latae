"""All methods related to parsing"""

import re
from typing import Dict, List, TextIO, Union


__agt_replace_pattern = re.compile("user-agent: ", re.IGNORECASE)
__dslw_replace_pattern = re.compile("disallow: ", re.IGNORECASE)
__crawl_delay_pattern = re.compile("crawl-delay: ", re.IGNORECASE)
__stmp_replace_pattern = re.compile("sitemap: ", re.IGNORECASE)
__host_replace_pattern = re.compile("host: ", re.IGNORECASE)


def get_disallowed(robots_file: Union[TextIO, str]) -> Dict[str, List[str]]:
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
        if line.lower().startswith("user-agent: "):
            current_agent = __agt_replace_pattern.sub("", line)
            disallows[current_agent] = []
        elif line.lower().startswith("disallow: "):
            disallows[current_agent].append(__dslw_replace_pattern.sub("", line))
        else:
            continue

    return disallows


def get_sitemap(robots_file: Union[TextIO, str]) -> List[str]:
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
        if line.lower().startswith("sitemap: "):
            sitemaps.append(__stmp_replace_pattern.sub("", line))

    return sitemaps


def get_crawl_delay(robots_file: Union[TextIO, str]) -> int:
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
        if line.lower().startswith("crawl-delay: "):
            delay = __crawl_delay_pattern.sub("", line)
            return int(delay)

    return 0  # Returns 0 if the `Disallow` rule is not found


def get_host(robots_file: Union[TextIO, str]) -> str:
    """
    Returns the value of the `Host` directive if found, otherwise returns an empty string "".
    
    ## Examples:
    >>> with open("robots.txt", "r") as f:
        # robots.txt contents: "Host: example.com"
    ... get_host(f.readlines())  # Returns "example.com"
    """
    robots_file = _trim_comments(robots_file)  # Trim comments
    
    for line in robots_file:
        if line.lower().startswith("host: "):
            host = __host_replace_pattern.sub("", line)
            return host
        
    return ""


def _trim_comments(robots_file: Union[TextIO, str]) -> List[str]:
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
        without_comments = line.partition("#")[
            0
        ]  # Use the `partition` method to trim everything after the seperator, in this case `#`
        without_comments = without_comments.strip(
            "\n"
        )  # A little bit of a hack but works to suppress the empty strings "" items in `trimmed_full`
        trimmed_full += (
            without_comments.rstrip() + "\n"
        )  # Use `rstrip` to trim the whitespace at the end of the string.

    return trimmed_full.splitlines()
