import os
import json
import re

# Find all report directories
report_dirs = []
if os.path.exists('reports'):
    for item in os.listdir('reports'):
        if os.path.isdir(os.path.join('reports', item)) and os.path.exists(os.path.join('reports', item, 'test-summary.json')):
            report_dirs.append(item)

print(f"Found {len(report_dirs)} report directories")
for report_dir in report_dirs:
    print(f"  - {report_dir}")
