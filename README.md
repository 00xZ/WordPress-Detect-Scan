# WordPress-Detect-Scan
Use python to scan for wordpress sites and scan dir from list for known CVE's



wpdetect.py - Detects if a server is running wordpress #outputs list to WP_SERVERS.txt. Dumps servers to temp wp.txt for loop scanning using wpload.py
Eexample: wpdetect.py ip_list.txt

wpload.py - Run commands against wp.txt. my use is running sqlmap against all wordpress servers with a dir known for sqli CVE
Eexample: wpload.py wp.txt

wp-dirscan.py - scans WP_SERVERS.txt/wp.txt for dir added to 2nd argument
example: wp-dirscan.py wp.txt DirList.txt

wpdump.bat - windows loop for running all these
