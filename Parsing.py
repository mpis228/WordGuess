from bs4 import BeautifulSoup
import requests


"""ля ну тут я вообще по красоте как же я сократил в два раза строчек тут думаю если ты захочешь добавить и скормить 
несколько сайтов, а не один. Смотря как устроено постарайся больше не выбирать сайты в которых ни одного класса даже нет 
 потому что немного не оптимизированый подход я считаю я нашел но и лучше пока не в силах придумать и так работает 
 ахуено"""


host = 'http://dict.ruslang.ru/'
URL = 'http://dict.ruslang.ru/freq.php?act=show&dic=freq_s&title'
reg = requests.get(URL)
soup = BeautifulSoup(reg.text, "html.parser")


def pars():
    lst = soup.find_all("td")
    filter_trash = [word.text for word in lst[8:len(lst):5]]

    return filter_trash
