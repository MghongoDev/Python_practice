"""Map letters from string into dictionary and print bar chart of frequency"""

import sys
import pprint
from collections import defaultdict

# Note: text should be a short phrase for bars to fit in IDLE window
text = "The quick fox caught a groundhog yesterday" 

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

mapped = defaultdict(list)
for character in text:
    character = character.lower()
    if character in ALPHABET:
        mapped[character].append(character)

print("\nYou may need to stretch console window if text wrapping occurs.\n")
print("text = ", end="")
print("{}\n".format(text), file=sys.stderr)
pprint.pprint(mapped, width=110)
