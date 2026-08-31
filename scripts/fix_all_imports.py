import os
import re

def fix_imports():
    src_dir = os.path.abspath("src")
    
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".ts") or file.endswith(".tsx"):
                file_path = os.path.join(root, file)
                rel_to_src = os.path.relpath(src_dir, root).replace("\\", "/")
                # if rel_to_src is '.', then relative prefix is '.'
                
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Replace '@/something' with relative path
                def repl(match):
                    target = match.group(1)
                    if rel_to_src == ".":
                        return f"from './{target}'"
                    else:
                        return f"from '{rel_to_src}/{target}'"
                
                new_content = re.sub(r"from\s+['\"]@/([^'\"]+)['\"]", repl, content)
                
                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Fixed imports in: {os.path.relpath(file_path, src_dir)}")

fix_imports()