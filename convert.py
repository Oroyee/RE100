import csv

l = []
m = {'M':6,'B':9,'T':12}

with open('revenue.txt',encoding="utf-8") as f:
  lines = csv.reader(f,delimiter='\t')
  for line in lines:
    new_string=line[0].strip('(')
    new_string_2=new_string.strip(')')
    print(new_string_2)
    for a in line:
        value = []
        multi = 1
        for i in a:
            if i == 'M':
                multi = 1000000
            elif i == "B":
                multi = 1000000000
            elif i == 'T':
                multi = 1000000000000
            else:
                value+=i
        number = ''.join(value)
        if len(number) != 0 :             
            anwser = float(number)*multi
        else:
            anwser = number
        print(anwser)
        with open(r'revenue_2.txt','a', encoding="utf-8")as fp:
            fp.write(str(anwser))
            fp.write('\t')
            fp.close()
    with open(r'revenue_2.txt','a', encoding="utf-8")as fp:
        fp.write('\n')