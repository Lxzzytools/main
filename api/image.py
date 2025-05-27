@echo off
mode 85, 20
set current_path=%cd%
cd %current_path%/files
chcp 65001 >nul
 
 
 
:banner
cls
echo.
echo.
echo.
ping localhost -n 2 >nul
echo                         [34m  ▄▄▄· ▄▄▄· ▄▄▄▄▄ ▄▄·  ▄ .▄[0m
ping localhost -n 1 >nul
echo                         [34m ▐█ ▄█▐█ ▀█ •██  ▐█ ▌▪██▪▐█[0m
ping localhost -n 1 >nul
echo                         [36m  ██▀·▄█▀▀█  ▐█.▪██ ▄▄██▀▐█[0m
ping localhost -n 1 >nul
echo                         [36m ▐█▪·•▐█ ▪▐▌ ▐█▌·▐███▌██▌▐▀[0m
ping localhost -n 1 >nul
echo                         [96m .▀    ▀  ▀  ▀▀▀ ·▀▀▀ ▀▀▀ ·[0m
echo.
echo.
echo.
 
:input
ping localhost -n 1 >nul
echo       [36m═╦════► [0m [36m/ 1 - Winrar Cracker \ 				4 - Next Page [0m
ping localhost -n 1 >nul
echo        [36m╩╦════► [0m [0m [36m/ 2 -  DDOS \[0m
ping localhost -n 1 >nul
echo         [36m╩═══╦═► [0m [0m [36m/ 3 -  Website Attacker \[0m
echo         [36m    ║ [0m [0m
echo|set /p=[36m            ╚═══►[0m
choice /c 1234 >nul
 
 
if /I "%errorlevel%" EQU "1" (
	start winrar.bat
	goto :banner
) else if /I "%errorlevel%" EQU "2" (
	start ddos.py
	goto :start
) else if /I "%errorlevel%" EQU "3" (
	start website.py
	goto :start
) else if /I "%errorlevel%" EQU "4" (
	goto :page2
)
 
:page2
cls
echo.
echo.
echo.
ping localhost -n 2 >nul
echo                         [35m  ▄▄▄· ▄▄▄· ▄▄▄▄▄ ▄▄·  ▄ .▄[0m
ping localhost -n 1 >nul
echo                         [35m ▐█ ▄█▐█ ▀█ •██  ▐█ ▌▪██▪▐█[0m
ping localhost -n 1 >nul
echo                         [36m  ██▀·▄█▀▀█  ▐█.▪██ ▄▄██▀▐█[0m
ping localhost -n 1 >nul
echo                         [36m ▐█▪·•▐█ ▪▐▌ ▐█▌·▐███▌██▌▐▀[0m
ping localhost -n 1 >nul
echo                         [96m .▀    ▀  ▀  ▀▀▀ ·▀▀▀ ▀▀▀ ·[0m
echo.
echo.
echo.
 
:input2
ping localhost -n 1 >nul
echo       [36m═╦════► [0m [36m/ 1 - perm spoof \ 				4 - Previous Page [0m
ping localhost -n 1 >nul
echo        [36m╩╦════► [0m [0m [36m/ 2 -  check serials \[0m
ping localhost -n 1 >nul
echo         [36m╩═══╦═► [0m [0m [36m/ 3 -  Fix serials not changing \[0m
echo         [36m    ║ [0m [0m
echo|set /p=[36m            ╚═══►[0m
choice /c 1234 >nul
 
 
 
if /I "%errorlevel%" EQU "1" (
 
	executable.exe /IVN %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /IV %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /IV %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /SM %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /SP %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /SV %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /SS %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /SU AUTO
	executable.exe /SK %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /SF %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /BM %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /BP %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /BV %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /BS %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /BT %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /BLC %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /CM %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /CV %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /CS %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /CA %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /CSK %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /PSN %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /PAT %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /PPN %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /OS 1 %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /OS 2 %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /OS 3 %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /OS 4 %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /OS 5 %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /OS 6 %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /OS 7 %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /OS 8 %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /OS 9 %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /OS 10 %RANDOM%-%RANDOM%-%RANDOM%
	executable.exe /OS 11 %RANDOM%-%RANDOM%-%RANDOM%
	net stop winmgmt /Y >nul
	goto :perm
) else if /I "%errorlevel%" EQU "2" (
 
	cls
	wmic bios get serialnumber
	wmic csproduct get uuid
	wmic cpu get serialnumber
	wmic baseboard get serialnumber
	wmic baseboard get manufacturer
	pause
	goto :perm
) else if /I "%errorlevel%" EQU "3" (
 
	net stop winmgmt /Y >nul
	net stop winmgmt /Y >nul
	net stop winmgmt /Y >nul
	net stop winmgmt /Y >nul
	net stop winmgmt /Y >nul
	pause
	goto :perm
) else if /I "%errorlevel%" EQU "4" (
	goto :start
) 
