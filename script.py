import os, json

data = []
files = os.listdir('.')
whitelist = ['.png', '.jpg', '.jpeg']

for file in files:
    if any(file.endswith(ext) for ext in whitelist):
        data.append(file)

with open('data.json', 'w', encoding='utf8') as f:
    json.dump({'data': data}, f, ensure_ascii=False)
