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