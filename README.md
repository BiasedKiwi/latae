# Robots.py

> A pure Python library for parsing and reading robots.txt files

## 🛠 Note

Robots.py is currently in heavy development, expect bugs! More features are planned.

## 💻 Usage

```python
import robotspy as rp

with open("robots.txt", "r") as f:
  rb_file = f.readlines()

# Get disallowed paths in the form of a Dict
rp.get_disallowed(rb_file)

# Get the XML sitemap
rp.get_sitemap(rb_file)
```
