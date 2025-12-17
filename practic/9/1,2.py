import re

text = """
Это простой текст. Это текст для примера.
Текст нужен, чтобы построить частотный словарь.
"""

words = re.findall(r"[а-яА-Яa-zA-Z]+", text.lower())

freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

top10 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]

for word, count in top10:
    print(word, count)