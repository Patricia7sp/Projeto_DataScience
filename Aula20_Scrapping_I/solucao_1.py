f = open('exercicio01.html', 'r')
soup = BeautifulSoup(f, 'html.parser')
table = soup.find_all('table', id = '1')
rows = table[0].find_all('tr')
values = rows[2].find_all('td')
values[0].text