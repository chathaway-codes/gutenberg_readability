import re

RE_START = re.compile(r"\*\*\* START OF THIS PROJECT GUTENBERG .*?\*\*\*")
RE_END = re.compile(r"\*\*\* END OF THIS PROJECT GUTENBERG .*?\*\*\*")
RE_CONTENTS = re.compile(r"\nC(?:ontents)|(?:ONTENTS)[\n\.]")


def sanitize(book):
    bstart = RE_START.search(book)
    bend = RE_END.search(book)
    bcontents = RE_CONTENTS.search(book)

    out = ""
    start = 0
    end = len(book) - 1
    if bcontents:
        start = bcontents.end()
    elif bstart:
        start = bstart.end()

    if bend:
        end = bend.start()

    out = book[start:end]
    out = out.replace("\r\n", " ")
    return out
