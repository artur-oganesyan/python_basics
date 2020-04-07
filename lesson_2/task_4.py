words = input('Enter a few words: ')
for n, w in enumerate(words.split(), 1):
    print(f'{n}. {w if len(w) <= 10 else w[:10]}')
