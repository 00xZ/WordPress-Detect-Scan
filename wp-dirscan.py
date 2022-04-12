import requests #add xss scan and jquery version detect
from bs4 import BeautifulSoup
from lxml import html, etree
import sys, fnmatch
import re
def title(url, headers): #start concurent threads scan all 10 at once
	inputext = open(sys.argv[2])
	print("[+] Searching: " + url)
	for i in inputext.readlines():
		ext = i.strip("\n")
		url2 = (url + '' + ext)
		try:
			r = requests.get(url2, timeout=7, verify=True, headers=headers)
			soup = BeautifulSoup(r.content, 'lxml')
			title = (soup.select_one('title').text)
			#print("  [+] Server: " + url2 + " : " + title + "  [+]")
			TizOrTiznot = re.search(".*ot.*ound.*", title) == None
			#TizOrTiznot2 = re.search(".*404.*Not.*Found.*", title) == None
			print(TizOrTiznot)
			if TizOrTiznot == True :#or TizOrTiznot2 == True:
				print("\n Gotcha: " + url2 + " : " + title + "\n\n")
				dumper = (url2 + "\n")
				with open('ExtFound.txt', 'a') as f:
					f.writelines(dumper)
			else:
				pass
		except: pass
def testwp(ip):
	url = (ip)
	headers = {
    'Accept-Encoding': '*',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': '*/*',   
	}
	try:
		httpre = requests.get(url, timeout=7, headers=headers)
		title(url, headers)
	except: pass
	#url = ("http://" + ip + "/")
	#title(url, headers)
def main():
	with open('wp.txt', 'w') as f:
		f.writelines(" ")
	print("    WordPress Plugin Detection\n")
	input_file = open(sys.argv[1])
	for i in input_file.readlines():
		ip = i.strip("\n")
		testwp(ip)
main()
