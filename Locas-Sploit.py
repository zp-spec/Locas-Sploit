from os import *
import webbrowser
gr, r, g, y, b, p, c, w=[
'\033[1;30m',
'\033[1;31m',
'\033[1;32m',
'\033[1;33m',
'\033[1;34m',
'\033[1;35m',
'\033[1;36m',
'\033[1;37m' ] 
class main:
	def tool():
		print(r)
		system("figlet Locas-Sploit")
		print("   ")
		print(f"{r}[{g}1{r}]{g} camera hack")
		print(f"{r}[{g}2{r}]{g} cv hack")
		print(f"{r}[{g}3{r}]{g} ip tools")
		print(f"{r}[{g}4{r}]{g} ddos attack")
		print(f"{r}[{g}5{r}]{g} fix")
		print(f"{r}[{g}6{r}]{g} andronix")
		print(f"{r}[{g}7{r}]{g} my instagram")
		main = input(f"{r}Locas{g} ~# ")
		if main == "1" :
			system("clear")
			system("figlet CHACK")
			print("   ")
			j = input("PRESS ENTER ")
			if j == "" :
				print("")
				system("bash CamHack.sh")
			else :
				print("good bye")
				print("")
		if main == "2" :
			system("clear")
			system("figlet CVhack")
			print("   ")
			k = input("PRESS ENTER ")
			if k == "" :
				print("")
				system("python cam-hackers.py")
			else :
				print("good bye")
				print("")
		if main == "3" :
			system("clear")
			system("figlet Ip Tools")
			ptint("  ")
			o = input("PRESS ENTER ")
			if o == "" :
				print("")
				system("bash install.sh")
				sysetm("python2 crips.py")
			else :
				print("good bye")
				print("")
		if main == "4" :
			system("clear")
			system("figlet DDOS ATTACK")
			print("   ")
			m = input("PRESS ENTER ")
			if m == "" :
				print("python3 hammer.py")
			else :
				print("good bye")
				print("")
		if main == "5" :
			system("clear")
			system("figlet FIX")
			print("   ")
			f = input("PRESS ENTER ")
			if f == "" :
				print("")
				system("bash Fix-Linux.sh")
			else :
				print("good bye")
				print("")
		if main == "6" :
			system("clear")
			system("figlet ANDRONIX")
			print("   ")
			z = input("PRESS ENTER ")
			if z == "" :
				print("")
				system("python Andronix.py")
			else :
				print("good bye")
				print("")
		if main == "7" :
			webbrowser.open("https://instagram.com/_zp_m?utm_medium=copy_link")
	tool()