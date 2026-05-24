import os
import re

content_dir = 'content'
static_dir = 'static'

broken_links = []

for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith('.md'):
            with open(os.path.join(root, file), 'r') as f:
                content = f.read()
                # Find download_link: '/pdfs/...'
                match = re.search(r"download_link:\s*'([^']+)'", content)
                if match:
                    link = match.group(1)
                    full_path = os.path.join(static_dir, link.lstrip('/'))
                    if not os.path.exists(full_path):
                        broken_links.append((os.path.join(root, file), link))

if broken_links:
    print("Found broken links:")
    for file, link in broken_links:
        print(f"{file}: {link}")
else:
    print("No broken download_links found.")
