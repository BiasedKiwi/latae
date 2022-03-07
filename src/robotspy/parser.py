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
