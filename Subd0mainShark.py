import requests
from requests import get
import os
os.system("clear")
print("\033[92m _____       _         _ _____                 _         _____ _                _    ")
print("\033[92m/  ___|     | |       | |  _  |               (_)       /  ___| |              | |   ")
print("\033[92m\ `--. _   _| |__   __| | |/' |_ __ ___   __ _ _ _ __   \ `--.| |__   __ _ _ __| | __")
print("\033[92m `--. \ | | | '_ \ / _` |  /| | '_ ` _ \ / _` | | '_ \   `--. \ '_ \ / _` | '__| |/ /")
print("\033[92m/\__/ / |_| | |_) | (_| \ |_/ / | | | | | (_| | | | | | /\__/ / | | | (_| | |  |   < ")
print("\033[92m\____/ \__,_|_.__/ \__,_|\___/|_| |_| |_|\__,_|_|_| |_| \____/|_| |_|\__,_|_|  |_|\_|")
print("\033[93m-------------------------------------------------------------------------------------")
print("")
print("            \033[38;5;197m～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●")
print("            \033[38;5;200m★★★   \033[1;93mAuthor    \033[1;97m−−\033[1;90m⋙⋙⋙ \033[1;93mEncrypted Noob !              \033[38;5;200m★★★")
print("            \033[38;5;200m★★★   \033[1;90mGithub    \033[1;97m−−\033[1;90m⋙⋙⋙ \033[1;90mgithub.com/encryptedn00b      \033[38;5;200m★★★")
print("            \033[38;5;200m★★★   \033[1;92mInstagram \033[1;97m−−\033[1;90m⋙⋙⋙ \033[1;92minstagram.com/encryptedn00b   \033[38;5;200m★★★")
print("            \033[38;5;197m～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●")
print("")
try:
    get("https://www.google.com/")
    internet = True
    print("\t\t\t\t Connected !!")
    print("\n")
except:
    print("\tYou are not Connected to Internet. Please Turn on your Mobile Data")
    print("\n")
    exit()
print("")
domain = input("\033[95m    Enter domain >>> ")
print("\n")
print("\033[38;5;21m           ┍──━──━──┙◆┕──━──━──┑┍──━──━──┙◆┕──━──━──┑")
print("\n")
file = open('wordlist.txt','r')
content = file.read()

subdomains = content.splitlines()

for subdomain in subdomains:
	url1 = f"http://{subdomain}.{domain}"
	url2 = f"https://{subdomain}.{domain}"
	try:
		requests.get(url1)
		print(f"\033[94m            Discovered URL: {url1}")
		requests.get(url2)
		print(f"\033[94m            Discovered URL: {url2}")
	except requests.ConnectionError:
		pass
print("\n")
print("\033[38;5;21m           ┕──━──━──┑◆┍──━──━──┙┕──━──━──┑◆┍──━──━──┙")
print("\n")
print("\033[38;5;197m       Thanks for Using Subd0main Shark !!")
print("\n")
