import re


def get_disallowed(user_agent: str, robots_file: str) -> bool:
    """
    Check if a user agent is allowed to access a website.
    
    ## Returns
    
    Returns a tuple containing all forbidden paths. Returns an empty tuple if the `Disallow` rule is not found or is set to `*`.
    
    ## Examples:
    >>> with open("robots.txt", "r") as f:
            # robots.txt contents: "User-Agent: *\n Disallow: /"
    ...     is_allowed("*", f.readlines())
            ("/")
    
    ## Parameters:
    `user_agent` (str): The user agent to check.
    `robots_file` (str): The contents of the robots.txt file to check.
    """
    user_agent_regex = r"User-Agent: (.*)"
    disallow_regex = r"Disallow: (.*)"
    disallows = {}
    current_agent = ""
    
    for line in robots_file:
        if line.startswith("User-Agent: "):
            current_agent = line.replace("User-Agent: ", "").strip("\n")
            disallows[current_agent] = []
            for line in robots_file:
                if not line.startswith("User-Agent: "):
                    try:
                        print(disallows)
                        disallows[current_agent] = []
                        disallows[current_agent].append(re.search(disallow_regex, line).group(1))
                    except AttributeError:
                        pass
                else:
                    current_agent = line.replace("User-Agent: ", "").strip("\n")
        elif line.startswith("Disallow: "):
            disallows[current_agent].append(re.search(disallow_regex, line).group(1))


if __name__ == "__main__":
    with open("./robots.txt") as file:
        robots_file = file.readlines()
    print(get_disallowed("JoeBot", robots_file))
