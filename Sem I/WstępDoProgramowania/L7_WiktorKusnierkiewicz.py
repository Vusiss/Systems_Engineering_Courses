# Zadanie 1

import re

def zamien_markdown_na_html(txt):
    txt = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', txt)
    txt = re.sub(r'# (.*?)\n', r'<h1>\1</h1>\n', txt)
    txt = re.sub(r'\!\[(.*?)\]\((.*?)\)', r'<img alt="\1" src="\2" />', txt)
    txt = re.sub(r'\!\[\s*\]\((.*?)\)', r'<img alt="obraz" src="\1" />', txt)
    return txt

plik = open('moj_markdown.txt', 'r') 
tekstWejsciowy = plik.read()

tekst_html = zamien_markdown_na_html(tekstWejsciowy)

plikWyjsciowy = open('moj_markdown.html', 'w')
plikWyjsciowy.write(f'<!DOCTYPE html>\n<html lang="pl">\n<head>\n<meta charset="UTF-8">\n<title>Mój markdown</title>\n</head>\n<body>\n{tekst_html}</body>\n</html>')

# Zadanie 2

import re

def remove_html_tags(html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', html)
    return cleantext

def remove_lines(text):
    lines = text.splitlines()  
    non_empty_lines = []
    for line in lines:
        stripped_line = line.strip()  
        if stripped_line:
            non_empty_lines.append(stripped_line)  

    result = '\n'.join(non_empty_lines)  
    return result


input_file = 'stronaWWW.html'
output_file = 'stronaWWW.txt'


input = open(input_file, 'r')
html_content = input.read()
text = remove_html_tags(html_content)

text_no_empty_lines = remove_lines(text)

output = open(output_file, 'w') 
output.write(text_no_empty_lines)