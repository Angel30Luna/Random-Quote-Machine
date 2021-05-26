output = [[]]
quote = ''
author = ''

with open("quotes.txt", 'r') as f:
    lines = f.readlines()

for j in range(len(lines)):
    line = lines[j]

    if(line[0] == '\n'):
        continue

    if(line[0] == '-' and line[1] == '-'):
        i = 3
        while(i < (len(line) - 1) and line[i] != ',' and line[i] != '('):
            if(line[i] == '\'' or line[i] == '\"'):
                author += '\\' + line[i]
            else:
                author += line[i]
            i += 1
        output.append([quote, author])
        quote = ''
        author = ''
        
    else:
        i = 0
        while(i < (len(line) - 1)):
            if(line[i] == '\'' or line[i] == '\"'):
                quote += '\\' + line[i]
            else:
                quote += line[i]
            i += 1

out = 'const QUOTES = {\n\tquotes: ['

for i in range(len(output)):
    if(i != 0):
        out += '\'' + output[i][0] + '\', \n\t  '

out += '],\n\tauthors: ['

for i in range(len(output)):
    if(i != 0):
        out += '\'' + output[i][1] + '\', \n\t  '

out += ']\n}'

with open("parsedQuotes.json", 'w') as f:
    f.write(out)