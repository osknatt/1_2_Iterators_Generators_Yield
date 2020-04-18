import hashlib

def hash(path):
    with open(path, encoding='utf-8') as f:
        for line in f.readlines():
            yield hashlib.md5(line.encode('utf-8'))

for h in hash('links.txt'):
    print(h)
