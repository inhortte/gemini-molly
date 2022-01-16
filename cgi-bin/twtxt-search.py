#!/usr/bin/python3

from pathlib import Path
from urllib import request
import os
if('QUERY_STRING' in os.environ) and len(os.environ['QUERY_STRING']) > 0:
    query_string = os.environ['QUERY_STRING']
    req = request.Request(f'https://flavigula.net/twtxt-search?q={query_string}')
    res = request.urlopen(req)
    prefix = res.read().decode()
    if(len(prefix) > 0):
        print(f'30 gemini://thurk.org/twtxt/tw1-{prefix}.gmi\r\n')
    else:
        print(f'30 gemini://thurk.org/twtxt/tw1.gmi\r\n')
else:
    print("10 For what do you search?\r\n")
