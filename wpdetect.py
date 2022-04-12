import requests 
from bs4 import BeautifulSoup
from lxml import html, etree
import sys, fnmatch
import re
def title(url, headers):
	url2 = (url + 'wp-login.php')
	try:
		r = requests.get(url2, timeout=7, verify=True, headers=headers)
		soup = BeautifulSoup(r.content, 'lxml')
		title = (soup.select_one('title').text)
		print("  [+] Server: " + url + " : " + title + "  [+]")
		TizOrTiznot = re.search(".*Log.*In.*", title) == None
		if TizOrTiznot == False:
			print("\n\n Gotcha: " + url2 + " : " + title + "\n\n")
			dumper = (url + "\n")
			with open('wp.txt', 'w') as f:
				f.writelines(dumper)
			with open('WP_SERVERS.txt', 'a') as f:
				f.writelines(dumper)
		else:
			pass
	except: pass
def testwp(ip):
	url = ("http://" + ip + "/")
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
	try:
		url = ("https://" +ip+ "/")
		httpsre = requests.get(url, timeout=7, headers=headers)
		title(url, headers)
	except: pass
	#url = ("http://" + ip + "/")
	#title(url, headers)
def main():
	with open('wp.txt', 'w') as f:
		f.writelines(" ")
	print("WordPress Finder")
	input_file = open(sys.argv[1])
	for i in input_file.readlines():
		ip = i.strip("\n")
		testwp(ip)
main()
