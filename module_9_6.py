def all_variants(text):
    stop = len(text)
    i = 1
    while i <= stop:
        yield text[i-1]
        i += 1
sim = all_variants('abc')

for i in sim:
    print(i)
