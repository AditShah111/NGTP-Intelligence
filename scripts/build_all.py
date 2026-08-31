#!/usr/bin/env python3
import os, json
base = os.getcwd()

def write_file(rel_path, content):
    p = os.path.join(base, rel_path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Wrote:', rel_path)
