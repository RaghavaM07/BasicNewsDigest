import Aljazeera
import BBC
import IndiaToday
import TheHindu
import colorama
from colorama import Fore, Style

print("="*50)
print("Today's news digest:")
print("="*50)

colorama.init(autoreset=True)

print(f"\n\nFrom {Style.BRIGHT}{Fore.RED}The Hindu{Fore.RESET}{Style.RESET_ALL}:")
TheHindu.GetHeadlines()

print(f"\n\nFrom {Style.BRIGHT}{Fore.RED}India Today{Fore.RESET}{Style.RESET_ALL}:")
IndiaToday.GetHeadlines()

print(f"\n\nFrom {Style.BRIGHT}{Fore.RED}BBC{Fore.RESET}{Style.RESET_ALL}:")
BBC.GetHeadlines()

print(f"\n\nFrom {Style.BRIGHT}{Fore.RED}Aljazeera{Fore.RESET}{Style.RESET_ALL}:")
Aljazeera.GetHeadlines()
