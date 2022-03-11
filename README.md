# Latae

> A pure Python library for parsing and reading robots.txt files

## 🛠 Note

Latae is currently in heavy development, expect bugs! More features are planned.

## 💻 Usage

Via a file on your local system...

```python
import latae as lt

with open("robots.txt", "r") as f:
  rb_file = f.readlines()

# Get disallowed paths in the form of a Dict
lt.get_disallowed(rb_file)

# Get the XML sitemap
lt.get_sitemap(rb_file)
```

...Or via the `requests` module

```python
import requests
import latae as lt

rb_file = requests.get("https://duckduckgo.com/robots.txt").text

# Get disallowed paths in the form of a Dict
lt.get_disallowed(rb_file.splitlines())

# Get the XML sitemap
lt.get_sitemap(rb_file.splitlines())
```
