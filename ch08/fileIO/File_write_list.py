
f = open("c:/pyfile/2021kbo.txt", "w")
team = ['KIA Tigers', "Samsung Lions", "LG Twins", "NC Dinos", "SSG Landers", "Hanwha Eagles", "Lotte Giants"]

'''
for i in team:
    f.write(i + ", ")
f.close()
'''

n = len(team)
for i in range(n):
    f.write(team[i] + "\n")

f.close()

f = open("c:/pyfile/2021kbo.txt", 'r')
data = f.read()
print(data)
f.close()