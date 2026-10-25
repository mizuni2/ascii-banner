
import os
import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)
os.system("title ASCII Banner Generator")

colors = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "blue": Fore.BLUE,
    "cyan": Fore.CYAN,
    "magenta": Fore.MAGENTA,
    "yellow": Fore.YELLOW,
    "white": Fore.WHITE,
}

print(Fore.CYAN + "=" * 40)
print(Fore.MAGENTA + "       ASCII BANNER GENERATOR")
print(Fore.CYAN + "=" * 40)

while True:
    text = input(Fore.WHITE + "\nEnter text (or 'exit' to quit): ")

    if text.lower() == "exit":
        break

    if not text.strip():
        continue

    print(Fore.YELLOW + "\nAvailable colors: " + ", ".join(colors))

    color_name = input(Fore.WHITE + "Choose a color: ").lower().strip()
    color = colors.get(color_name, Fore.GREEN)

    try:
        banner = pyfiglet.figlet_format(text, font="standard")
        print()
        print(color + banner + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

input(Fore.CYAN + "\nPress Enter to close...")
