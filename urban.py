#!/usr/bin/env python3

# Copyright (c) 2013-2019 Juan Francisco Cantero Hurtado <iam@juanfra.info>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import urllib.request
import urllib.parse
import json
import sys
from shutil import get_terminal_size

if len(sys.argv) == 1:
    sys.exit(1)

arguments = urllib.parse.quote(" ".join(sys.argv[1:]))
urban_url = "http://api.urbandictionary.com/v0/define?term=" + arguments
urban_data = urllib.request.urlopen(urban_url).read().decode("utf8")
urban_dict = json.loads(urban_data)["list"]

term_blue = "\033[94m"
term_green = "\033[92m"
term_black = "\033[0m"

for i in urban_dict:
    print(("> " + i["word"] + " <").center((get_terminal_size()[0]), "="))
    print(term_blue + "Definition:" + term_black, i["definition"], "\n")
    if i["example"] != None:
        print(term_green + "Example:" + term_black, i["example"])
    print()
