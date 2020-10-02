#!/usr/bin/env python
import sys
import json
import code
bible = json.load(open('bible.json'))
for book,chapters in bible.items():
    for chapter,verses in chapters.items():
        for verse_ix,verse in enumerate(verses):
            if sys.argv[1] in verse:
                print(f'{book} {chapter},{verse_ix}')
