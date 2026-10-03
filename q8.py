text = "programming"
freq={}
for ch in text:
    freq.setdefault(ch,0)
    freq[ch] += 1
print(freq)

from collections import defaultdict
freq = defaultdict(int)
for ch in text:
    freq[ch] += 1
print(freq)

