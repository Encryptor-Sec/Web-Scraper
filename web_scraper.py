#!/usr/bin/python

# importing required modules

import socket
import os
import requests
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen

# Banner for Web Scraper

logo = '''

 ######################################################################### 
 #   __          __  _        _____                                      #
 #   \ \        / / | |      / ____|                                     #
 #    \ \  /\  / /__| |__   | (___   ___ _ __ __ _ _ __   ___ _ __       #
 #     \ \/  \/ / _ \ '_ \   \___ \ / __| '__/ _` | '_ \ / _ \ '__|      #
 #      \  /\  /  __/ |_) |  ____) | (__| | | (_| | |_) |  __/ |         # 
 #       \/  \/ \___|_.__/  |_____/ \___|_|  \__,_| .__/ \___|_|         #
 #                                                | |                    # 
 #                                                |_|                    #
 #########################################################################
 #                                                                       #
 #                <- A melange of Web Tool for Web Hacking ->            #
 #                                                                       #
 #########################################################################       
                  #        Developed By Encryptor        #   
                  #   Twitter : _.encryptor._            #   
                  #   Website : www.cyberbuddy.co.in     #   
                  #   Owner   : Sathyaprakash Sahoo      #   
                  ########################################                          
'''
menu = '''
  [+] \033[4mChoose An Option\033[0m
  _________________________________________________________
 | [1] Find ASN               |   [11] External Links      |
 | [2] HTTP Header            |   [12] Banner Grab         |
 | [3] Find Sub-Domains       |   [13] Subnet Lookup       |
 | [4] Find Web Technology    |   [14] Reverse IP Lookup   |
 | [5] Find Admin Panel       |   [15] Geo-location        | 
 | [6] Find Directory         |   [16] DNS Lookup          |
 | [7] Whois Information      |   [17] Trace Route         |
 | [8] Port Scan              |   [18] Firewall Detect     |
 | [9] TCP Scan               |   [19] Vulnerability Scan  |
 | [10] UDP Scan              |   [20] Zone Transfer       |
 +---------------------------------------------------------+
 | [N] New Target        [X] Unistall        [E] Exit      |
 +---------------------------------------------------------+
'''
print(logo)

def ping():
	global domain
	global IP
	domain = input("Enter Target Address [Example.com / IP]: ")
	try:	
		IP = socket.gethostbyname(domain)
	except socket.gaierror or requests.ConnectionError:
		print("\n\033[0;31m[*] Invalid Target Address\033[0m\n")
		ping()
	else:	
		response = os.system("ping -c 1 " + domain)
		if response == 0:
			print("\n\033[0;31m[-] Target is Live\033[0m")
			print(menu)
		else:
			print("\n\033[0;31m[!] Oops!! Target is not Live\033[0m\n")
			ping()

	# Creating global function for Domain ping and Assesment

def Exit():
	while True :
		cond = input("Are you sure (y/n) : ")
		if cond == str('y'or 'Y'):
			exit()	
		elif cond == str('n' or 'N'):
			os.system("clear")
			print(logo)
			ping()			
			option()
		else:
			print("\n\033[0;31m[!] Invalid Input\033[0m\n")

	# Exit function to Exit the Tool

