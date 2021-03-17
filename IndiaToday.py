from bs4 import BeautifulSoup
from requests import get
import colorama
from colorama import Fore, Style

URL='https://www.indiatoday.in/top-stories'


def GetHeadlines():
    src = get(URL).content

    soup = BeautifulSoup(src, 'lxml')

    a = soup.find_all('div', {"class" : "catagory-listing"})

    colorama.init(autoreset=True)

    for b in a:
        txt = b.find('div', {"class":"detail"}).h2.string.strip().replace('‘', '\'').replace('’', '\'')
        link = b.find('div', {"class":"detail"}).h2.a.attrs['href']
        if 'indiatoday.in' not in link:
            link = 'https://www.indiatoday.in'+link
        print(f"{Fore.GREEN}{Style.BRIGHT}{txt}{Style.RESET_ALL}\n{Fore.RESET}({Fore.CYAN}{link}{Fore.RESET})\n")
    
    print("="*25)


if __name__=='__main__':
    GetHeadlines()
