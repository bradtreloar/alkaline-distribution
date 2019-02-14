#!/usr/bin/env python3

import os
import yaml

if "install" not in os.listdir("."):
    os.mkdir("install")

for filename in os.listdir("install"):
    os.remove(os.path.join("install", filename))

for filename in os.listdir("sync"):
    ignore = [
        ".htaccess",
        "core.extension.yml",
        "update.settings.yml"
    ]

    if filename not in ignore:
        with open(os.path.join("sync", filename), "r") as stream:
            config = yaml.load(stream)

        if "_core" in config:
            del config["_core"]

        if "uuid" in config:
            del config["uuid"]

        with open(os.path.join("install", filename), "w") as stream:
            yaml.dump(config, stream)
