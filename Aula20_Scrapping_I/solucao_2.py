url = 'https://www.amazon.com.br/s?k=data+science&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2'pagina = requests.get(url)
soup_2 = BeautifulSoup(pagina.content, 'html.parser')
table = soup_2.select('.a-color-base.a-text-normal')
for i in table:
    print(i.text)