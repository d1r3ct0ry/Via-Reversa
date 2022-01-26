import csv

f = open('base_cep.txt','r')
g = open('base_cepout.csv','a')
h = open('ceps.csv', newline='', encoding="ISO-8859-1")
d = {}


with h as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        bairro = row[2]
        a, b = row[-2:]
        d[(int(a), int(b))] = bairro 


for i in f:
    for (a, b), bairro in d.items():
        if a <= int(i) <= b:
            g.write(i[:-1]+ "," +bairro +"," +str(a) +"," +str(b) + '\n')
            break
    else:
        g.write(i)

