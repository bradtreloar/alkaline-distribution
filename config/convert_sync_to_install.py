#!/usr/bin/python3

import os
import re
from ruamel.yaml import YAML

sync_dir = "sync"
install_dir = "install"

ignore_filename_patterns = [
    "\.htaccess",
    "README\.txt",

    # Do not use core.extension config as this configuration is created during
    # site installation.
    "core\.extension\.yml",

    # Do not use google_analytics.settings as this config contains secrets
    "google_analytics\.settings\.yml",

    # Do not use google_map_field.settings as this config contains secrets
    "google_map_field\.settings\.yml",

    # Ignore block configuration for any theme besides the alkaline base theme
    # and the core themes, Bartik and Seven.
    "block\.block\.(?!alkaline)(?!bartik)(?!seven)[a-z]+[^\.]+.yml",

    # Do not use update.settings config as this configuration is created during
    # site installation.
    "update\.settings\.yml",
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
