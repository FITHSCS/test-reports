import os
import json
import re

# Find all report directories
report_dirs = []
if os.path.exists('reports'):
    for item in os.listdir('reports'):
        if os.path.isdir(os.path.join('reports', item)) and os.path.exists(os.path.join('reports', item, 'test-summary.json')):
            report_dirs.append(item)

# Read the HTML file and inject the report directories
with open('index.html', 'r') as f:
    html_content = f.read()

# Replace the reportDirs array
report_dirs_js = json.dumps(report_dirs)
html_content = re.sub(
    r'const reportDirs = \[\]; // Will be populated by build script',
    f'const reportDirs = {report_dirs_js};',
    html_content
)

# Write back
with open('index.html', 'w') as f:
    f.write(html_content)

print(f"Updated dashboard with {len(report_dirs)} report directories")
