from bs4 import BeautifulSoup
import requests
url = 'https://www.napanta.com/fertilizer-dealer/timalnadu/madurai/madurai-west'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = str(soup.findAll('td'))
# print('\n'.join(table.split(', ')))
a = '\n'.join(table.split(', '))
a = a[1:len(a)-1]
# print(a)
a = a.replace('<td class="td-style">', '')
# print(a)
a = a.replace('</td>','')
print(a)
b = [['serial no','name','location']]
a = a.split('\n')
l = [a[0]]
for i in range(1,len(a)):
    if a[i].isdigit() == True:
        b.append(l)
        l = []
        l.append(a[i])
    else:
        l.append(a[i])
return b