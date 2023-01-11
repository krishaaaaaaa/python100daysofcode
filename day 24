with open('./input/letter/letter.txt' ) as file:
    con = file.read()

with open('./input/name/names.txt') as f:
    n = f.read()
    li = list(n.split("\n"))

for a in range(len(li)):
    with open(f'./output/ready to send/{li[a]}', mode='x') as ab:
       ab.write(f"{con.replace('[name]', li[a])}\n\n")
       
       
#names.txt
Aang
Zuko
Appa
Katara
Sokka
Momo
Uncle Iroh
Toph



#letter.txt
Dear [name],
You are invited to my birthday this Saturday.
Hope you can make it!
Krisha
