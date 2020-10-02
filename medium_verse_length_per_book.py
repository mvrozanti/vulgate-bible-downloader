#!/usr/bin/env python
import json
import code
bible = json.load(open('bible.json'))
medium_verse_length_per_book = {}
for book,chapters in bible.items():
    verse_sum = 0
    verse_count = 0
    for chapter,verses in chapters.items():
        for verse in verses:
            verse_count += 1
            verse_sum += len(verse)
    medium_verse_length_per_book[book] = verse_sum/verse_count
for w in sorted(medium_verse_length_per_book, key=medium_verse_length_per_book.get, reverse=True):
    print(w, medium_verse_length_per_book[w])
code.interact(banner='', local=globals().update(locals()) or globals(), exitmsg='')
