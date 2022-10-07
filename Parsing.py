from bs4 import BeautifulSoup
import requests


host = 'http://dict.ruslang.ru/'
URL = 'http://dict.ruslang.ru/freq.php?act=show&dic=freq_s&title'
reg = requests.get(URL)
soup = BeautifulSoup(reg.text, "html.parser")


def pars():
    lst = soup.find_all("td")
    filter_trash = [word.text for word in lst[8:len(lst):5]]

    return filter_trash
