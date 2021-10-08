#!/usr/bin/env python

import sys
import importlib

assert sys.version_info.major == 3, "not using Python 3"

import_targets = [
    "numpy",
    "matplotlib",
    "sklearn",
    "pandas",
    "seaborn",
    "tensorflow.keras",
]

for name in import_targets:
    try:
        importlib.import_module(name)
        print(f"{name:20} ... ok")
    except Exception as ex:
        print(f"{name:20} ... FAIL: {ex}")
