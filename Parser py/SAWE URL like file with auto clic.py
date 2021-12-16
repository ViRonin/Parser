from bs4 import BeautifulSoup

# ============= Збор данных через з СУП с файла =================

for i in range(2, 800):

    with open("C:\\Users\\[YOU_NAME_PC]\\Downloads\\2.html", encoding="UTF-8-sig") as file:
    
        src = file.read(0)

    soup = BeautifulSoup(src, "lxml")
    get_http_info = soup.find_all(class_="post-title entry-title") #указать тег div если берет первый тег

    for item in get_http_info:
        item_text = item.text
        item_herf = item.get("href")
        print(item_text)

    # for link in soup.find_all('a'):   # Виводить ссилку
    #     item_href = link.get('href')
    #     print(f'{item_href}')


    


