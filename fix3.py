with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove max-width: 600px;
content = content.replace('max-width: 600px; ', '')
content = content.replace('max-width: 600px;', '')

# Change 30y.png to 30RAA_white_PNG.png
content = content.replace('img/30y.png', 'img/30RAA_white_PNG.png')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")
