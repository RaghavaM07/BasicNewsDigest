from bs4 import BeautifulSoup
from requests import get
import colorama
from colorama import Fore, Style

URL='https://www.aljazeera.com/'


def GetHeadlines():
    src = get(URL).content

    soup = BeautifulSoup(src, 'lxml')

    a = soup.find_all('a', {"class" : "article-trending__title-link"})

    colorama.init(autoreset=True)

    for b in a:
        txt = b.span.string.strip().replace('‘', '\'').replace('’', '\'')
        link = b.attrs['href']
        if 'aljazeera.com' not in link:
            link = 'https://www.aljazeera.com'+link
        print(f"{Fore.GREEN}{Style.BRIGHT}{txt}{Style.RESET_ALL}\n{Fore.RESET}({Fore.CYAN}{link}{Fore.RESET})\n")
    
    print("="*25)


if __name__=='__main__':
    GetHeadlines()