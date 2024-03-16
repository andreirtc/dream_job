import pyfiglet
from pyfiglet import Figlet
import colorama
from colorama import Fore, Back, Style
colorama.init()

name = input("Enter your name: ")
dream_job = input("Enter your dream job: ")
figlet = Figlet(font='3d-ascii')

result = (f"{dream_job} is an amazing job, {name}!")
print(f"\n{Fore.CYAN}{Style.BRIGHT}{figlet.renderText(result)}")

