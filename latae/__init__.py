"""A simple library to parse and read robots.txt files"""
__all__ = []

import pkgutil
import inspect

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)

    for fname, value in inspect.getmembers(module, inspect.isfunction):
        if fname.startswith('__'):
            continue

        if value.__module__ != module.__name__:
            continue

        globals()[fname] = value
        __all__.append(fname)
