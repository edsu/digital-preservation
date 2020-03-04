#!/usr/bin/env python3

from pathlib import Path
from bs4 import BeautifulSoup

plans = Path('site/plans')
for plan in plans.iterdir():
    if plan.name.endswith('_.html'): 
        continue
    doc = BeautifulSoup(plan.open(), 'lxml')
    html = doc.prettify()
    new_f = plans / plan.name.replace('.html', '_.html')
    new_f.open('w').write(html)
