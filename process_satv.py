""" This is not a very good script, I had to manually find-and-replace a bunch of special characters"""
import csv

with open("dictionaryv.txt", "a") as f:
    with open('vocabs.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter="|")
        for row in reader:
            if len(row) > 0:
                (index, word, definition, grouping) = row
                word = word.lower().replace(" ", "_").replace("-", "_")
                definition = f"({grouping}) {definition}".replace('"', "'")
                f.write(f'{word}="{definition}",\n')
