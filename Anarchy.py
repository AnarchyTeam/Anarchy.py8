#_# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import ast
import time,random,sys,json,codecs,glob,re, string, os, tweepy, requests ,subprocess,urllib,urllib2,urllib3,wikipedia
from time import sleep
from random import randint
from urllib import urlopen
from bs4 import BeautifulSoup
import requests
from io import StringIO
from threading import Thread
#from gtts import gTTS
from googletrans import Translator

cl = LINETCR.LINE()
cl.login(token="EpuLKrSmDJnELIumuPNe.GJq7GBzzMu2nGqyaPN/ipG./ywYL+v4EdoMkqCMm2cHZGAtzTgu/vtP513MwPYas1o=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EpUvbMjt0rERCh2acH1b.lG3J7fc5sDPatBXqhRBQsW.yFJyvsvOeq7YTp8Fd1l3963wkGvohFISvGAeAB8NYAA=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="EpOcL4UZ1PxPIX37Ywh5.PT0fO6oRxm3RJkmvumHfXq.U8tN4bNCAc2t/mFXQci01dk3+1OoHlbTqFFvBpKpt88=")
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token="EpMM170Fo4Cr24xu4Zte.mze8dIVt1aOJrX3ceSwShG.EZl+yVKac5wJs4LGTLd3Ume3QDVmP8Lg6tYUr/0UpEc=")
kc.loginResult()

ka = ki
kb = kk
kd = ke = kc

#ka = LINETCR.LINE()
#ka.login(qr=True)
#ka.login(token='Ell6RQYfDDCPoUABwi9f.znm/u7lDUW3O7dlUCds5NW.FanPGiuAtpTpYkaSBjcqtDCQV/LFaCqQPI4z4Y6N0c4=')
#ka.loginResult()

#kb = LINETCR.LINE()
#kb.login(qr=True)
#kb.login(token='ElwXzZN59yLKdOo6wmT3.JfX8KE5Zbd1y9oi4UerpuW.k4MvnlFlw/h4F0I26GvrkL1dDNsh1tuAugHd6JXdaaw=')
#kb.loginResult()

#kd = LINETCR.LINE()
#kd.login(qr=True)
#kd.login(token='ElUDhYSSOMtquHbTBYU1.iWszu+q3V9Ie7Tj6b1sDiq.4jqWpcai48x/zbqXnKcZpMTbIPPj8MgBrRuVLQL1Vmo=')
#kd.loginResult()

#ke = LINETCR.LINE()
#ke.login(qr=True)
#ke.login(token='')
#ke.loginResult()

