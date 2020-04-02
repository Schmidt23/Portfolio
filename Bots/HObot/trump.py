import json
import os
import re
"""just morphing a huge json file into text and removing twitter links """

filepath = f"ai\\trump.json"
out = f"ai\\trump.txt"
links_out = "(http[s]*://t.co/[\w]+)"

if not os.path.exists(out):
    with open(filepath, 'r', encoding="utf8") as f:
        for i in list(json.load(f)):
            with open(out, 'a', encoding="utf-8") as o:
                print(re.sub(links_out,"",i['text']+"\n"))
                o.write(re.sub(links_out,"",i['text']+"\n"))

