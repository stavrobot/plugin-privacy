#!/usr/bin/env -S uv run
# /// script
# dependencies = ["requests"]
# ///
#
# list_transactions — Privacy.com plugin
# Copyright 2026 Stavros Korokithakis
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# See the LICENSE file for the full license text.

import json
import sys
from pathlib import Path

import requests


KNOWN_PARAMS = {
    "account_token",
    "card_token",
    "result",
    "begin",
    "end",
    "page_size",
    "page",
}


def main() -> None:
    params = json.load(sys.stdin)

    unknown = set(params) - KNOWN_PARAMS
    if unknown:
        print(f"Unknown parameters: {', '.join(sorted(unknown))}", file=sys.stderr)
        sys.exit(1)

    config = json.loads(Path("../config.json").read_text())
    api_key = config["api_key"]

    response = requests.get(
        "https://api.privacy.com/v1/transactions",
        headers={"Authorization": f"api-key {api_key}"},
        # Only forward parameters that were explicitly provided; omitting a
        # parameter lets the API apply its own defaults rather than receiving
        # an empty value that might be treated differently.
        params={key: value for key, value in params.items()},
    )

    if not response.ok:
        print(f"{response.status_code} {response.text}", file=sys.stderr)
        sys.exit(1)

    sys.stdout.write(response.text)


main()
