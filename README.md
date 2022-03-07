# Robots.py

> A pure Python library for parsing and reading robots.txt files

## 🛠 Note

Robots.py is currently in heavy development, expect bugs! More features are planned.

## 💻 Usage

Via a file on your local system...

```python
import robotspy as rp

with open("robots.txt", "r") as f:
  rb_file = f.readlines()

# Get disallowed paths in the form of a Dict
rp.get_disallowed(rb_file)

# Get the XML sitemap
rp.get_sitemap(rb_file)
```

...Or via the `requests` module

```python
import requests
import robotspy as rp

rb_file = requests.get("https://duckduckgo.com/robots.txt").text

# Get disallowed paths in the form of a Dict
rp.get_disallowed(rb_file)

# Get the XML sitemap
rp.get_sitemap(rb_file)
```
