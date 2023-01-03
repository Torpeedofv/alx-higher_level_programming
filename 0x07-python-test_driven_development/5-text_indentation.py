#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    sentences = text.split(". ")
    sentences = [s + ". " for s in sentences[:-1]] + sentences[-1:]

    for s in sentences:
        print(s.strip())
        if s[-1] in (":", "?", "."):
            print("\n")
            print()
