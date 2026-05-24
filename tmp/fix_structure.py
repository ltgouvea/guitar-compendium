import os
import re

directories = ['content/compendium', 'content/teoria']

for directory in directories:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and file != 'index.md' and file != '_index.md':
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, 'index.md')
                
                # Get the filename without extension for the alias
                name = os.path.splitext(file)[0]
                
                # Read content
                with open(old_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                # Add alias to front matter
                # Assuming front matter starts and ends with ---
                if len(lines) > 0 and lines[0].strip() == '---':
                    # Find the closing ---
                    try:
                        closing_index = -1
                        for i in range(1, len(lines)):
                            if lines[i].strip() == '---':
                                closing_index = i
                                break
                        
                        if closing_index != -1:
                            # Construct the alias
                            # Relative to the section, it would be the filename
                            # But Hugo aliases are usually relative to baseURL or absolute
                            # Let's use the full path relative to the section
                            # e.g. /compendium/folder/file/
                            
                            # Calculate path relative to content/
                            rel_root = os.path.relpath(root, 'content')
                            alias_url = f"/{rel_root}/{name}/"
                            
                            # Check if aliases already exists
                            has_aliases = any('aliases:' in line for line in lines[:closing_index])
                            
                            if not has_aliases:
                                lines.insert(closing_index, f"aliases:\n  - {alias_url}\n")
                            else:
                                # This is more complex, but for now we assume no aliases
                                pass
                    except Exception as e:
                        print(f"Error processing {old_path}: {e}")
                
                # Write back to index.md
                with open(new_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                
                # Remove old file
                os.remove(old_path)
                print(f"Moved {old_path} -> {new_path} with alias {alias_url}")
