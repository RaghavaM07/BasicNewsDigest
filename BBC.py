from bs4 import BeautifulSoup
from requests import get
import colorama
from colorama import Fore, Style

URL='https://www.bbc.com/news/world'


def GetHeadlines():
    src = get(URL).content

    soup = BeautifulSoup(src, 'lxml')

    a = soup.find_all('a', {"class" : "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"})

    colorama.init(autoreset=True)
    
    l = []
    for b in a:
        txt = b.h3.string.strip().replace('‘', '\'').replace('’', '\'')
        link = b.attrs['href']
        if 'bbc.com' not in link:
            link = 'https://www.bbc.com'+link
        if txt not in l:
            l.append(txt)
            print(f"{Fore.GREEN}{Style.BRIGHT}{txt}{Style.RESET_ALL}\n{Fore.RESET}({Fore.CYAN}{link}{Fore.RESET})\n")
    
    print("="*25)


if __name__=='__main__':
    GetHeadlines()
