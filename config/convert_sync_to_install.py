#!/usr/bin/python3

import os
import re
from ruamel.yaml import YAML

sync_dir = "sync"
install_dir = "install"

ignore_filename_patterns = [
    "\.htaccess",
    "core\.extension\.yml",
    "update\.settings\.yml",
    "block\.block\.(?!alkaline)(?!seven)[a-z]+[^\.]+.yml",
    "README\.txt",
]

if "install" not in os.listdir("."):
    os.mkdir("install")

for filename in os.listdir(install_dir):
    os.remove(os.path.join(install_dir, filename))

for filename in os.listdir(sync_dir):
    ignore = False
    for pattern in ignore_filename_patterns:
        if re.match(pattern, filename):
            ignore = True

    if ignore:
        continue

    with open(os.path.join(sync_dir, filename), "r") as stream:
        yaml = YAML()
        config = yaml.load(stream)

    if "_core" in config:
        del config["_core"]

    if "uuid" in config:
        del config["uuid"]

    with open(os.path.join(install_dir, filename), "w") as stream:
        yaml.dump(config, stream)
