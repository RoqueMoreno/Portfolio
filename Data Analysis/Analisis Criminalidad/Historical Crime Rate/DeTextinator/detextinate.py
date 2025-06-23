import re
myFile = "2019.txt"
endText = ''
with open(myFile, encoding= "utf-8") as f:
    line = f.readline()
    i = 1
    while line != "":
        importantLines = {3,4,6,7,9,10,12,13,15,16,18,19,21,22,23,24,25,27,28,29,31,33,35,36,38,39,40,41,42,43,44,45,46,47}
        if i in importantLines:
            myResult = re.findall(r'\d+', line.replace(',', ''))

            endText = endText + ('\t'.join(myResult)) + '\n'

        line = f.readline()
        i+=1
print(endText)

with open(myFile, "w", encoding = "utf-8") as f:
    f.write(endText)

