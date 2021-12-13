from bs4 import BeautifulSoup
import os, openpyxl
from datetime import datetime


time = datetime.now().strftime("%Y.%m.%d %H_%M_%S")
dirrr = os.path.abspath(os.curdir)
print(time)

def parser():
    # Создание файла xlsx
    filename = f"{dirrr}/TV {time}.xlsx"
    wb = openpyxl.Workbook()
    wb.save(filename)
    wb.close()

    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    ws.cell(column=1, row=ws.max_row, value='Ссылка')
    ws.cell(column=2, row=ws.max_row, value='Название товара')
    ws.cell(column=3, row=ws.max_row, value='Цена')

# ============= Збор данных через СУП с файла html =================
   
    for s in range(2, 5):  #Если много страниц ранжировать 
        try:
           
            with open(f"C:\\Users\\[YOU_NAME_PC]\\Downloads\\Телевизоры в Украине. Сравнить цены и купить телевизоры на Prom.ua, стр. {s}.html", encoding="UTF-8-sig") as file:
                soup = BeautifulSoup(file.read(), "lxml")

            get_http_info = soup.find('div', class_='[ENTER_YOU_CLASS]')  #soup.find_all("div", class_ ="ek-body__section") #указать тег div если проблема 

            with open(f'C:\\Users\\[YOU_NAME_PC]\\Downloads\\price_url_list.txt', 'a', encoding='utf-8') as file:

                for i in get_http_info:
                    # text = i.find('a').get(text) #_3h93n _21mbo NeaHz x85B7  # i.text.replace('\n', '') 
                    # link = i.find('a').get('href')
                    price = i.find('a').get(text)
                    text = i.text.replace('\n', '')
                    link = i.find('a').get('href')
                    print(i.find('_1KcTA _1kpcW _3WUeh qv3iA _3Kn0k _1sZ22').get('href'), (f"name= {text}"))
                    # print(i.find('a').get('href'), (f"name= {text}"))
                    # "link": HOST + item.find("a", class_="js-item-slider").get('href'),

                    file.write(f'{link} = {text} \n')  #f'{line}\n'

                    # Запись в XLSX
                    ws = wb.active
                    ws.cell(column=1, row=ws.max_row+1, value=link)
                    ws.cell(column=2, row=ws.max_row, value=text)
                    ws.cell(column=3, row=ws.max_row, value=price)
        except Exception as e:
            print(e)
        else:
            print("================ ВЖУХ  a(＾O ωO＾)a ﾞ(((((((((●～* ГОТОВО ================")


    wb.save(filename)
    wb.close()
    

if __name__ == '__main__':
    parser()
    
