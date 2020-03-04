#!/usr/bin/env python3

import re
import os
from pathlib import Path

plans = Path('plans')
for plan in plans.iterdir():
    if plan.name.endswith('_.html'):
        path = str(plan)
        new_path = re.sub('_.html$', '.html', path)
        print(path, new_path)
        os.rename(path, new_path)