print "Anarchy Team Bots"

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
╔════════════════════════
║ 👑 PUBLIC COMMAND 👑
╠════════════════════════
╠ 「 About 」
╠ 「 Me 」
╠ 「 Myid 」
╠ 「 Gid 」
╠ 「 Ginfo 」
╠ 「 Gcreator 」
╠ 「 Youtube 」
╠ 「 Music 」
╠ 「 Tr-id 」
╠ 「 Tr-en 」
╠ 「 Ig 」
╠ 「 Wiki 」
╠ 「 Tagall 」
╠ 「 Setpoint 」
╠ 「 Viewlastseen 」
╠════════════════════════
║ 👑 STAFF COMMAND 👑
╠════════════════════════
╠ 「 Protectqr on/off 」
╠ 「 Protectinvite on/off 」
╠ 「 Protect on/off 」
╠ 「 Adminlist 」
╠ 「 Buka 」
╠ 「 Tutup 」
╠ 「 Getqr 」
╠════════════════════════
║ 👑 ADMIN COMMAND 👑
╠════════════════════════
╠ 「 Staff on @ 」
╠ 「 Unstaff on @ 」
╠ 「 Ban on @ 」
╠ 「 Unban on @ 」
╠ 「 Wl on @ 」
╠ 「 Unwl on @ 」
╠════════════════════════
║ 👑 OWNER COMMAND 👑
╠════════════════════════
╠ 「 Admin on @ 」
╠ 「 Unadmin on @ 」
╠ 「 Bot on @ 」
╠ 「 Unbot on @ 」
╠ 「 Botlist 」
╠ 「 Banlist 」
╠ 「 Whitelist 」
╠ 「 Adminlist 」
╠ 「 Clear admin 」
╠ 「 Clear staff 」
╠ 「 Clear White 」
╠ 「 Allname: 」
╠ 「 Allbio: 」
╠ 「 1-6Clone 」
╠ 「 1-6Bio: 」
╠ 「 1-6Name: 」
╠════════════════════════
║ Anarchy Team Bots
║ Bot Protected
╚════════════════════════
"""

KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ka.getProfile().mid
Emid = kb.getProfile().mid
Fmid = kd.getProfile().mid
Gmid = ke.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid]
admin=["uc77fd25b59f6e563d84f1334f3fed10b"]
#admin=["u34797caa6c3d49029a6802f33488e4bb"]

wait = {
    'contact':False,
    'autoJoin':True,
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":True,
    "clock":True,
    "cName":"Miyuki",
    "blacklist":{},
    "whitelist":{},
    "GC":{},
    "pOn":{},
    "lOn":{},
    "cOn":{},
    "admin":{},
    "listbot":{},
    "Ban":{},
    "Unban":{},
    "White":{},
    "Unwhite":{},
    "Admin":{},
    "Unadmin":{},
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

with open('st2__b.json','r') as fp:
        wait = json.load(fp)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def restart():
	python = sys.executable
	os.execl(python, python, *sys.argv)

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â£ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â»" + Name
                wait2['ROM'][op.param1][op.param2] = "ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â£ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â»" + Name
        else:
            pass
    except:
        pass

#===============================================================================
agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

def translate(to_translate, to_language="auto", language="auto"):
    bahasa_awal = "auto"
    bahasa_tujuan = to_language
    kata = to_translate
    url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
    agent = {'User-Agent':'Mozilla/5.0'}
    cari_hasil = 'class="t0">'
    request = urllib2.Request(url, headers=agent)
    page = urllib2.urlopen(request).read()
    result = page[page.find(cari_hasil)+len(cari_hasil):]
    result = result.split("<")[0]
    return result

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi
def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }

        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        print r
        if r.status_code != 201:
            raise Exception('Upload audio failure.')

def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
            raise e

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def mention2(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

#==========================================================================

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
	if op.type == 19:
		bots = [Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
		team = admin+[Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
		if op.param2 not in team and op.param2 not in wait["GC"] and op.param2 not in wait["admin"] and op.param2 not in wait["whitelist"] and op.param3 not in wait["listbot"]:
			if op.param3 not in bots and op.param3 not in wait["listbot"]:
				if wait["pOn"][op.param1] == True:
					try:
						kk.kickoutFromGroup(op.param1,[op.param2])
						kk.findAndAddContactsByMid(op.param3)
						kk.inviteIntoGroup(op.param1,[op.param3])
					except:
						try:
							kk.kickoutFromGroup(op.param1,[op.param2])
							kk.findAndAddContactsByMid(op.param3)
							kk.inviteIntoGroup(op.param1,[op.param3])
						except:
							try:
								kc.kickoutFromGroup(op.param1,[op.param2])
                	                                        kc.findAndAddContactsByMid(op.param3)
								kc.kickoutFromGroup(op.param1,[op.param2])
							except:
	                                                        try:
									ka.kickoutFromGroup(op.param1,[op.param2])
			                                                ka.findAndAddContactsByMid(op.param3)
		                                                        ka.inviteIntoGroup(op.param1,[op.param3])
								except:
									try:
										kb.kickoutFromGroup(op.param1,[op.param2])
										kb.findAndAddContactsByMid(op.param3)
										kb.inviteIntoGroup(op.param1,[op.param3])
									except:
										try:
											kd.kickoutFromGroup(op.param1,[op.param2])
											kd.findAndAddContactsByMid(op.param3)
											kd.inviteIntoGroup(op.param1,[op.param3])
										except:
											try:
												ke.kickoutFromGroup(op.param1,[op.param2])
												ke.findAndAddContactsByMid(op.param3)
												ke.inviteIntoGroup(op.param1,[op.param3])
											except:
												cl.kickoutFromGroup(op.param1,[op.param2])
												cl.findAndAddContactsByMid(op.param3)
												cl.inviteIntoGroup(op.param1,[op.param3])

					if op.param2 in wait["blacklist"]:
						pass
					else:
						wait["blacklist"][op.param2] = True
				else:
					return
			if op.param3 in wait["listbot"]:
				pass
			if op.param3 in bots:
				try:
	                                X = ki.getGroup(op.param1)
        		                X.preventJoinByTicket = False
                	                ki.updateGroup(X)
                        	        Tiki = ki.reissueGroupTicket(op.param1)
                        	        cl.acceptGroupInvitationByTicket(op.param1,Tiki)
                        	        kk.acceptGroupInvitationByTicket(op.param1,Tiki)
                        	        kc.acceptGroupInvitationByTicket(op.param1,Tiki)
                        	        ka.acceptGroupInvitationByTicket(op.param1,Tiki)
                        	        kb.acceptGroupInvitationByTicket(op.param1,Tiki)
                        	        kd.acceptGroupInvitationByTicket(op.param1,Tiki)
					ke.acceptGroupInvitationByTicket(op.param1,Tiki)
                                	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                	X.preventJoinByTicket = True
                                	ki.updateGroup(X)
				except:
					try:
						G = kk.getGroup(op.param1)
                                        	G.preventJoinByTicket = False
                                        	kk.updateGroup(G)
	                                       	Tiki = kk.reissueGroupTicket(op.param1)
                        	        	cl.acceptGroupInvitationByTicket(op.param1,Tiki)
                        	        	ki.acceptGroupInvitationByTicket(op.param1,Tiki)
                        	        	kc.acceptGroupInvitationByTicket(op.param1,Tiki)
                        		        ka.acceptGroupInvitationByTicket(op.param1,Tiki)
                        		        kb.acceptGroupInvitationByTicket(op.param1,Tiki)
                	        	        kd.acceptGroupInvitationByTicket(op.param1,Tiki)
						ke.acceptGroupInvitationByTicket(op.param1,Tiki)
	                                	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
	       	                                G.preventJoinByTicket = True
	                                        kk.updateGroup(G)
					except:
						try:
							L = kc.getGroup(op.param1)
                	                        	L.preventJoinByTicket = False
                        	                	kc.updateGroup(L)
	                       	                	Tiki = kc.reissueGroupTicket(op.param1)
		                        	        cl.acceptGroupInvitationByTicket(op.param1,Tiki)
                		        	        ki.acceptGroupInvitationByTicket(op.param1,Tiki)
                		        	        kk.acceptGroupInvitationByTicket(op.param1,Tiki)
                		        	        ka.acceptGroupInvitationByTicket(op.param1,Tiki)
                		        	        kb.acceptGroupInvitationByTicket(op.param1,Tiki)
                		        	        kd.acceptGroupInvitationByTicket(op.param1,Tiki)
							ke.acceptGroupInvitationByTicket(op.param1,Tiki)
                			               	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        		                                L.preventJoinByTicket = True
		                                        kc.updateGroup(L)
						except:
							try:
								L = ka.getGroup(op.param1)
        	                                                L.preventJoinByTicket = False
                	                                        ka.updateGroup(L)
                	                                        Tiki = ka.reissueGroupTicket(op.param1)
			                        	        cl.acceptGroupInvitationByTicket(op.param1,Tiki)
	                		        	        ki.acceptGroupInvitationByTicket(op.param1,Tiki)
	                		        	        kk.acceptGroupInvitationByTicket(op.param1,Tiki)
	                		        	        kc.acceptGroupInvitationByTicket(op.param1,Tiki)
	                		        	        kb.acceptGroupInvitationByTicket(op.param1,Tiki)
	                		        	        kd.acceptGroupInvitationByTicket(op.param1,Tiki)
								ke.acceptGroupInvitationByTicket(op.param1,Tiki)
	                			               	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
	                                                        L.preventJoinByTicket = True
	                                                        ka.updateGroup(L)
							except:
								try:
									L = kb.getGroup(op.param1)
	        	                                                L.preventJoinByTicket = False
	                	                                        kb.updateGroup(L)
	                	                                        Tiki = kb.reissueGroupTicket(op.param1)
				                        	        cl.acceptGroupInvitationByTicket(op.param1,Tiki)
		                		        	        ki.acceptGroupInvitationByTicket(op.param1,Tiki)
		                		        	        kk.acceptGroupInvitationByTicket(op.param1,Tiki)
		                		        	        kc.acceptGroupInvitationByTicket(op.param1,Tiki)
		                		        	        ka.acceptGroupInvitationByTicket(op.param1,Tiki)
		                		        	        kd.acceptGroupInvitationByTicket(op.param1,Tiki)
									ke.acceptGroupInvitationByTicket(op.param1,Tiki)
		                			               	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		                                                        L.preventJoinByTicket = True
		                                                        kb.updateGroup(L)
								except:
									try:
										L = kd.getGroup(op.param1)
		        	                                                L.preventJoinByTicket = False
		                	                                        kd.updateGroup(L)
		                	                                        Tiki = kd.reissueGroupTicket(op.param1)
					                        	        cl.acceptGroupInvitationByTicket(op.param1,Tiki)
				             		        	        ki.acceptGroupInvitationByTicket(op.param1,Tiki)
			                		        	        kk.acceptGroupInvitationByTicket(op.param1,Tiki)
			                		        	        kc.acceptGroupInvitationByTicket(op.param1,Tiki)
        			        		        	        ka.acceptGroupInvitationByTicket(op.param1,Tiki)
                					        	        kb.acceptGroupInvitationByTicket(op.param1,Tiki)
										ke.acceptGroupInvitationByTicket(op.param1,Tiki)
                						               	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			                                                        L.preventJoinByTicket = True
			                                                        kd.updateGroup(L)
									except:
										try:
											L = ke.getGroup(op.param1)
			        	                                                L.preventJoinByTicket = False
			                	                                        ke.updateGroup(L)
			                	                                        Tiki = ke.reissueGroupTicket(op.param1)
						                        	        cl.acceptGroupInvitationByTicket(op.param1,Tiki)
					             		        	        ki.acceptGroupInvitationByTicket(op.param1,Tiki)
				                		        	        kk.acceptGroupInvitationByTicket(op.param1,Tiki)
				                		        	        kc.acceptGroupInvitationByTicket(op.param1,Tiki)
	        			        		        	        ka.acceptGroupInvitationByTicket(op.param1,Tiki)
	                					        	        kb.acceptGroupInvitationByTicket(op.param1,Tiki)
											kd.acceptGroupInvitationByTicket(op.param1,Tiki)
	                						               	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
				                                                        L.preventJoinByTicket = True
				                                                        ke.updateGroup(L)
										except:
											L = cl.getGroup(op.param1)
			        	                                                L.preventJoinByTicket = False
			                	                                        cl.updateGroup(L)
			                	                                        Tiki = cl.reissueGroupTicket(op.param1)
						                        	        ki.acceptGroupInvitationByTicket(op.param1,Tiki)
					             		        	        kk.acceptGroupInvitationByTicket(op.param1,Tiki)
				                		        	        kc.acceptGroupInvitationByTicket(op.param1,Tiki)
				                		        	        ka.acceptGroupInvitationByTicket(op.param1,Tiki)
	        			        		        	        kb.acceptGroupInvitationByTicket(op.param1,Tiki)
	                					        	        kd.acceptGroupInvitationByTicket(op.param1,Tiki)
											ke.acceptGroupInvitationByTicket(op.param1,Tiki)
	                						               	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
				                                                        L.preventJoinByTicket = True
				                                                        cl.updateGroup(L)
				if op.param2 in wait["blacklist"]:
                                        pass
                                else:
                                        wait["blacklist"][op.param2] = True
		else:
			pass
		print "19" + "\n" + op.param1+"\n" +  op.param2 + "\n" + op.param3 +"\n"
	if op.type == 13:
		team = [Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
		if mid in op.param3:
		    if op.param2 in admin or op.param2 in wait["admin"]:
                        cl.acceptGroupInvitation(op.param1)
                        wait["pOn"][op.param1] = True
                        wait["cOn"][op.param1] = True
                        wait["lOn"][op.param1] = True
                        wait["Ban"][op.param1] = False
                        wait["Unban"][op.param1] = False
                        wait["White"][op.param1] = False
                        wait["Unwhite"][op.param1] = False
                        wait["Admin"][op.param1] = False
                        wait["Unadmin"][op.param1] = False
                        with open('st2__b.json','w') as fp:
                              json.dump(wait, fp, sort_keys=True, indent=4)
                        cl.sendText(op.param1,"")
		    else:
			pass
		if Amid in op.param3:
		    if op.param2 in admin or op.param2 in wait["admin"]:
                        ki.acceptGroupInvitation(op.param1)
		    else:
			pass
		if Bmid in op.param3:
		    if op.param2 in admin or op.param2 in wait["admin"]:
                        kk.acceptGroupInvitation(op.param1)
		    else:
			pass
		if Cmid in op.param3:
		    if op.param2 in admin or op.param2 in wait["admin"]:
                        kc.acceptGroupInvitation(op.param1)
		    else:
			pass
		if Dmid in op.param3:
		    if op.param2 in admin or op.param2 in wait["admin"]:
                        ka.acceptGroupInvitation(op.param1)
		    else:
			pass
		if Emid in op.param3:
		    if op.param2 in admin or op.param2 in wait["admin"]:
                        kb.acceptGroupInvitation(op.param1)
		    else:
			pass
		if Fmid in op.param3:
		    if op.param2 in admin or op.param2 in wait["admin"]:
                        kd.acceptGroupInvitation(op.param1)
		    else:
			pass
		team = admin+[Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
		if op.param2 not in team and op.param2 not in wait["GC"] and op.param2 not in wait["admin"] and op.param2 not in wait["whitelist"]:
                        if wait["cOn"][op.param1] == True:
                                x = ki.getGroup(op.param1)
                                ginv = [contact.mid for contact in x.invitee]
                                ki.cancelGroupInvitation(op.param1,ginv)
                                cl.cancelGroupInvitation(op.param1,[op.param3])
                        if op.param3 in wait["blacklist"]:
                               cl.cancelGroupInvitation(op.param1,[op.param3])
                               x = ki.getGroup(op.param1)
                               ginv = [contact.mid for contact in x.invitee]
                               ki.cancelGroupInvitation(op.param1,ginv)
                               kc.kickoutFromGroup(op.param1,[op.param2])
		print "13" + "\n" + op.param1+"\n" +  op.param2 + "\n" + op.param3 + "\n"
		return
	if op.type == 17:
 		 bots = [Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
		 if op.param2 in wait["blacklist"]:
			try:
				kk.kickoutFromGroup(op.param1,[op.param2])
			except:
				try:
					ki.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						kc.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							ka.kickoutFromGroup(op.param1,[op.param2])
						except:
     							try:
								kb.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									kd.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ke.kickoutFromGroup(op.param1,[op.param2])
									except:
										cl.kickoutFromGroup(op.param1,[op.param2])
		 if op.param2 not in wait["listbot"] and op.param2 not in bots and op.param2 not in admin:
			cl.sendText(op.param1,"Selamat Datang di group\nSemoga betah Jangan Nakal!!")
			cl.sendText(op.param1,"WELCOME")
			pass
		 if op.param2 in admin:
			cl.sendText(op.param1,"Welcome")
			pass
                 print "17" + "\n" + op.param1+"\n" + op.param2 + "\n" + op.param3 + "\n"
	if op.type == 11:
		team = admin+[Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
		print team
		if op.param2 not in team and op.param2 not in wait["GC"] and op.param2 not in wait["admin"] and op.param2 not in wait["whitelist"]:
			if wait["lOn"][op.param1] == True:
				try:
					ki.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						ki.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							kc.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								ka.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									kb.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										kd.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											ke.kickoutFromGroup(op.param1,[op.param2])
										except:
											cl.kickoutFromGroup(op.param1,[op.param2])
				X = ki.getGroup(op.param1)
				X.preventJoinByTicket = True
				ki.updateGroup(X)
				if op.param2 in wait["blacklist"]:
					pass
				else:
					wait["blacklist"][op.param2] = True
 			else:
				pass
		else:
			pass
		print "11" + "\n" + op.param1+"\n" +  op.param2 + "\n" + op.param3 + "\n"
		return
	if op.type == 32:
		if op.param3 in admin or op.param3 in wait["GC"] or op.param3 in wait["admin"]:
			if op.param2 not in admin and wait["GC"] and wait["admin"]:
				if wait["pOn"] == True:
					try:
						ka.findAndAddContactsByMid(op.param3)
						ka.inviteIntoGroup(op.param1,[op.param3])
						ka.kickoutFromGroup(op.param1,[op.param2])
					except:
						try:
							kb.findAndAddContactsByMid(op.param3)
							kb.inviteIntoGroup(op.param1,[op.param3])
							kb.kickoutFromGroup(op.param1,[op.param2])
						except:
							try:
								kd.findAndAddContactsByMid(op.param3)
								kd.inviteIntoGroup(op.param1,[op.param3])
								kd.kickoutFromGroup(op.param1,[op.param2])
							except:
								try:
									ke.findAndAddContactsByMid(op.param3)
									ke.inviteIntoGroup(op.param1,[op.param3])
									ke.kickoutFromGroup(op.param1,[op.param2])
								except:
									try:
										ki.findAndAddContactsByMid(op.param3)
										ki.inviteIntoGroup(op.param1,[op.param3])
										ki.kickoutFromGroup(op.param1,[op.param2])
									except:
										try:
											kk.findAndAddContactsByMid(op.param3)
											kk.inviteIntoGroup(op.param1,[op.param3])
											kk.kickoutFromGroup(op.param1,[op.param2])
										except:
											kc.findAndAddContactsByMid(op.param3)
											kc.inviteIntoGroup(op.param1,[op.param3])
											kc.kickoutFromGroup(op.param1,[op.param2])
				else:
					pass
			else:
				pass
		else:
			pass
		print "32" + "\n" + op.param1+"\n" +  op.param2 + "\n" + op.param3 + "\n"
	if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
        if op.type == 26:
  	    lurkGroup = ""
            dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
	    reading = []
            msg = op.message
            if msg.contentType == 13:
               if wait["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
			xxx = msg.contentMetadata["mid"]
			get = cl.getContact(xxx).displayName
			stts = cl.getContact(xxx).statusMessage
			if xxx in wait["blacklist"] and wait ["whitelist"]:
				print "yes"
				cl.sendText(msg.to,"Name:["+get+"]\nmid:["+msg.contentMetadata["mid"]+"]\nStatus Message:\n"+stts+"\n\nBlacklist = Yes\nWhitelist = Yes")
				wait["contact"] = False
			elif xxx in wait["blacklist"] and xxx not in wait ["whitelist"]:
				print "yes-no"
				cl.sendText(msg.to,"Name:["+get+"]\nmid:["+msg.contentMetadata["mid"]+"]\nStatus Message:\n"+stts+"\n\nBlacklist = Yes\nWhitelist = No")
                                wait["contact"] = False
			elif xxx not in wait["blacklist"] and xxx in wait ["whitelist"]:
				print "no-yes"
				cl.sendText(msg.to,"Name:["+get+"]\nmid:["+msg.contentMetadata["mid"]+"]\nStatus Message:\n"+stts+"\n\nBlacklist = No\nWhitelist = Yes")
                                wait["contact"] = False
	                elif xxx not in wait["blacklist"] and wait["whitelist"]:
			      print "2no"
			      cl.sendText(msg.to,"Name:["+get+"]\nmid:["+msg.contentMetadata["mid"]+"]\nStatus Message:\n"+stts+"\n\nBlacklist = No\nWhitelist = No")
  			      wait["contact"] = False
			elif xxx in admin:
				cl.sendText(msg.to,"Name:["+get+"]\nmid:["+msg.contentMetadata["mid"]+"]\nStatus Message:\n"+stts+"\n\nBlacklist = No\nWhitelist = Yes\n\nMY CREATOR")
                                wait["contact"] = False
			elif xxx in wait["admin"] and xxx in wait["GC"]:
				cl.sendText(msg.to,"Name:["+get+"]\nmid:["+msg.contentMetadata["mid"]+"]\nStatus Message:\n"+stts+"\n\nBlacklist = No\nWhitelist = Yes\n\n===Whitelist user===")
                                wait["contact"] = False
	       if wait["Ban"][msg.to] == True:
			msg.contentType = 0
			userx = msg.contentMetadata["mid"]
                        if userx in wait["blacklist"]:
                              cl.sendText(msg.to,"Already in blacklist")
                        else:
				if userx in admin or userx in wait["whitelist"]:
					cl.sendText(msg.to,"Cannot banned White user(s)")
				else:
					wait["blacklist"][userx] = True
                                        with open('st2__b.json','w') as fp:
                                               json.dump(wait, fp, sort_keys=True, indent=4)
					cl.sendText(msg.to,"Success")
	       if wait["Unban"][msg.to] == True:
			g = msg.contentMetadata["mid"]
                        if g in wait["blacklist"]:
			       del wait["blacklist"][g]
	                       with open('st2__b.json', 'w') as fp:
                                     json.dump(wait, fp, sort_keys=True, indent=4)
                               cl.sendText(msg.to,"Deleted")
                        else:
                               cl.sendText(msg.to,"Not in blacklist")
	       if wait["White"][msg.to] == True:
                        msg.contentType = 0
                        userx = msg.contentMetadata["mid"]
                        if userx in wait["whitelist"]:
                              cl.sendText(msg.to,"Already in whitelist")
                        else:
                                if userx in admin or userx in wait["blacklist"]:
                                        cl.sendText(msg.to,"Cannot white black user(s)")
                                else:
                                        wait["whitelist"][userx] = True
                                        with open('st2__b.json','w') as fp:
                                               json.dump(wait, fp, sort_keys=True, indent=4)
                                        cl.sendText(msg.to,"Success")
               if wait["Unwhite"][msg.to] == True:
                        g = msg.contentMetadata["mid"]
                        if g in wait["whitelist"]:
                               del wait["whitelist"][g]
                               with open('st2__b.json', 'w') as fp:
                                     json.dump(wait, fp, sort_keys=True, indent=4)
                               cl.sendText(msg.to,"Deleted")
                        else:
                               cl.sendText(msg.to,"Not in blacklist")
	       if wait["Admin"][msg.to] == True:
                        msg.contentType = 0
                        userx = msg.contentMetadata["mid"]
                        if userx in wait["admin"]:
                              cl.sendText(msg.to,"Already in admin")
                        else:
                                if userx in admin or userx in wait["blacklist"]:
                                        cl.sendText(msg.to,"Cannot add to admin black user(s)")
                                else:
                                        wait["admin"][userx] = True
                                        with open('st2__b.json','w') as fp:
                                               json.dump(wait, fp, sort_keys=True, indent=4)
                                        cl.sendText(msg.to,"Success add to admin")
               if wait["Unadmin"][msg.to] == True:
                        g = msg.contentMetadata["mid"]
                        if g in wait["admin"]:
                               del wait["admin"][g]
                               with open('st2__b.json', 'w') as fp:
                                     json.dump(wait, fp, sort_keys=True, indent=4)
                               cl.sendText(msg.to,"Deleted")
                        else:
                               cl.sendText(msg.to,"Not in admin")
	       return
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾Ãƒâ€šÃ‚Â¢\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
	    elif msg.toType == 0:
		msg.to = msg.from_
	    elif msg.text in ["Leaveall"]:
			print "[ok]"
			gid = cl.getGroupIdsJoined()
			gidx= ki.getGroupIdsJoined()
			gidy= kk.getGroupIdsJoined()
			gidz= kc.getGroupIdsJoined()
			gida= ka.getGroupIdsJoined()
			gidb= kb.getGroupIdsJoined()
			gidc= kd.getGroupIdsJoined()
			gidd= ke.getGroupIdsJoined()
			if msg.from_ in admin:
                                cl.sendText(msg.to,"Please wait a minute...")
                                cl.sendText(msg.to,"Loading...")
				for i in gid:
					if i == msg.to:
						pass
					else:
						cl.leaveGroup(i)
				for x in gidx:
					if x == msg.to:
						pass
					else:
						ki.leaveGroup(x)
				for y in gidy:
					if y == msg.to:
						pass
					else:
						kk.leaveGroup(y)
				for z in gidz:
					if z == msg.to:
						pass
					else:
						kc.leaveGroup(z)
				for a in gida:
					if a == msg.to:
						pass
					else:
						ka.leaveGroup(a)
				for b in gidb:
					if b == msg.to:
						pass
					else:
						kb.leaveGroup(b)
				for c in gidc:
					if c == msg.to:
						pass
					else:
						kd.leaveGroup(c)
				for d in gidd:
					if d == msg.to:
						pass
					else:
						ke.leaveGroup(d)
				cl.sendText(msg.to,"Success leave all group")
			else:
				cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Admin remove:on"]:
                if msg.from_ in admin:
                        if wait ["Unadmin"][msg.to] == True:
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Already on")
                                else:
                                        cl.sendText(msg.to,"Aktif")
                        else:
                                wait["Unadmin"][msg.to] = True
                                with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Kirim kontak")
                                else:
                                        cl.sendText(msg.to,"Berhasil")
                else:
                        cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Admin remove:off"]:
                if msg.from_ in admin:
                        if wait ["Unadmin"][msg.to] == False:
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Already off")
                                else:
                                        cl.sendText(msg.to,"Done")
                        else:
                                wait["Unadmin"][msg.to] = False
                                with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Turn off")
                                else:
                                        cl.sendText(msg.to,"Done")
                else:
                        cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Admin add:on"]:
                if msg.from_ in admin:
                        if wait ["Admin"][msg.to] == True:
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Already on")
                                else:
                                        cl.sendText(msg.to,"Aktif")
                        else:
                                wait["Admin"][msg.to] = True
                                with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Kirim kontak")
                                else:
                                        cl.sendText(msg.to,"Berhasil di tambahkan")
                else:
                        cl.sendText(msg.to,"Please don't play bots")
            elif msg.text in ["Admin add:off"]:
                if msg.from_ in admin:
                        if wait ["Admin"][msg.to] == False:
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Already off")
                                else:
                                        cl.sendText(msg.to,"Done")
                        else:
                                wait["Admin"][msg.to] = False
                                with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Turn off")
                                else:
                                        cl.sendText(msg.to,"Done")
                else:
                        cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Ban remove:on"]:
                if msg.from_ in admin or msg.from_ in wait["admin"] or msg.from_ in wait["GC"]:
			if wait ["Unban"][msg.to] == True:
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Already on")
                                else:
                                        cl.sendText(msg.to,"Done")
                        else:
                                wait["Unban"][msg.to] = True
                                with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Kirim kontak")
                                else:
                                        cl.sendText(msg.to,"Berhasil")
                else:
                        cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Ban remove:off"]:
                if msg.from_ in admin or msg.from_ in wait["admin"] or msg.from_ in wait["GC"]:
                        if wait ["Unban"][msg.to] == False:
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Already off")
                                else:
                                        cl.sendText(msg.to,"Berhasil")
                        else:
                                wait["Unban"][msg.to] = False
                                with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Turn off")
                                else:
                                        cl.sendText(msg.to,"Done")
                else:
                        cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Putih remove:on"]:
                if msg.from_ in admin:
                        if wait ["Unwhite"][msg.to] == True:
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Already on")
                                else:
                                        cl.sendText(msg.to,"Done")
                        else:
                                wait["Unwhite"][msg.to] = True
                                with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Send contact")
                                else:
                                        cl.sendText(msg.to,"Done")
                else:
                        cl.sendText(msg.to,"Admins or Staffs permission required.")
            elif msg.text in ["Putih remove:off"]:
                if msg.from_ in admin:
                        if wait ["Unwhite"][msg.to] == False:
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Already off")
                                else:
                                        cl.sendText(msg.to,"Done")
                        else:
                                wait["Unwhite"][msg.to] = False
                                with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Turn off")
                                else:
                                        cl.sendText(msg.to,"Done")
                else:
                        cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Putih add:on"]:
                if msg.from_ in admin:
                        if wait ["White"][msg.to] == True:
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Already on")
                                else:
                                        cl.sendText(msg.to,"Done")
                        else:
                                wait["White"][msg.to] = True
                                with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Send contact")
                                else:
                                        cl.sendText(msg.to,"Done")
                else:
                        cl.sendText(msg.to,"Admins or Staffs permission required.")
            elif msg.text in ["Putih add:off"]:
                if msg.from_ in admin:
                        if wait ["White"][msg.to] == False:
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Already off")
                                else:
                                        cl.sendText(msg.to,"Done")
                        else:
                                wait["White"][msg.to] = False
                                with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Turn off")
                                else:
                                        cl.sendText(msg.to,"Done")
                else:
                        cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Ban add:on"]:
		if msg.from_ in admin or msg.from_ in wait["admin"]:
                        if wait ["Ban"][msg.to] == True:
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Already on")
                                else:
                                        cl.sendText(msg.to,"Aktif")
                        else:
                                wait["Ban"][msg.to] = True
                                with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Kirim Kontak")
                                else:
                                        cl.sendText(msg.to,"Berhasil")
                else:
                        cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Ban add:off"]:
		if msg.from_ in admin or msg.from_ in wait["admin"]:
                        if wait ["Ban"][msg.to] == False:
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Already off")
                                else:
                                        cl.sendText(msg.to,"Berhasil")
                        else:
                                wait["Ban"][msg.to] = False
                                with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
                                if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Turn off")
                                else:
                                        cl.sendText(msg.to,"Done")
                else:
                        cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Clear admin"]:
		if msg.from_ in admin:
			wait["admin"] = {}
			with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
        		cl.sendText(msg.to,"Done")
	    elif msg.text in ["Clear white"]:
		if msg.from_ in admin:
			wait["whitelist"] = {}
			with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
        		cl.sendText(msg.to,"Done")
	    elif msg.text in ["Clearb"]:
                if msg.from_ in admin:
                        wait["blacklist"] = {}
                        with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
	                cl.sendText(msg.to,"Done")
	    elif msg.text in ["Clear staff"]:
                if msg.from_ in admin:
                        wait["GC"] = {}
                        with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
	                cl.sendText(msg.to,"Done")
	    elif msg.text in ["@Restart"]:
                if msg.from_ in admin or msg.from_ in wait["admin"]:
			cl.sendText(msg.to,"Bot has been restart\nPlease wait a minute")
			restart()
			print "@restart"
	    elif msg.text in ["Periksa"]:
                if msg.from_ in admin or msg.from_ in wait["admin"] or msg.from_ in wait["GC"]:
			cl.sendText(msg.to,"Send contact")
			wait["contact"] = True
			return
	    elif "1Name:" in msg.text:
                if msg.from_ in admin:
                        name = msg.text.replace("1Name:","")
                        namex = name.rstrip(' ')
                        string = namex
                        if len(string.decode('utf-8')) <= 20:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
				cl.sendText(msg.to,"Success")
			else:
                                cl.sendText(msg.to,"Under 20 please")
	    elif "2Name:" in msg.text:
                if msg.from_ in admin:
                        name = msg.text.replace("2Name:","")
                        namex = name.rstrip(' ')
                        string = namex
                        if len(string.decode('utf-8')) <= 20:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
				ki.sendText(msg.to,"Success")
                        else:
				ki.sendText(msg.to,"Under 20 please")
	    elif "3Name:" in msg.text:
                if msg.from_ in admin:
                        name = msg.text.replace("3Name:","")
                        namex = name.rstrip(' ')
                        string = namex
                        if len(string.decode('utf-8')) <= 20:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
				kk.sendText(msg.to,"Success")
                        else:
				kk.sendText(msg.to,"Under 20 please")
	    elif "4Name:" in msg.text:
                if msg.from_ in admin:
                        name = msg.text.replace("4Name:","")
                        namex = name.rstrip(' ')
                        string = namex
                        if len(string.decode('utf-8')) <= 20:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendText(msg.to,"Success")
                        else:
                                kc.sendText(msg.to,"Under 20 please")
	    elif "5Name:" in msg.text:
                if msg.from_ in admin:
                        name = msg.text.replace("5Name:","")
                        namex = name.rstrip(' ')
                        string = namex
                        if len(string.decode('utf-8')) <= 20:
                                profile = ka.getProfile()
                                profile.displayName = string
                                ka.updateProfile(profile)
                                ka.sendText(msg.to,"Success")
                        else:
                                ka.sendText(msg.to,"Under 20 please")
	    elif "6Name:" in msg.text:
                if msg.from_ in admin:
                        name = msg.text.replace("6Name:","")
                        namex = name.rstrip(' ')
                        string = namex
                        if len(string.decode('utf-8')) <= 20:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendText(msg.to,"Success")
                        else:
                                kb.sendText(msg.to,"Under 20 please")
	    elif "7Name:" in msg.text:
                if msg.from_ in admin:
                        name = msg.text.replace("7Name:","")
                        namex = name.rstrip(' ')
                        string = namex
                        if len(string.decode('utf-8')) <= 20:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                kd.sendText(msg.to,"Success")
                        else:
                                kd.sendText(msg.to,"Under 20 please")
	    elif "8Name:" in msg.text:
                if msg.from_ in admin:
                        name = msg.text.replace("8Name:","")
                        namex = name.rstrip(' ')
                        string = namex
                        if len(string.decode('utf-8')) <= 20:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendText(msg.to,"Success")
                        else:
                                ke.sendText(msg.to,"Under 20 please")
	    elif "Allstatus:" in msg.text:
                if msg.from_ in admin:
                        name = msg.text.replace("Allstatus:","")
                        namex = name.rstrip(' ')
                        string = namex
                        if len(string.decode('utf-8')) <= 500:
				profile = cl.getProfile()
				profile = ki.getProfile()
				profile = kk.getProfile()
				profile = kc.getProfile()
				profile.statusMessage = string
				cl.updateProfile(profile)
				ki.updateProfile(profile)
				kk.updateProfile(profile)
				kc.updateProfile(profile)
				cl.sendText(msg.to,"Success")
                        else:
                                cl.sendText(msg.to,"Under 500 please")
	    elif "Allname:" in msg.text:
		if msg.from_ in admin:
			name = msg.text.replace("Allname:","")
			namex = name.rstrip(' ')
			string = namex
			if len(string.decode('utf-8')) <= 20:
				profile = cl.getProfile()
				profile = ki.getProfile()
				profile = kk.getProfile()
				profile = kc.getProfile()
				profile.displayName = string
				cl.updateProfile(profile)
				ki.updateProfile(profile)
				kk.updateProfile(profile)
				kc.updateProfile(profile)
				cl.sendText(msg.to,"Success")
			else:
				cl.sendText(msg.to,"Under 20 please")
	    elif msg.text in ["Respons","respons"]:
				profile = cl.getProfile()
                                profilex = ki.getProfile()
                                profiley = kk.getProfile()
				profilez = kc.getProfile()
                                string = profile.displayName
				stringx = profilex.displayName
				stringy = profiley.displayName
				stringz = profilez.displayName
				cl.sendText(msg.to,string)
				ki.sendText(msg.to,stringx)
				kk.sendText(msg.to,stringy)
				kc.sendText(msg.to,stringz)
	    elif msg.text in ["Key","help","Help"]:
	                    cl.sendText(msg.to,helpMessage)
	    elif msg.text in ["Public menu"]:
	                    cl.sendText(msg.to,helpPublic)
	    elif msg.text in ["Staff menu"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
	                    cl.sendText(msg.to,helpStaff)
	    elif msg.text in ["Admin menu"]:
		if msg.from_ in admin or msg.from_ in wait["admin"]:
	                    cl.sendText(msg.to,helpAdmin)
	    elif msg.text in ["Owner menu"]:
                if msg.from_ in admin:
	                    cl.sendText(msg.to,helpOwner)
            elif "Gn:" in msg.text:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
	                if msg.toType == 2:
	                    X = cl.getGroup(msg.to)
	                    X.name = msg.text.replace("Gn:","")
	                    cl.updateGroup(X)
	                else:
        	            cl.sendText(msg.to,"It can't be used besides the group.")
	    elif "Invitemeto:" in msg.text:
		if msg.from_ in admin:
			grup= msg.text.replace("Invitemeto:","")
			get = cl.getGroup(grup)
	                cl.findAndAddContactsByMid(msg.from_)
			cl.inviteIntoGroup(grup,[msg.from_])
            elif "Undang:" in msg.text:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
	                midd = msg.text.replace("undang:","")
	                ki.findAndAddContactsByMid(midd)
	                ki.inviteIntoGroup(msg.to,[midd])
	    elif msg.text in ["Gcreator"]:
		ginfo = cl.getGroup(msg.to)
		gc = ginfo.creator.mid
		msg.contentType = 13
		msg.contentMetadata = {'mid': gc}
		cl.sendMessage(msg)
	    elif msg.text in ["Owner"]:
		owner = "uda265efc942337e2f436927df04acdd7"
		msg.contentType = 13
		msg.contentMetadata = {'mid': owner}
		cl.sendMessage(msg)
		cl.sendText(msg.to,"Itu owner Saya ^_^")
	    elif msg.text in ["Stafflist"]:
		if msg.from_ in admin:
                        print "list Staff[OK]"
                        if wait["GC"] == {}:
                            cl.sendText(msg.to,"belum ada staff")
                        else:
                            cl.sendText(msg.to,"Sedang prosess..")
                            mc = ""
                            for mi_d in wait["GC"]:
                                mc += "â•‘â• â‚Í¡ÍœðŸŒŸâž£" +cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,"â•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•\nâ•‘â•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•\nâ•‘â• â‚âž£STAFFLIST\nâ•‘â•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•\nâ•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•\n" + mc + "\nTotal staff [" + str(len(wait["GC"])) +"] !")
                else:
                        return
            elif msg.text in ["Me"]:
	                msg.contentType = 13
	                msg.contentMetadata = {'mid': msg.from_}
	                cl.sendMessage(msg)
            elif msg.text in [ "Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Cancel"]:
                if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
                	if msg.toType == 2:
                	    X = cl.getGroup(msg.to)
                	    if X.invitee is not None:
                	        gInviMids = [contact.mid for contact in X.invitee]
                	        cl.cancelGroupInvitation(msg.to, gInviMids)
                	    else:
                	        if wait["lang"] == "JP":
                	            cl.sendText(msg.to,"No one is inviting")
                	        else:
                	            cl.sendText(msg.to,"Sorry, nobody absent")
                	else:
                	    if wait["lang"] == "JP":
                	        cl.sendText(msg.to,"Can not be used outside the group")
                	    else:
                	        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Buka"]:
                if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
                	if msg.toType == 2:
                	    X = cl.getGroup(msg.to)
                	    X.preventJoinByTicket = False
                	    cl.updateGroup(X)
                	    if wait["lang"] == "JP":
                	        cl.sendText(msg.to,"Done")
                	    else:
                	        cl.sendText(msg.to,"already open")
                	else:
                	    if wait["lang"] == "JP":
                	        cl.sendText(msg.to,"Can not be used outside the group")
                	    else:
                        	cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tutup"]:
                if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
                	if msg.toType == 2:
                	    X = cl.getGroup(msg.to)
                	    X.preventJoinByTicket = True
                	    cl.updateGroup(X)
                	    if wait["lang"] == "JP":
                	        cl.sendText(msg.to,"Done")
                	    else:
                	        cl.sendText(msg.to,"already close")
                	else:
                	    if wait["lang"] == "JP":
                	        cl.sendText(msg.to,"Can not be used outside the group")
                	    else:
                	        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Gid" in  msg.text:
                	cl.sendText(msg.to,msg.to)
	    elif 'Myid' in msg.text:
		cl.sendText(msg.to,msg.from_)
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome,wc,Wc,Wb,welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
            elif "Sc:" in msg.text:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
	                mmid = msg.text.replace("Sc:","")
	                msg.contentType = 13
	                msg.contentMetadata = {"mid":mmid}
	                cl.sendMessage(msg)
            elif msg.text in ["Bicara"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
	                if wait["contact"] == True:
	                    if wait["lang"] == "JP":
	                        cl.sendText(msg.to,"Already off")
	                    else:
	                        cl.sendText(msg.to,"done")
	                else:
	                    wait["contact"] = True
	                    if wait["lang"] == "JP":
	                        cl.sendText(msg.to,"Unmuted")
	                    else:
	                        cl.sendText(msg.to,"done")
            elif msg.text in ["Diam"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
	                if wait["contact"] == False:
	                    if wait["lang"] == "JP":
	                        cl.sendText(msg.to,"Already mute")
	                    else:
	                        cl.sendText(msg.to,"done ")
	                else:
	                    wait["contact"] = False
	                    if wait["lang"] == "JP":
	                        cl.sendText(msg.to,"Muted")
	                    else:
	                        cl.sendText(msg.to,"done")
	    elif msg.text in ["Protectqr on"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
			if wait ["lOn"][msg.to] == True:
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Already on")
				else:
					cl.sendText(msg.to,"Done")
			else:
				wait["lOn"][msg.to] = True
				with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Turn on")
				else:
					cl.sendText(msg.to,"Done")
		else:
			cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Protectqr off"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
			if wait["lOn"][msg.to] == False:
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Already off")
				else:
					cl.sendText(msg.to,"Done")
			else:
				wait["lOn"][msg.to] = False
				with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Turn off")
				else:
					cl.sendText(msg.to,"Done")
		else:
			cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Protectinvite on"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
			if wait ["cOn"][msg.to] == True:
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Already on")
				else:
					cl.sendText(msg.to,"Done")
			else:
				wait["cOn"][msg.to] = True
				with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Turn on")
				else:
					cl.sendText(msg.to,"Done")
		else:
			cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Protectinvite off"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
			if wait["cOn"][msg.to] == False:
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Protection Cancel close")
				else:
					cl.sendText(msg.to,"Berhasil")
			else:
				wait["cOn"][msg.to] = False
				with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Turn off")
				else:
					cl.sendText(msg.to,"Done")
		else:
			cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Protection on"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
			if wait ["pOn"][msg.to] == True:
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Protection Aktif")
				else:
					cl.sendText(msg.to,"Aktif")
			else:
				wait["pOn"][msg.to] = True
				with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Turn on")
				else:
					cl.sendText(msg.to,"Done")
		else:
			cl.sendText(msg.to,"Admins or Staffs permission required.")
	    elif msg.text in ["Protection off"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
			if wait["pOn"][msg.to] == False:
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Protection close")
				else:
					cl.sendText(msg.to,"Berhasil")
			else:
				wait["pOn"][msg.to] = False
				with open('st2__b.json','w') as fp:
                                        json.dump(wait, fp, sort_keys=True, indent=4)
				if wait["lang"] == "JP":
					cl.sendTexts(msg.to,"Turn off")
				else:
					cl.sendText(msg.to,"Done")
		else:
			cl.sendText(msg.to,"Admins or Staffs permission required.")
            elif msg.text in ["Join on"]:
		if msg.from_ in admin:
	                if wait["autoJoin"] == True:
	                    if wait["lang"] == "JP":
        	                cl.sendText(msg.to,"already on")
        	            else:
        	                cl.sendText(msg.to,"done")
        	        else:
       		            wait["autoJoin"] = True
        	            if wait["lang"] == "JP":
                	        cl.sendText(msg.to,"already on")
                	    else:
                	        cl.sendText(msg.to,"done")
            elif msg.text in ["Join off"]:
		if msg.from_ in admin:
	                if wait["autoJoin"] == False:
	                    if wait["lang"] == "JP":
	                        cl.sendText(msg.to,"already off")
	                    else:
	                        cl.sendText(msg.to,"done")
	                else:
	                    wait["autoJoin"] = False
	                    if wait["lang"] == "JP":
	                        cl.sendText(msg.to,"already off")
	                    else:
	                        cl.sendText(msg.to,"done")
            elif msg.text in ["Leave on"]:
	                if wait["leaveRoom"] == True:
	                    if wait["lang"] == "JP":
	                        cl.sendText(msg.to,"already on")
	                    else:
	                        cl.sendText(msg.to,"done")
	                else:
	                    wait["leaveRoom"] = True
	                    if wait["lang"] == "JP":
	                        cl.sendText(msg.to,"done")
	                    else:
	                        cl.sendText(msg.to,"ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¦ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂºÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¥ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¼ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â£ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡")
            elif msg.text in ["Leave off"]:
		if msg.from_ in admin:
	                if wait["leaveRoom"] == False:
	                    if wait["lang"] == "JP":
	                        cl.sendText(msg.to,"already off")
	                    else:
	                        cl.sendText(msg.to,"done")
	                else:
	                    wait["leaveRoom"] = False
	                    if wait["lang"] == "JP":
	                        cl.sendText(msg.to,"done")
	                    else:
	                        cl.sendText(msg.to,"already")
	    elif msg.text in ["Protection"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
			if wait["cOn"] and wait["lOn"] and wait["pOn"] == True:
				cl.sendText(msg.to,"Already Protected")
			else:
				wait ["cOn"][msg.to] = True
				wait ["lOn"][msg.to] = True
				wait ["pOn"][msg.to] = True
				with open('st2__b.json','w') as fp:
                                      json.dump(wait, fp, sort_keys=True, indent=4)
				cl.sendText(msg.to,"PROTECTION ALL GROUP AKTIF")
	    elif msg.text in ["Unprotect"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
			if wait["cOn"] and wait["lOn"] and wait["pOn"] == False:
	                        cl.sendText(msg.to,"Already Protected")
	                else:
	                        wait ["cOn"][msg.to] = False
	                        wait ["lOn"][msg.to] = False
	                        wait ["pOn"][msg.to] = False
				with open('st2__b.json','w') as fp:
                                      json.dump(wait, fp, sort_keys=True, indent=4)
	                        cl.sendText(msg.to,"Berhasil")
            elif msg.text in ["Set"]:
	      if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
                md = ""
  	        if wait["cOn"][msg.to] == True and wait["lOn"][msg.to] == True and wait["pOn"][msg.to] == True: md+="Terlindungi\n\n"
		else: md+="Berbahaya\n\n"
		if wait["cOn"][msg.to] == True: md+="Cancel [Aktif]\n"
		else: md+="Cancel [Close]\n"
		if wait["pOn"][msg.to] == True: md+="Protect [Aktif]\n"
		else: md+="Protect [Close]\n"
		if wait["lOn"][msg.to] == True: md+="Qr [Aktif]\n"
		else: md+="Qr [Close]\n"
                if wait["contact"] == True: md+="Bicara [Aktif]\n"
                else: md+="Bicara [Close]\n"
                if wait["autoJoin"] == True: md+="Join [Aktif]\n"
                else: md +="Join [Close]\n"
                if wait["leaveRoom"] == True: md+="Leave [Aktif]\n"
                else: md+="Leave [Close]\n"
                if wait["timeline"] == True: md+="Share [Aktif]\n"
                else:md+="Share [Close]\n"
                if wait["autoAdd"] == True: md+="Add [Aktif]\n"
                else:md+="Add [Close]\n"
                cl.sendText(msg.to,"SETTINGS GROUP\n" + md)
            elif msg.text in ["Glist"]:
		if msg.from_ in admin:
	                gid = cl.getGroupIdsJoined()
	                h = ""
			jml = 0
	                for i in gid:
	                    h += "✧ [%s]\n[%s]\n\n" % (cl.getGroup(i).name,i)
			    jml += 1
	                cl.sendText(msg.to,"Groups : \n" + h + "\n [TOTAL GROUPS] " + str(jml) + " groups")
            elif msg.text in ["Tolak"]:
		if msg.from_ in admin:
                	gid = cl.getGroupIdsInvited()
                	for i in gid:
                	    cl.rejectGroupInvitation(i)
                	if wait["lang"] == "JP":
                	    cl.sendText(msg.to,"All invitations have been refused")
                	else:
                	    cl.sendText(msg.to,"ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¦ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¹ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â»ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂºÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¥ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¦ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¾ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¯ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â·ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â£ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡")
            elif msg.text in ["Add on"]:
		if msg.from_ in admin:
	                if wait["autoAdd"] == True:
	                    if wait["lang"] == "JP":
	                        cl.sendText(msg.to,"already on")
	                    else:
	                        cl.sendText(msg.to,"done")
	                else:
	                    wait["autoAdd"] = True
	                    if wait["lang"] == "JP":
	                        cl.sendText(msg.to,"done")
	                    else:
	                        cl.sendText(msg.to,"ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¦ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂºÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¥ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¼ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â£ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡")
            elif msg.text in ["Add off"]:
		if msg.from_ in admin:
	                if wait["autoAdd"] == False:
        	            if wait["lang"] == "JP":
        	                cl.sendText(msg.to,"already off")
        	            else:
        	                cl.sendText(msg.to,"done")
        	        else:
        	            wait["autoAdd"] = False
        	            if wait["lang"] == "JP":
        	                cl.sendText(msg.to,"done")
        	            else:
        	                cl.sendText(msg.to,"ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¦ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂºÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¥ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¦ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¦ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â£ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Message"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â£ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡\n\n" + wait["message"])
            elif msg.text in ["Getqr"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
	                if msg.toType == 2:
	                    x = cl.getGroup(msg.to)
	                    if x.preventJoinByTicket == True:
	                        x.preventJoinByTicket = False
	                        cl.updateGroup(x)
	                    gurl = cl.reissueGroupTicket(msg.to)
	                    cl.sendText(msg.to,"line://ti/g/" + gurl)
	                else:
	                    if wait["lang"] == "JP":
	                        cl.sendText(msg.to,"Can't be used outside the group")
	                    else:
	                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------------------------------
	    elif msg.text in ["Team @join"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
			if msg.toType == 2:
				X = cl.getGroup(msg.to)
				X.preventJoinByTicket = False
				cl.updateGroup(X)
				Ti = cl.reissueGroupTicket(msg.to)
				ki.acceptGroupInvitationByTicket(msg.to,Ti)
				kk.acceptGroupInvitationByTicket(msg.to,Ti)
				kc.acceptGroupInvitationByTicket(msg.to,Ti)
				X.preventJoinByTicket = True
				cl.updateGroup(X)
		return
            elif msg.text in ["Team @bye"]:
	     if msg.from_ in admin or msg.from_ in wait["admin"]:
                if msg.toType == 2:
                    try:
			cl.sendText(msg.to,"Bye~Bye")
			cl.leaveGroup(msg.to)
			ki.leaveGroup(msg.to)
			kk.leaveGroup(msg.to)
			kc.leaveGroup(msg.to)
                    except:
			ki.leaveGroup(msg.to)
			kk.leaveGroup(msg.to)
			kc.leaveGroup(msg.to)
#-----------------------------------------------
	    elif msg.text in ["About"]:
		cr = "uc77fd25b59f6e563d84f1334f3fed10b"
		msg.contentType = 13
		msg.contentMetadata = {'mid': cr}
		cl.sendMessage(msg)
		ki.sendText(msg.to,"Itu Pembuat Saya")
	    elif "Mid @" in msg.text:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
			cek = msg.text.replace("Mid @","")
			midcek = cek.rstrip(' ')
			gs = cl.getGroup(msg.to)
			anu = ""
			for g in gs.members:
				midcek == g.displayName
				if midcek == g.displayName:
					anu = g.mid
			if midcek == midcek:
				try:
					cl.sendText(msg.to,"Name= " + midcek + "\n" + "Mid=" + anu)
				except:
					pass
	    elif "Admin on @" in msg.text :
		if msg.from_ in admin:
				target = []
                        	key = eval(msg.contentMetadata["MENTION"])
                        	key["MENTIONEES"][0]['M']
                		for s in key["MENTIONEES"]:
		                      target.append(s['M'])
                                for targets in target:
					if targets not in wait["blacklist"]:
                                                if targets in wait["admin"]:
                                                        cl.sendText(msg.to,"Sudah terdaftar")
                                                else:
                                                        wait["admin"][targets] = True
                                                        with open('st2__b.json','w') as fp:
                                                                json.dump(wait, fp, sort_keys=True, indent=4)
                                                        cl.sendText(msg.to,"Berhasil")
                                        else:
                                                cl.sendText(msg.to,"Blacklist detected")
                                                return
	    elif "Unadmin on @" in msg.text:
                if msg.from_ in admin:
                        if msg.toType == 2:
				target = []
                        	key = eval(msg.contentMetadata["MENTION"])
                        	key["MENTIONEES"][0]['M']
        		        for s in key["MENTIONEES"]:
		                       target.append(s['M'])
				for targets in target:
                                                if targets in wait["admin"]:
                                                        del wait["admin"][targets]
                                                        with open('st2__b.json', 'w') as fp:
                                                               json.dump(wait, fp, sort_keys=True, indent=4)
                                                        cl.sendText(msg.to,"Sudah terhapus")
                                                else:
                                                        cl.sendText(msg.to,"Not in admin")
	    elif "Bot on @" in msg.text:
		if msg.from_ in admin:
                                target = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]['M']
                                for s in key["MENTIONEES"]:
                                      target.append(s['M'])
                                for targets in target:
                                        if targets not in wait["blacklist"]:
                                                if targets in wait["listbot"]:
                                                        cl.sendText(msg.to,"Sudah terdaftar")
                                                else:
                                                        wait["listbot"][targets] = True
                                                        with open('st2__b.json','w') as fp:
                                                                json.dump(wait, fp, sort_keys=True, indent=4)
                                                        cl.sendText(msg.to,"Berhasil")
                                        else:
                                                cl.sendText(msg.to,"Blacklist detected")
                                                return
	    elif "Unbot on @" in msg.text:
		if msg.from_ in admin:
                        if msg.toType == 2:
                                target = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]['M']
                                for s in key["MENTIONEES"]:
                                       target.append(s['M'])
                                for targets in target:
                                                if targets in wait["listbot"]:
                                                        del wait["listbot"][targets]
                                                        with open('st2__b.json', 'w') as fp:
                                                               json.dump(wait, fp, sort_keys=True, indent=4)
                                                        cl.sendText(msg.to,"Terhapus")
                                                else:
                                                        cl.sendText(msg.to,"Not in bots")
	    elif "Staff on @" in msg.text:
		if msg.from_ in admin or msg.from_ in wait["admin"]:
                                target = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]['M']
                                for s in key["MENTIONEES"]:
                                      target.append(s['M'])
                                for targets in target:
                                        if targets not in wait["blacklist"]:
                                                if targets in wait["GC"]:
                                                        cl.sendText(msg.to,"Sudah terdaftar")
                                                else:
                                                        wait["GC"][targets] = True
                                                        with open('st2__b.json','w') as fp:
                                                                json.dump(wait, fp, sort_keys=True, indent=4)
                                                        cl.sendText(msg.to,"Berhasil")
                                        else:
                                                cl.sendText(msg.to,"Blacklist detected")
                                                return
	    elif "Unstaff on @" in msg.text:
		if msg.from_ in admin or msg.from_ in wait["admin"]:
                        if msg.toType == 2:
                                target = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]['M']
                                for s in key["MENTIONEES"]:
                                       target.append(s['M'])
                                for targets in target:
                                                if targets in wait["GC"]:
                                                        del wait["GC"][targets]
                                                        with open('st2__b.json', 'w') as fp:
                                                               json.dump(wait, fp, sort_keys=True, indent=4)
                                                        cl.sendText(msg.to,"Sudah terhapus")
                                                else:
                                                        cl.sendText(msg.to,"Not in staff")
	    elif "1clone @" in msg.text:
		if msg.from_ in admin:
			if msg.toType == 2:
				name = msg.text.replace("1clone @","")
                                nametarget = name.rstrip(' ')
                                gs = cl.getGroup(msg.to)
                                target = []
				for g in gs.members:
                                        if nametarget == g.displayName:
						target.append(g.mid)
                                if target == []:
                                        cl.sendText(msg.to,"Not found")
                                else:
                                        for targets in target:
						try:
							cl.clonePicture(targets)
							cl.sendText(msg.to,"Berhasil")
						except Exception as e:
							cl.sendText(msg.to,str(e))
	    elif "2clone @" in msg.text:
                if msg.from_ in admin:
                        if msg.toType == 2:
                                name = msg.text.replace("2clone @","")
                                nametarget = name.rstrip(' ')
                                gs = ki.getGroup(msg.to)
                                target = []
                                for g in gs.members:
                                        if nametarget == g.displayName:
                                                target.append(g.mid)
                                if target == []:
                                        ki.sendText(msg.to,"Not found")
                                else:
                                        for targets in target:
                                                try:
                                                        ki.clonePicture(targets)
                                                        ki.sendText(msg.to,"Berhasil")
                                                except Exception as e:
                                                        ki.sendText(msg.to,str(e))
	    elif "3clone @" in msg.text:
                if msg.from_ in admin:
                        if msg.toType == 2:
                                name = msg.text.replace("3clone @","")
                                nametarget = name.rstrip(' ')
                                gs = kk.getGroup(msg.to)
                                target = []
                                for g in gs.members:
                                        if nametarget == g.displayName:
                                                target.append(g.mid)
                                if target == []:
                                        kk.sendText(msg.to,"Not found")
                                else:
                                        for targets in target:
                                                try:
                                                        kk.clonePicture(targets)
                                                        kk.sendText(msg.to,"Berhasil")
                                                except Exception as e:
                                                        kk.sendText(msg.to,str(e))
	    elif "4clone @" in msg.text:
                if msg.from_ in admin:
                        if msg.toType == 2:
                                name = msg.text.replace("4clone @","")
                                nametarget = name.rstrip(' ')
                                gs = kc.getGroup(msg.to)
                                target = []
				for g in gs.members:
                                        if nametarget == g.displayName:
                                                target.append(g.mid)
                                if target == []:
                                        kc.sendText(msg.to,"Not found")
                                else:
                                        for targets in target:
                                                try:
                                                        kc.clonePicture(targets)
                                                        kc.sendText(msg.to,"Berhasil")
                                                except Exception as e:
                                                        kk.sendText(msg.to,str(e))
	    elif "5clone @" in msg.text:
                if msg.from_ in admin:
                        if msg.toType == 2:
                                name = msg.text.replace("5clone @","")
                                nametarget = name.rstrip(' ')
                                gs = ka.getGroup(msg.to)
                                target = []
				for g in gs.members:
                                        if nametarget == g.displayName:
                                                target.append(g.mid)
                                if target == []:
                                        ka.sendText(msg.to,"Not found")
                                else:
                                        for targets in target:
                                                try:
                                                        ka.clonePicture(targets)
                                                        ka.sendText(msg.to,"Berhasil")
                                                except Exception as e:
                                                        ka.sendText(msg.to,str(e))
	    elif "6clone @" in msg.text:
                if msg.from_ in admin:
                        if msg.toType == 2:
                                name = msg.text.replace("6clone @","")
                                nametarget = name.rstrip(' ')
                                gs = kb.getGroup(msg.to)
                                target = []
				for g in gs.members:
                                        if nametarget == g.displayName:
                                                target.append(g.mid)
                                if target == []:
                                        kb.sendText(msg.to,"Not found")
                                else:
                                        for targets in target:
                                                try:
                                                        kb.clonePicture(targets)
                                                        kb.sendText(msg.to,"Berhasil")
                                                except Exception as e:
                                                        kb.sendText(msg.to,str(e))
	    elif "7clone @" in msg.text:
                if msg.from_ in admin:
                        if msg.toType == 2:
                                name = msg.text.replace("7clone @","")
                                nametarget = name.rstrip(' ')
                                gs = kd.getGroup(msg.to)
                                target = []
				for g in gs.members:
                                        if nametarget == g.displayName:
                                                target.append(g.mid)
                                if target == []:
                                        kd.sendText(msg.to,"Not found")
                                else:
                                        for targets in target:
                                                try:
                                                        kd.clonePicture(targets)
                                                        kd.sendText(msg.to,"Berhasil")
                                                except Exception as e:
                                                        kd.sendText(msg.to,str(e))
	    elif "Wl on @" in msg.text:
                if msg.from_ in admin:
                        if msg.toType == 2:
					target = []
		                        key = eval(msg.contentMetadata["MENTION"])
                		        key["MENTIONEES"][0]['M']
                        		for s in key["MENTIONEES"]:
                        		     target.append(s['M'])
                                        for targets in target:
                                            if targets not in wait["blacklist"]:
						if targets in wait["whitelist"]:
                                                        cl.sendText(msg.to,"already")
                                                else:
							wait["whitelist"][targets] = True
                                                        with open('st2__b.json','w') as fp:
                                                                json.dump(wait, fp, sort_keys=True, indent=4)
                                                        cl.sendText(msg.to,"Sukses")
                                            else:
                                                cl.sendText(msg.to,"Blacklist detected")
						return
	    elif "Unwl on @" in msg.text:
                if msg.from_ in admin:
                        if msg.toType == 2:
					target = []
                        		key = eval(msg.contentMetadata["MENTION"])
                		        key["MENTIONEES"][0]['M']
                		        for s in key["MENTIONEES"]:
		                             target.append(s['M'])
                                        for targets in target:
						if targets in wait["whitelist"]:
							if targets not in admin and targets not in wait["admin"] and targets not in wait["GC"]:
								del wait["whitelist"][targets]
        	                                                with open('st2__b.json', 'w') as fp:
                	                                               json.dump(wait, fp, sort_keys=True, indent=4)
                	                                        cl.sendText(msg.to,"Deleted")
							else:
								cl.sendText(msg.to,"Cannot Unwhite this user(s)")
                                                else:
                                                        cl.sendText(msg.to,"Not in Whitelist")
            elif "Ban on @" in msg.text:
       		if msg.from_ in admin or msg.from_ in wait["admin"]:
			if msg.toType == 2:
					target = []
                        		key = eval(msg.contentMetadata["MENTION"])
        		                key["MENTIONEES"][0]['M']
	        	                for s in key["MENTIONEES"]:
                        		     target.append(s['M'])
					for targets in target:
					    nuked = admin+[mid]+[Amid]+[Bmid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
					    if targets not in nuked and targets not in wait["whitelist"]:
						if targets in wait["blacklist"]:
							cl.sendText(msg.to,"Sudah terdaftar")
						else:
							wait["blacklist"][targets] = True
							with open('st2__b.json','w') as fp:
		                                                json.dump(wait, fp, sort_keys=True, indent=4)
							cl.sendText(msg.to,"Berhasil")
					    else:
						cl.sendText(msg.to,"Cannot black white user(s)")
						return
	    elif msg.text in ["Killban"]:
      	     if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group = ki.getGroup(msg.to)
                    group = kk.getGroup(msg.to)
                    group = kc.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        kc.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Nothing blacklist users in group again")
		    return
	    elif msg.text in ["Adminlist"]:
                if msg.from_ in admin:
                        print "list admin[OK]"
                        if wait["admin"] == {}:
                            cl.sendText(msg.to,"Belum ada admin")
                        else:
                            cl.sendText(msg.to,"Loading....")
                            mc = ""
                            for mi_d in wait["admin"]:
                                mc += "✧" +cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,"Admin : \n" + mc + "\n[Total admin] [" + str(len(wait["admin"])) +"] !")
                else:
                        return
	    elif msg.text in ["Whitelist"]:
                if msg.from_ in admin:
			print "whitelist[OK]"
                        if wait["whitelist"] == {}:
                            cl.sendText(msg.to,"Belum Ada Whitelist")
                        else:
                            cl.sendText(msg.to,"Loading....")
                            mc = ""
                            for mi_d in wait["whitelist"]:
                                mc += "✧" +cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,"White List : \n" + mc + "\nTotal whitelist [" + str(len(wait["whitelist"])) +"] !")
                else:
                        return
	    elif msg.text in ["Banlist"]:
		if msg.from_ in admin:
			print "blacklist[OK]"
	                if wait["blacklist"] == {}:
	                    cl.sendText(msg.to,"Belum ada Banlist")
	                else:
	                    cl.sendText(msg.to,"Blacklist user")
	                    mc = ""
	                    for mi_d in wait["blacklist"]:
	                        mc += "✧" +cl.getContact(mi_d).displayName + "\n"
			    cl.sendText(msg.to,"Banlist : \n" + mc + "\n [TOTAL BANLIST] [" + str(len(wait["blacklist"])) +"] ")
		else:
			return
	    elif msg.text in ["Botlist"]:
		if msg.from_ in admin:
			print "botlist[OK]"
	                if wait["listbot"] == {}:
	                    cl.sendText(msg.to,"Belum ada Banlist")
	                else:
	                    cl.sendText(msg.to,"Loading....")
	                    mc = ""
	                    for mi_d in wait["blacklist"]:
	                        mc += "✧" +cl.getContact(mi_d).displayName + "\n"
			    cl.sendText(msg.to,"BOTLIST : \n" + mc + "\n [TOTAL BOT] [" + str(len(wait["blacklist"])) +"] ")

	    elif "Unban on @" in msg.text:
		if msg.from_ in admin or msg.from_ in wait["admin"]:
			if msg.toType == 2:
				target = []
                        	key = eval(msg.contentMetadata["MENTION"])
                        	key["MENTIONEES"][0]['M']
                	        for s in key["MENTIONEES"]:
        	                     target.append(s['M'])
				for targets in target:
						if targets in wait["blacklist"]:
							del wait["blacklist"][targets]
							with open('st2__b.json', 'w') as fp:
		 	                                       json.dump(wait, fp, sort_keys=True, indent=4)
							cl.sendText(msg.to,"Sudah di hapus")
						else:
							cl.sendText(msg.to,"Not in blacklist")
							return
            elif "Bunuh " in msg.text:
                  if msg.from_ in admin or msg.from_ in wait["admin"]:
			targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]['M']
                        for s in key["MENTIONEES"]:
                             targets.append(s['M'])
                        for target in targets:
				if target in admin and target in wait["admin"]:
					pass
				else:
				    kicker = [ki,kk,kc,ka,kb,kd,ke]
				    random.choice(kicker).kickoutFromGroup(msg.to,[target])
			return
#-----------------------------------------------
            elif "Bot Say" in msg.text:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
				bctxt = msg.text.replace("Bot Say","")
				cl.sendText(msg.to,(bctxt))
				ka.sendText(msg.to,(bctxt))
				ke.sendText(msg.to,(bctxt))
				ke.sendText(msg.to,(bctxt))
				ke.sendText(msg.to,(bctxt))
				ka.sendText(msg.to,(bctxt))
#==================================================
            elif msg.text in ["Tag kabeh","Tagall","Tag"]:
                if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
                              group = cl.getGroup(msg.to)
                              nama = [contact.mid for contact in group.members]
                              nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                              if jml <= 100:
                                 mention(msg.to, nama)
                              if jml > 100 and jml < 200:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 mention(msg.to, nm1)
                                 for j in range (100, len(nama)-1):
                                        nm2 += [nama[j]]
                                 mention(msg.to, nm2)
                              if jml > 200 and jml < 300:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 mention(msg.to, nm1)
                                 for j in range (100, 199):
                                        nm2 += [nama[j]]
                                 mention(msg.to, nm2)
                                 for k in range (200, len(nama)-1):
                                        nm3 += [nama[k]]
                                 mention(msg.to, nm3)
                              if jml > 300 and jml < 400:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 mention(msg.to, nm1)
                                 for j in range (100, 199):
                                        nm2 += [nama[j]]
                                 mention(msg.to, nm2)
                                 for k in range (200, 299):
                                        nm3 += [nama[k]]
                                 mention(msg.to, nm3)
                                 for l in range (300, len(nama)-1):
                                     nm4 += [nama[l]]
                                 mention(msg.to, nm4)
                              cnt = Message()
                              cnt.text = "Hasil Tag : "+str(jml)
                              cnt.to = msg.to
                              cl.sendText(msg.to,"TAGALL SUCCESS")
                              cl.sendMessage(cnt)
#-----------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Bisa Jadi","Mungkin")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#-----------------------------------------------
            elif 'music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
#-----------------------------------------------
            elif 'ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
#------------------------------------------------------
            elif "Tr-id " in msg.text:
                nk0 = msg.text.replace("Tr-id ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'id')
                cl.sendText(msg.to,str(trans))
            elif "Tr-th " in msg.text:
                nk0 = msg.text.replace("Tr-th ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'th')
                cl.sendText(msg.to,str(trans))
#----------------------------------------------
            elif "youtube " in msg.text.lower():
                 query = msg.text.lower().replace("youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                             cl.sendText(msg.to,'Judul : ' + a['title'] + '\nLink : ' + 'http://www.youtube.com' + a['href'])
#-----------------------------------------------
            elif msg.text in ["Sp"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
	                start = time.time()
	                cl.sendText(msg.to, "Sedang Prosess...")
	                elapsed_time = time.time() - start
	                kc.sendText(msg.to, "%sseconds" % (elapsed_time))
#-----------------------------------------------------------------
            elif msg.text in ["Clear"]:
		if msg.from_ in admin or msg.from_ in wait["GC"] or msg.from_ in wait["admin"]:
	                if msg.toType == 2:
	                    group = cl.getGroup(msg.to)
	                    gMembMids = [contact.mid for contact in group.invitee]
	                    for _mid in gMembMids:
				if _mid in admin:
					pass
				else:
		                        cl.cancelGroupInvitation(msg.to,[_mid])
	                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif msg.text in ["Cleanse"]:
		if msg.from_ in admin:
	                if msg.toType == 2:
		                kk.sendText(msg.to,"Ready")
				gid = msg.to
				group = kk.getGroups([gid])
				if len(group) > 0:
					totalMember = group[0].members
					cl.sendText(msg.to,"Your group will Clean")
					for x in range(len(totalMember)):
		  	 		        bots = [Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
						if totalMember[x].mid not in admin and totalMember[x].mid not in bots and totalMember[x].mid not in wait["listbot"] and totalMember[x].mid not in wait["whitelist"] and totalMember[x].mid not in wait ["admin"]:
							random.choice(KAC).kickoutFromGroup(msg.to,[totalMember[x].mid])
				cl.sendText(msg.to,"Succes clean group")
            elif 'Cleanse' in msg.text:
	        bots = [Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
                if msg.from_ not in admin and msg.from_ not in wait["GC"] and msg.from_ not in wait["admin"] and msg.from_ not in bots:
                        if msg.toType == 2:
				wait["blacklist"][msg.from_] = True
				with open('st2__b.json','w') as fp:
	                                 json.dump(wait, fp, sort_keys=True, indent=4)
                                random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
		else:
			pass
            elif 'Mayhem' in msg.text:
	        bots = [Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
                if msg.from_ not in admin and msg.from_ not in wait["GC"] and msg.from_ not in wait["admin"] and msg.from_ not in bots:
                        if msg.toType == 2:
				wait["blacklist"][msg.from_] = True
				with open('st2__b.json','w') as fp:
	                                 json.dump(wait, fp, sort_keys=True, indent=4)
                                random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
			else:
				pass
            elif 'Status:' in msg.text:
	        bots = [Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
                if msg.from_ not in admin and msg.from_ not in wait["GC"] and msg.from_ not in wait["admin"] and msg.from_ not in bots and msg.from_ not in wait["whitelist"]:
                        if msg.toType == 2:
				wait["blacklist"][msg.from_] = True
				with open('st2__b.json','w') as fp:
	                                 json.dump(wait, fp, sort_keys=True, indent=4)
                                random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                else:
                        pass
            elif 'Beli dulu pak' in msg.text:
	        bots = [Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
                if msg.from_ not in admin and msg.from_ not in wait["GC"] and msg.from_ not in wait["admin"] and msg.from_ not in bots:
                        if msg.toType == 2:
				wait["blacklist"][msg.from_] = True
				with open('st2__b.json','w') as fp:
                                               json.dump(wait, fp, sort_keys=True, indent=4)
                                random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                else:
                        pass
            elif 'You Are' in msg.text:
	        bots = [Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
                if msg.from_ not in admin and msg.from_ not in wait["GC"] and msg.from_ not in wait["admin"] and msg.from_ not in bots:
                        if msg.toType == 2:
				wait["blacklist"][msg.from_] = True
				with open('st2__b.json','w') as fp:
	                                   json.dump(wait, fp, sort_keys=True, indent=4)
                                random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                else:
                        pass
            elif 'Not admin' in msg.text:
	        bots = [Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
                if msg.from_ not in admin and msg.from_ not in wait["GC"] and msg.from_ not in wait["admin"] and msg.from_ not in bots:
                        if msg.toType == 2:
				wait["blacklist"][msg.from_] = True
				with open('st2__b.json','w') as fp:
	                                   json.dump(wait, fp, sort_keys=True, indent=4)
                                random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                else:
                        pass
            elif '{"cancel":0,"kick":1}' in msg.text:
	        bots = [Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
                if msg.from_ not in admin and msg.from_ not in wait["GC"] and msg.from_ not in wait["admin"] and msg.from_ not in bots:
                        if msg.toType == 2:
				wait["blacklist"][msg.from_] = True
				with open('st2__b.json','w') as fp:
	                                   json.dump(wait, fp, sort_keys=True, indent=4)
                                random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                else:
                        pass
	    elif '{"cancel"' in msg.text:
	        bots = [Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
                if msg.from_ not in admin and msg.from_ not in wait["GC"] and msg.from_ not in wait["admin"] and msg.from_ not in bots:
                        if msg.toType == 2:
				wait["blacklist"][msg.from_] = True
				with open('st2__b.json','w') as fp:
	                                   json.dump(wait, fp, sort_keys=True, indent=4)
                                random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                else:
                        pass
	    elif '"kick":1}' in msg.text:
	        bots = [Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
                if msg.from_ not in admin and msg.from_ not in wait["GC"] and msg.from_ not in wait["admin"] and msg.from_ not in bots:
                        if msg.toType == 2:
				wait["blacklist"][msg.from_] = True
				with open('st2__b.json','w') as fp:
	                                   json.dump(wait, fp, sort_keys=True, indent=4)
                                random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                else:
                        pass
            elif msg.text in ["Kick on","kick on","kickall","Kickall",".kick on",".kickall"]:
	        bots = [Amid]+[Bmid]+[mid]+[Cmid]+[Dmid]+[Emid]+[Fmid]+[Gmid]
                if msg.from_ not in admin and msg.from_ not in wait["GC"] and msg.from_ not in wait["admin"] and msg.from_ not in bots:
                        if msg.toType == 2:
				wait["blacklist"][msg.from_] = True
				with open('st2__b.json','w') as fp:
	                                   json.dump(wait, fp, sort_keys=True, indent=4)
                                random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                else:
                        pass
            elif msg.text in ["Cek","cek"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "Cek Sider On")
                print "@setview"
            elif msg.text in ["Read","read"]:
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "Yang Sider :v\n[*]"
                        grp = '\n[*] '.join(str(f) for f in dataResult)
                        total = '\n\n[Total] %i [yang terlihat Sider] (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        cl.sendText(msg.to, "Belum ada viewers")
                    print "@viewseen"

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
#thread2 = threading.Thread(target=nameUpdate)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
