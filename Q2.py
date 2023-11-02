# Use nmap to get the dns-brute hostnames
# Launched an ec2 instance  - Ubuntu OS,
# updated OS, installed nmap
# ran script - ('nmap --script dns-brute herovired.com')

'''
beta.herovired.com - 65.2.118.110
www.herovired.com - 3.108.107.11
help.herovired.com - 104.16.51.111
demo.herovired.com - 13.127.179.32
'''

# Stored the subdomain in a file

'''Python script to check if the site is up and running'''

# importing module
import requests
# using pretty table 
from prettytable import PrettyTable

t = PrettyTable(['URL', 'UP/DOWN'])

# function for scanning subdomains
def domain_scanner(domain_name,sub_domnames):
	print('----URL after scanning subdomains----')
	
	# loop for getting URL's
	for subdomain in sub_domnames:
	
		# making url by putting subdomain one by one
		url = f"https://{subdomain}.{domain_name}"
		
		# using try catch block to avoid crash of the program
		try:
			# sending get request to the url
			requests.get(url)
			
            # if no exception then it will add a row to the table
            t.add_row([f'{url}', 'UP'])
			# if after putting subdomain one by one url 
			# is valid then printing the url
			print(f'[+] {url}')
			
			# if url is invalid then pass it
		except requests.ConnectionError:
            # if exception add the row to the table as website is down
            t.add_row([f'{url}', 'DOWN'])
			pass

# main function
if __name__ == '__main__':

	# inputting the domain name
	dom_name = input("Enter the Domain Name:")

	# opening the subdomain text file
	with open('./list_subdomains.txt','r') as file:
	
		# reading the file
		name = file.read()
		
		# using splitlines() function storing the list
		# of splitted strings
		sub_dom = name.splitlines()
		
	# calling the function for scanning the subdomains
	# and getting the url
	domain_scanner(dom_name,sub_dom)
	
    print(t)