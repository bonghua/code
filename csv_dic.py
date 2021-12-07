import csv
with open('./score2.csv','r',newline='',encoding='utf-8') as file:
    dicreader=csv.DictReader(file)
    fieldname=dicreader.fieldnames
    print(fieldname)
    count=0
    for i in dicreader:
        count+=1
        with open(f'{count}.csv',mode='w',newline='',encoding='utf-8') as file2:
            dicwriter=csv.DictWriter(file2,fieldnames=fieldname)
            dicwriter.writeheader()
            dicwriter.writerow(i)
            
        