def option():	
	opt = input("[+] Select an Option : ")  

	# Taking input for Testing

	if opt == str('e' or 'E'):                   
		Exit() 

	# Input for Exit

	elif opt == str('n' or 'N') :
		ping()
		option()

	# Input for New Target

	elif opt == str('x' or 'X') :
		while True :
			uni_cond = input("Are you sure (y/n) : ")
			if uni_cond == str('y' or 'Y'):
				os.system("cd .. && rm -rf Web-Scraper")
			elif uni_cond == str('n' or 'N'):
				os.system("clear")
				print(logo)
				ping()			
				option()
			else:
				print("\n\033[0;31m[!] Invalid Input\033[0m\n")

	# Input for Uninstalling Web Scraper

	elif opt == '1' :
		os.system("clear")	
		os.system('curl https://ipinfo.io/'+IP+'/org?token=d2f5771a7ad7b0')
		x= input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for ASN 	

	elif opt == '2' :
		os.system("clear")
		os.system('curl https://api.hackertarget.com/httpheaders/?q=https://www.google.com')
		x= input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for HTTP HEADER

	elif opt == '3' :
		os.system("clear")
		file = open("subdomain.txt")
		content = file.read()
		subdomains = content.splitlines()
		print("[+] Fetching Subdomains...")
		for subdomain in subdomains:
			link = f"https://{subdomain}.{domain}"
			url = link.replace("https://","")
			try:
				requests.get(link)
			except requests.ConnectionError:
				pass
			else:
				print(url)
		x= input("\n[+] Press Enter For Menu : ")	
		print(menu)
		option()

	# Input for Subdomain Enumeration

	elif opt == '4' :
		os.system("clear")
		os.system('whatweb '+ domain )
		x= input("\n[+] Press Enter For Menu : ")		
		print(menu)
		option()

	# Input for Web Technology

	elif opt == '5' :
		os.system("clear")
		f = open("admin_panel.txt","r")
		print("\n[+] Enumerating Admin Panel...  \n")
		while True :
			sub_link=f.readline()
			if not sub_link:
				break
			req_link = "http://"+domain+"/"+sub_link
			req = Request(req_link)
			try:
				admin_response=urlopen(req)
			except HTTPError as e:
				continue
			except URLError as e:
				continue
			except request.ConnectionError:
				pass
			else:
				print(req_link)
			
		x= input("\n[+] Press Enter For Menu : ")		
		print(menu)
		option()

	# Input for Admin Panel Enumeration

	elif opt == '6' :
		os.system("clear")
		f=open("directories.txt","r")
		print("[+] Enumerating Directories... \n")
		while True:
			dir_links = f.readline()
			if not dir_links:
				break
			dir_link = "http://"+domain+"/"+dir_links
			dir_req = Request(dir_link)
			try:
				dir_response=urlopen(dir_req)
			except HTTPError as e:
				continue
			except URLError as e:
				continue
			else:
				print(dir_link)
		x= input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for Directory Brute Forcing

	elif opt == '7' :
		os.system("clear")
		os.system("whois "+domain)
		x= input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for WHOIS information

	elif opt == '8' :
		os.system("clear")
		os.system("curl https://api.hackertarget.com/nmap/?q="+domain)
		x= input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for port scan

	elif opt == '9' :
		os.system("clear")
		os.system("curl https://api.hackertarget.com/tcp-port-scan/?q="+domain)
		x= input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for TCP scan

	elif opt == '10' :
		os.system("clear")
		os.system("curl https://api.hackertarget.com/udp-port-scan/?q="+domain)
		x= input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for UDP scan

	elif opt == '11' :
		os.system("clear")
		print("[+] External Links : ")
		os.system("curl https://api.hackertarget.com/pagelinks/?q="+domain)
		x= input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for External links

	elif opt == '12':
		os.system("clear")
		os.system("curl -I "+ domain)
		x= input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for Banner grab

	elif opt == '13' :
		os.system("clear")
		subnet = input("Enter Subnet Number : ")
		os.system("curl https://api.hackertarget.com/subnetcalc/?q="+IP+"/"+subnet)
		x= input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for Subnet Lookup

	elif opt == '14' :
		os.system ("clear")
		os.system ("curl https://api.hackertarget.com/reverseiplookup/?q="+IP)
		x=input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for Reverse IP lookup

	elif opt == '15' :
		os.system ("clear")
		os.system ("curl https://api.hackertarget.com/geoip/?q="+IP)
		x=input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for GeoIP location

	elif opt == '16' :
		os.system ("clear")
		os.system ("curl https://api.hackertarget.com/dnslookup/?q="+domain)
		x=input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for DNS lookup

	elif opt == '17' :
		os.system ("clear")
		os.system ("curl https://api.hackertarget.com/mtr/?q="+domain)
		x= input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for Trace Route

	elif opt == '18' :
		os.system("clear")
		os.system ("nmap -p 80,443 --script=http-waf-fingerprint "+domain)
		x= input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for Firewall detection

	elif opt == '19' :
		os.system("clear")
		os.system("nikto -h "+domain)
		x= input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for Vulnerability scanner

	elif opt == '20' :
		os.system("clear")
		os.system("dig "+domain)
		x= input("\n[+] Press Enter For Menu : ")
		print(menu)
		option()

	# Input for Zone transfer

	else :
		print("\033[0;31m[!] Invalid Input\033[0m")
		option()

	# Invalid Input Warning
		
if __name__ == "__main__":
	ping()	
	option()





