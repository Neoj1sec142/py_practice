# Finished Shorted Word 7 kyu

def find_short(s):
    l = 15
    for x in s.split(' '):
        if len(x)<l:
            l = len(x)
    return l # l: shortest word length