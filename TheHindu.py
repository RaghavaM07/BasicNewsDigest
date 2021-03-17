from requests import get
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style

URL = 'https://www.thehindu.com/todays-paper/tp-national/'


def GetHeadlines():
    src = get(URL).content

    soup = BeautifulSoup(src, 'lxml')

    l = soup.find('ul', {'class': 'archive-list'})
    n = l.find_all('li')

    colorama.init(autoreset=True)
    
    for item in n:
        hline = item.text.strip().replace('‘', '\'').replace('’', '\'')
        link = item.a.attrs['href']
        print(f"{Fore.GREEN}{Style.BRIGHT}{hline}{Style.RESET_ALL}\n{Fore.RESET}({Fore.CYAN}{link}{Fore.RESET})\n")
    
    print("="*25)


if __name__=='__main__':
    GetHeadlines()
