import requests
from time import sleep
import os
import json
import sys

print('Ciwi-Ciwi Spoon.\n')
print(
    'Created by [ K O N A ].\n'
)
print('   gunakan secara benar !!')
print('jangan lupa memakai pengaman\n')
print('Fitur :\n- LISTENER & TAPLOVE\n')
print('Jumlah maksimal Bot :\n - 200\n')
API_BASE_URL = "https://id-api.spooncast.net/lives/"
API_CMD = "/join/"
sleep(1)
txtid = input("Link Live : ")
response = requests.get(txtid)
url = response.url
slink = url[34:-59]
print('ID LIVE : ' + slink)
UAInput = open('UALIST.txt', 'r').read().splitlines()
DBTEST = ("token.txt")
jml = int(input('Jumlah Taplove : '))
time = 0
user_token_list = open(DBTEST, 'r').read().splitlines()
print('Proses Taplove >>> ')
sleep(1)
for i in range(0, jml):
	with open(DBTEST) as f:
		lst = f.read().splitlines()
		paramex = {'cv': 'heimdallr'}
		headers = {
		    'Authorization':
		    'Token ' + str(lst[i]),
		    'accept':
		    'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		    'accept-encoding':
		    'gzip, deflate, br',
		    'accept-language':
		    'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		    'origin':
		    'https://www.spooncast.net',
		    'referer':
		    'https://www.spooncast.net/',
		    'sec-fetch-dest':
		    'empty',
		    'sec-fetch-mode':
		    'cors',
		    'sec-fetch-site':
		    'same-site',
		    'content-type':
		    'application/json',
		    'user-agent':
		    str(UAInput[i])
		}
		with requests.Session() as c:
			r = c.post(
			    API_BASE_URL + slink + API_CMD,
			    headers=headers,
			    params=paramex)
			r2 = c.post(
			    API_BASE_URL + slink + '/like/',
			    headers=headers,
			    params=paramex)
			print(i + 1, 'Server Status', r.status_code,
			      'Token Used : %s' % (user_token_list[i]))
			sleep(time)