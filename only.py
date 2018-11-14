# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import *
from datetime import datetime
from multiprocessing import Pool, Process
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
import pytz, datetime, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from gtts import gTTS
import pafy
import youtube_dl
import html5lib
import ttypes
from googletrans import Translator
from urllib.parse import urlencode
import requests.packages.urllib3.exceptions as urllib3_exceptions
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
    
def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)    
#==============================================================================#
mulai = time.time()

line = LINE("")
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

print ("Login succes ")
lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()
oepoll = OEPoll(line)

welcome = []
responPc = []
autoRespon = []
autoResponImage = []
autoResponPm = []
msg_dict1 = {}
msg_dict = {}
#==============================================================================#
settings = {
    "autoAdd": False,
    "autoJoin": False,
    "contact":False,
    "autoblock": False,
    "autoRespon": False,
    "autoKick": False, 
    "diinvite": " terima kasih sudah invite saya",
    "autoResponImage": False,
    "autoResponPm": False,
    "simiSimi": {},
    "autoLeave": False,
    "autojj": False,
    "leavemsg": False,
    "welcomemsg": False,
    "responPc": False,
    "keluar":"sᴇʟᴀᴍᴀᴛ ᴊᴀʟᴀɴ ....\nsᴇᴍᴏɢᴀ ᴋᴀᴍᴜ ʙᴀɪᴋ2 ᴅɪʟᴜᴀʀ sᴀɴᴀ\nsᴀᴍᴘᴀɪ ᴊᴜᴍᴘᴀ 👌👌👌",
    "autoRead": False,
    "protect": False,
    "qrprotect": False,
    "tag": "Iya, ada apa ka",
    "tag2": "Ada apa kak tag saya",
    "tag3": "Ada apasih ka Pm mulu",
    "detectMention": False,
    "autorejc": False,
    "mention": "Sider mulu sini ka",
    "welcome":"sᴇᴍᴏɢᴀ ʙᴇᴛᴀʜ ʏᴀ...\nsᴀʟᴀᴍ ᴋᴇɴᴀʟ ᴅᴀʀɪ sᴀʏᴀ 😘",
    "responpc": "Tag terus",
    "checkSticker": False,
    "TagMention": False,
    "TagMention2": False,
    "unsendMessage":False,
     "autoBalas": False,
    'wellcome':False,
    'bymsg':{},
    "lang":"JP",
    "autoJoinTicket": {},
    "changeGroupPicture":True,
    "Mute": True,    
    "changePicture": {},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
     "copy": False,
     "status": False,
     "target": {}
    }
}
wait = {
    "Sider":{},
    "limit": 1,
    "Mute": False,
    "unsend":True,
    "timeline":False,
    "selfbot":True,    
    "sukaPost":True,
    "comment1":"» ʜᴇʏ,  ɪᴍ ᴄᴏᴍᴍɪɴɢ 💃\n» ᴀᴜᴛᴏʟɪᴋᴇ ʙʏ: ᴛᴇᴀᴍ ᴅᴋᴢ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ\n» ғᴀᴍɪʟʏ ʙᴏᴛs ᴘʀᴏᴛᴇᴄᴛ\n» ғᴀᴍɪʟʏ sᴇʟғʙᴏᴛ\n» ғᴀᴍɪʟʏ ᴊᴀᴠᴀsᴄʀɪғᴛ ʙᴏᴛ\n\n» ᴡᴇ ᴀʀᴇ ᴘʀᴏᴛᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
    "welcomeOn":False,    
    "lang":"JP",
}
like = {
    "like":True,
    "likeOn":True,
    "liked":True,
    }
    
tikel = {
   'sid':"48198",
   'spkg':"2000000"
   }
   
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
    }
    
contact = line.getProfile()
mybackup = line.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def restart_program(): 
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)    


def waktu(secs):
      mins, secs = divmod(secs,60)
      hours, mins = divmod(mins,60)
      return '%02d : Jam, ♪ %02d : Menit, ♪ %02d : Detik ♪' % (hours, mins, secs)
      
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)
    elif days > 0 and weaks == 0:
        return '%02d Hari %02d Jam %02d Menit %02d Detik' %(days, hours, mins, secs)
    elif days > 0 and weaks > 0:
        return '%02d Minggu %02d Hari %02d Jam %02d Menit %02d Detik' %(weaks, days, hours, mins, secs)
    
def a2():
    now2 = datetime.datetime.now()
    nowT = datetime.datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
        

def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "❨✪❩ ᴅᴋᴢ mentions ❨✪❩ \n\n1. ".format(str(len(mid)))
        textx2 ="╭════════════════╮\n ✍ ᴛᴏᴛᴀʟ {} ᴍᴇᴍʙᴇʀs".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(line.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        jp1 = line.getContact(lineMID).displayName
        line.sendMessage(to, textx2 + "\n ✍ ᴍᴇɴᴛɪᴏɴᴇs ʙʏ : " + jp1 + "\n╰════════════════╯")
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))
 
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╭════════════════╮\n   ❨✪❩ ᴅᴋᴢ mentions ❨✪❩ \n║\n║◍ 1. ".format(str(len(mid)))
        ginfo = line.getGroup(to)

        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "║◍ {}. ".format(str(no))
            else:
                textx += "\n「 Total {} Member 」\n╰════════════════╯".format(str(len(mid)))
        line.sendMessage(to, textx, {'AGENT_NAME':'「 Creator 」', 'AGENT_LINK': 'line://ti/p/~eg_2'.format(line.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + line.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@jeck "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = line.getAllContactIds()
        gid = line.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n🔰 Group : "+str(len(gid))+"\n🔰 Teman : "+str(len(teman))+"\n🔰 Expired : In "+hari+"\n🔰 Version : Saints Bot\n🔰 Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n🔰 Runtime : \n • "+bot
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    myid = line.getProfile().mid
    if myid in nm:
      nm.remove(myid)
    for mm in nm:
      akh = akh + 6
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 7
      akh = akh + 1
      bb += "@nrik "
    aa = (aa[:int(len(aa)-1)])
    text = bb
    try:
       line.sendMessage(to, text, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
       print(error)

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    line.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
        
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item) #Append all the links in the list named 'Links'
            #time.sleep(0.1) #Timer could be used to slow down the request for#image downloads
            page = page[end_content:]
    return items
    
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict1[msg_id]

def atend1():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

    
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                line.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            

#atexit.register(atend)            
            
    
def helpmessage():
    helpMessage = """
╭═══════════════════╮
 ❨✪❩ ɢᴇɴᴇʀᴀʟ ᴄᴏᴍᴍᴀɴᴅ ❨✪❩
╰═══════════════════╯
01.║✍ ᴍᴇ
02.║✍ sᴘ
03.║✍ sᴇᴛ
04.║✍ ᴘᴘ
05.║✍ ɴᴋ:
06.║✍ ɢɪᴅ
07.║✍ ᴋɪᴄᴋ @
08.║✍ ᴠᴋɪᴄᴋ @
09.║✍ ɴᴜᴋᴇ
10.║✍ ɢᴜʀʟ
11.║✍ ʜᴇʟᴘ
12.║✍ ᴍɪᴅ
13.║✍ ᴍɪᴅ @
14.║✍ ᴍᴜsɪᴄ
15.║✍ ᴍᴏᴠɪᴇ
16.║✍ ʀᴇᴊᴇᴄᴛ
17.║✍ ᴄᴀɴᴄᴇʟ
18.║✍ ɢᴘɪᴄᴛ
19.║✍ ᴄᴏᴠᴇʀ
20.║✍ ᴘɪᴄᴛ @
21.║✍ ᴄᴏᴠᴇʀ @
22.║✍ ᴄᴏᴘʏ @
23.║✍ ɢᴄᴀʟʟ
24.║✍ sᴘᴀᴍ
25.║✍ ʙᴀᴄᴋᴜᴘ
26.║✍ ʏᴏᴜᴛᴜʙᴇ
27.║✍ ɪᴍᴀɢᴇ:
28.║✍ ɪɴsᴛᴀɢʀᴀᴍ
29.║✍ ᴋᴀʟᴋᴜʟᴀᴛᴏʀ
30.║✍ ʙʀᴏᴀᴅᴄᴀsᴛ
╭═══════════════════╮
 ❨✪❩  ʀᴇʟᴀᴛᴇᴅ ɢʀᴏᴜᴘ ❨✪❩
╰═══════════════════╯
31.║✍ ʀᴇʙᴏᴏᴛ
32.║✍ ʀᴜɴᴛɪᴍᴇ
33.║✍ ᴀʙᴏᴜᴛ
34.║✍ ᴄʀᴇᴀᴛᴏʀ
35.║✍ ᴍʏɴᴀᴍᴇ
36.║✍ ᴍʏʙɪᴏ
37.║✍ ᴍʏᴠɪᴅ
38.║✍ ɢᴇᴛʙɪᴏ @
39.║✍ ɢᴄʀᴇᴀᴛᴏʀ
40.║✍ ɢɴᴀᴍᴇ
41.║✍ ᴍᴇᴍʟɪsᴛ
42.║✍ ɢʀᴏᴜᴘs
43.║✍ ᴀᴜᴛᴏʟɪᴋᴇ
44.║✍ ʟɪɴᴋ ᴏɴ/ᴏғғ
45.║✍ ɢᴇᴛɴᴀᴍᴇ @
46.║✍ ᴜᴘᴅᴀᴛᴇ ᴘɪᴄᴛ
47.║✍ ɢᴇᴛ ᴄᴏɴᴛᴀᴄᴛ @
48.║✍ ʀᴇᴍᴏᴠᴇᴄʜᴀᴛ
49.║✍ ɢᴇᴛ ᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ
50.║✍ ᴜᴘᴅᴀᴛᴇ ᴘɪᴄᴛ ɢʀᴏᴜᴘ
51.║✍ ᴀʟʟsᴇᴛᴛɪɴɢs ᴍᴏᴅᴇ ᴏɴ
52.║✍ ᴀʟʟsᴇᴛᴛɪɴɢs ᴍᴏᴅᴇ ᴏғғ
53.║✍ ᴛᴀɢ /ʜɪ /ʜᴀɪ /ʜᴇᴍ /ᴅᴋᴢ
╭═══════════════════╮
 ❨✪❩  ᴍɪᴍɪᴄ ᴄᴏᴍᴍᴀɴᴅ ❨✪❩
╰═══════════════════╯
54.║✍ ᴍɪᴍɪᴄᴀᴅᴅ
55.║✍ ᴍɪᴍɪᴄᴅᴇʟ
56.║✍ ᴍɪᴍɪᴄʟɪsᴛ
57.║✍ ᴍɪᴍɪᴄ ᴏɴ/ᴏғғ
╭═══════════════════╮
 ❨✪❩  ᴍᴇᴅɪᴀ ᴄᴏᴍᴍᴀɴᴅ ❨✪❩
╰═══════════════════╯
58.║✍ ʟᴇᴅ (ᴛxᴛ)
59.║✍ ᴘᴏsᴛᴇʀ (ᴛxᴛ)
60.║✍ ғs (ᴛxᴛ)
61.║✍ ᴄᴏʙᴀ (ᴛxᴛ)
62.║✍ ᴀɴᴜ (ᴛxᴛ)
63.║✍ ᴍᴜsɪᴄ (ᴛxᴛ)
64.║✍ ᴋᴏɴᴛᴀᴋ ᴍᴇ
65.║✍ ɪɴғᴏ ᴍᴇ
66.║✍ sᴍᴜʟᴇ (ɪᴅsᴍᴜʟᴇ)
67.║✍ ᴄᴇᴋsᴍᴜʟᴇ (ɪᴅsᴍᴜʟᴇ)
╭═══════════════════╮
 ❨✪❩  sᴇᴛᴛɪɴɢ ɪɴ ʀᴇsᴘᴏɴ ❨✪❩
╰═══════════════════╯
68.║✍ sᴇᴛ ʀᴇsᴘᴏɴ1
69.║✍ ᴄᴇᴋ ʀᴇsᴘᴏɴ1
70.║✍ sᴇᴛ ʀᴇsᴘᴏɴ2
71.║✍ ᴄᴇᴋ ʀᴇsᴘᴏɴ2
72.║✍ sᴇᴛ ʀᴇsᴘᴏɴ3
73.║✍ ᴄᴇᴋ ʀᴇsᴘᴏɴ3
74.║✍ sᴇᴛ ʀᴇsᴘᴏɴᴘᴄ
75.║✍ ᴄᴇᴋ ʀᴇsᴘᴏɴᴘᴄ
76.║✍ sᴇᴛ ᴡᴇʟᴄᴏᴍᴇ 
77.║✍ ᴄᴇᴋ ᴡᴇᴋᴄᴏᴍᴇ
78.║✍ sᴇᴛ ʟᴇᴀᴠᴇᴍsɢ
79.║✍ ᴄᴇᴋ ʟᴇᴀᴠᴇᴍsɢ
80.║✍ sᴇᴛ sɪᴅᴇʀᴛᴇxᴛ
81.║✍ ᴄᴇᴋ sɪᴅᴇʀᴛᴇxᴛ
82.║✍ sᴇᴛ ᴀᴜᴛᴏʟɪᴋᴇ
83.║✍ ᴄᴇᴋ ᴀᴜᴛᴏʟɪᴋᴇ
"""
    return helpMessage
#==============================================================================#


def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                line.sendMessage(op.param1, "ʜᴀʟʟᴏ {} ᴛx ғᴏʀ ᴀᴅᴅ ᴍᴇ\nʙʏ: ᴛᴇᴀᴍ ᴅᴋᴢ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ".format(str(line.getContact(op.param1).displayName)))

        if op.type == 15:
            print ("[ 15 ] MEMBER LEAVE GROUP")
            if settings["leavemsg"] == True:
                contact = line.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                text = "ɢᴏᴏᴅ ʙʏᴇ @!\n{}".format(str(settings["keluar"]))
                sendMentionV2(op.param1, text, [op.param2])
                line.sendImageWithURL(op.param1,image)
          
        if op.type == 17:
          if settings["welcomemsg"] == True:
            if op.param2 in lineMID:
                return
            ginfo = line.getGroup(op.param1)
            contact = line.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            summon(op.param1,[op.param2])
            line.sendMessage(op.param1,"ʜᴀʟʟᴏ ☛ " + line.getContact(op.param2).displayName + "\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ☛ " + str(ginfo.name)+"\n"+(str(settings["welcome"])))
            line.sendImageWithURL(op.param1,image)
            print ("MEMBER JOIN THE GROUP")
           
        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if settings["autoblock"] == True:
                line.sendMessage(op.param1, "Halo {} \nThank yah \nSory akun saya Autoblock ".format(str(line.getContact(op.param1).displayName)))
                line.blockContact(op.param1)
                
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            group = line.getGroup(op.param1)
            if settings["autoJoin"] == True:
                line.acceptGroupInvitation(op.param1)
                
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                line.leaveRoom(op.param1)
        if op.type == 25:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                elif text.lower() == 'help':
                    helpMessage = helpmessage()
                    jp1 = line.getContact(lineMID).displayName
                    line.sendMessage(to,str(helpMessage) + "╭════════════════════╮\n❨✪❩ ᴠɪᴇᴡ sᴇᴛᴛɪɴɢs = sᴇᴛ \n❨✪❩ ᴠɪᴇᴡ ɪɴғᴏ ʙᴏᴛ = ᴀʙᴏᴜᴛ \n❨✪❩ ʜᴇʟᴘᴍᴇssᴀɢᴇ ʙʏ : " + jp1+ "\n╰════════════════════╯\n         ™ ᴛᴇᴀᴍ ᴅᴋᴢ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ™\n")

#==============================================================================#
                elif text.lower() == 'speed' or text.lower() == 'sp':
                    line.sendMessage(to, "progres...")
                    line.sendMessage(to,str(time.time()/1000000000000.0)+" seconds")

                elif text.lower() == 'reboot':
                    line.sendMessage(to, "I'II come back latter")
                    line.sendMessage(to, "Restarted done ♪")
                    restartBot()
                    
                elif text.lower() == 'runtime':
                     eltime = time.time() -mulai
                     van = "╭════════════════════╮\n     Mybot sudah berjalan selama\n     " +waktu(eltime)+"\n╰════════════════════╯"
                     line.sendMessage(to,van)  
                    
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u9922f516e7fac1ea266f55a148e76217"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "____________________________\n❨✪❩ Impormation Selfbot ❨✪❩\n____________________________"
                        ret_ += "\n┃❨✪❩ Line Name : {}".format(contact.displayName)
                        ret_ += "\n┃❨✪❩ Groups : {}".format(str(len(grouplist)))
                        ret_ += "\n┃❨✪❩ Friends : {}".format(str(len(contactlist)))
                        ret_ += "\n┃❨✪❩ Blocked : {}".format(str(len(blockedlist)))
                        ret_ += "\n┃❨✪❩ Version1 : Python3 Update"
                        ret_ += "\n┃❨✪❩ Version2 : Premium server"
                        ret_ += "\n┃❨✪❩ Server : Gnu Linux 48"
                        ret_ += "\n┃❨✪❩ Masa Aktif : 28-09-2018"
                        ret_ += "\n┃❨✪❩ Creator : {}".format(creator.displayName)
                        ret_ += "\n____________________________"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'set' or text.lower() == 'myset':
                    try:
                        ret_ = "╭═════════════════╮\n"
                        ret_ += "  ❨✪❩ sᴇᴛᴛɪɴɢs ᴍʏʙᴏᴛ ❨✪❩\n"
                        ret_ += "╰═════════════════╯\n"
                        if settings["autoAdd"] == True: ret_ += "01.┃ᴀᴜᴛᴏᴀᴅᴅ ᴏɴ \n"
                        else: ret_ += "01.┃ᴀᴜᴛᴏᴀᴅᴅ ᴏғғ \n"
                        if settings["autoblock"] == True: ret_ += "02.┃ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴏɴ \n"
                        else: ret_ += "02.┃ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴏғғ \n"         
                        if settings["contact"] == True: ret_ += "03.┃ᴄᴏɴᴛᴀᴄᴛ ᴏɴ \n"
                        else: ret_ += "03.┃ᴄᴏɴᴛᴀᴄᴛ ᴏғғ \n"
                        if settings["autoJoin"] == True: ret_ += "04.┃ᴀᴜᴛᴏᴊᴏɪɴ ᴏɴ \n"
                        else: ret_ += "04.┃ᴀᴜᴛᴏᴊᴏɪɴ ᴏғғ \n"
                        if settings["mimic"]["status"] == True: ret_ += "05.┃ᴍɪᴍɪᴄ ᴏɴ \n"
                        else: ret_ += "05.┃ᴍɪᴍɪᴄ ᴏғғ \n"
                        if settings["welcomemsg"] == True: ret_+= "06.┃ᴡᴇʟᴄᴏᴍᴇ ᴏɴ \n"
                        else: ret_ +="06.┃ᴡᴇʟᴄᴏᴍᴇ ᴏғғ \n"
                        if settings["leavemsg"] == True: ret_+= "07.┃ʟᴇᴀᴠᴇᴍsɢ ᴏɴ \n"
                        else: ret_ +="07.┃ʟᴇᴀᴠᴇᴍsɢ ᴏғғ \n"                     
                        if settings["autoLeave"] == True: ret_ += "08.┃ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴏɴ \n"
                        else: ret_ += "08.┃ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴏғғ \n"
                        if settings["autoRead"] == True: ret_ += "09.┃ᴀᴜᴛᴏʀᴇᴀᴅ ᴏɴ \n"
                        else: ret_ += "09.┃ᴀᴜᴛᴏʀᴇᴀᴅ ᴏғғ \n"
                        if settings["checkSticker"] == True: ret_ += "10.┃ᴄᴇᴋsᴛɪᴄᴋᴇʀ ᴏɴ \n"
                        else: ret_ += "10.┃ᴄᴇᴋsᴛɪᴄᴋᴇʀ ᴏғғ \n"                     
                        if settings["autoRespon"] == True: ret_ += "11.┃ʀᴇsᴘᴏɴ1 ᴏɴ \n"
                        else: ret_ += "11.┃ʀᴇsᴘᴏɴ1 ᴏғғ \n"
                        if settings["autoResponImage"] == True: ret_ += "12.┃ʀᴇsᴘᴏɴ2 ᴏɴ \n"
                        else: ret_ += "12.┃ʀᴇsᴘᴏɴ2 ᴏғғ \n"
                        if settings["autoResponPm"] == True: ret_ += "13.┃ʀᴇsᴘᴏɴ3 ᴏɴ \n"
                        else: ret_ += "13.┃ʀᴇsᴘᴏɴ3 ᴏғғ \n"                     
                        if settings["responPc"] == True: ret_ += "14.┃ʀᴇsᴘᴏɴᴘᴄ ᴏɴ \n"
                        else: ret_ += "14.┃ʀᴇsᴘᴏɴᴘᴄ ᴏғғ \n"
                        if settings["protect"] == True: ret_ += "15.┃ᴘʀᴏᴛᴇᴄᴛ ᴏɴ \n"
                        else: ret_ += "15.┃ᴘʀᴏᴛᴇᴄᴛ ᴏғғ \n"
                        if settings["qrprotect"] == True: ret_ += "16.┃ʟɪɴᴋᴘʀᴏᴛᴇᴄᴛ ᴏɴ \n"
                        else: ret_ += "16.┃ʟɪɴᴋᴘʀᴏᴛᴇᴄᴛ ᴏғғ \n"                    
                        if settings["autorejc"] == True: ret_ += "17.┃ᴀᴜᴛᴏʀᴇᴊᴇᴄᴛ ᴏɴ \n"
                        else: ret_ += "17.┃ᴀᴜᴛᴏʀᴇᴊᴇᴄᴛ ᴏғғ \n"
                        if settings["autoKick"] == True: ret_ += "18.┃ᴀᴜᴛᴏᴋɪᴄᴋ ᴏɴ \n"
                        else: ret_ += "18.┃ᴀᴜᴛᴏᴋɪᴄᴋ ᴏғғ \n"
                        ret_ += "╭═════════════════╮"
                        jp = line.getContact(lineMID).displayName
                        line.sendMessage(to, str(ret_)+"\n ❨✪❩ ʟɪɴᴇ ɴᴀᴍᴇ : "+jp+"\n ❨✪❩ ᴅᴋᴢ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ❨✪❩\n╰═════════════════╯")
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                        
                elif text.lower() == 'allsettings mode on':
                    settings["autoAdd"] = True
                    settings["autoblock"] = True
                    settings["contact"] = True
                    settings["autoJoin"] = True
                    settings["mimic"]["status"] = True
                    settings["welcomemsg"] = True
                    settings["leavemsg"] = True
                    settings["autoLeave"] = True
                    settings["autoRead"] = True
                    settings["checkSticker"] = True
                    settings["autoRespon"] = True
                    settings["autoResponImage"] = True
                    settings["autoResponPm"] = True
                    settings["responPc"] = True
                    settings["protect"] = True
                    settings["qrprotect"] = True
                    settings["autorejc"] = True
                    settings["autoKick"] = True
                    line.sendMessage(to, "All Setting Bot Mode On")
                    
                elif text.lower() == 'allsettings mode off':
                    settings["autoAdd"] = False
                    settings["autoblock"] = False
                    settings["contact"] = False
                    settings["autoJoin"] = False
                    settings["mimic"]["status"] = False
                    settings["welcomemsg"] = False
                    settings["leavemsg"] = False
                    settings["autoLeave"] = False
                    settings["autoRead"] = False
                    settings["checkSticker"] = False
                    settings["autoRespon"] = False
                    settings["autoResponImage"] = False
                    settings["autoResponPm"] = False
                    settings["responPc"] = False
                    settings["protect"] = False
                    settings["qrprotect"] = False
                    settings["autorejc"] = False
                    settings["autoKick"] = False
                    line.sendMessage(to, "All Setting Bot Mode Off")
                          
                elif text.lower() == 'clear ban':
                    line.sendMessage(to, "Removed banlist success")
             
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    line.sendMessage(to, "AutoAdd already On")
                    
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    line.sendMessage(to, "AutoAdd already Off")
    
                elif text.lower() == 'autoblock on':
                    settings["autoblock"] = True
                    line.sendMessage(to, "AutoBlock already On")
                    
                elif text.lower() == 'autoblock off':
                    settings["autoblock"] = False
                    line.sendMessage(to, "AutoBlock already Off")
           
                elif text.lower() == 'autojoin on':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "AutoJoin already On")
                    
                elif text.lower() == 'autojoin off':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "AutoJoin already Off")
                    
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    line.sendMessage(to, "AutoLeave already On")
                    
                elif text.lower() == 'autoleave off':
                    settings["autoLeave"] = False
                    line.sendMessage(to, "AutoLeave already Off")
                    
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    line.sendMessage(to, "Autoread Chat already On")
                    
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    line.sendMessage(to, "Autoread Chat already Off")
                    
                elif text.lower() == 'ceksticker on':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "CekStiker already On")
                    
                elif text.lower() == 'ceksticker off':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "CekStiker already Off")

                elif text.lower() == 'autokick on':
                    if sender in lineMID:
                        settings["autoKick"] = True
                        line.sendMessage(to, "AutoKick Di Aktifkan")
                        
                elif text.lower() == 'autokick off':
                    if sender in lineMID:
                        settings["autoKick"] = False
                        line.sendMessage(to, "AutoKick Turned Off")  
                    
                elif text.lower() == 'respon1 on':
                    if sender in lineMID:
                        settings["autoRespon"] = True
                        line.sendMessage(to, "Autorespon1 Text di Aktifkan")
                        
                elif text.lower() == 'respon1 off':
                    if sender in lineMID:
                        settings["autoRespon"] = False
                        line.sendMessage(to, "Autorespon1 Text Off")
                        
                elif text.lower() == 'respon2 on':
                    if sender in lineMID:
                        settings["autoResponImage"] = True
                        line.sendMessage(to, "Autorespon2 TagImage di Aktifkan")
                        
                elif text.lower() == 'respon2 off':
                    if sender in lineMID:
                        settings["autoResponImage"] = False
                        line.sendMessage(to, "Autorespon2 Image Off")
                        
                elif text.lower() == 'respon3 on':
                    if sender in lineMID:
                        settings["autoResponPm"] = True
                        line.sendMessage(to, "Autorespon3 PM di Aktifkan")
                        
                elif text.lower() == 'respon3 off':
                    if sender in lineMID:
                        settings["autoResponPm"] = False
                        line.sendMessage(to, "Autorespon3 PM Off")  
                        
                elif text.lower() == 'responpc on':
                    if sender in lineMID:
                        settings["responPc"] = True
                        line.sendMessage(to, "Autorespon Tagpc di Aktifkan")
                        
                elif text.lower() == 'responpc off':
                    if sender in lineMID:
                        settings["responPc"] = False
                        line.sendMessage(to, "Autorespon Tagpc Off")
                        
                elif text.lower() == 'protect on':
                    if sender in lineMID:	
                        if settings["protect"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to," Protection Already On")
                            else:
                                line.sendMessage(to,"Protection Already On")
                        else:
                            settings["protect"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Protection Already On")
                            else:
                                line.sendMessage(to,"Protection Already On")
                                
                elif text.lower() == 'protect off':
                    if sender in lineMID:
                        if settings["protect"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to," Protection Already Off ")
                            else:
                                line.sendMessage(to,"Protection Already Off ")
                        else:
                            settings["protect"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Protection Already Off ")
                            else:
                                line.sendMessage(to,"Protection Already Off ")
                                                              
                elif text.lower() == 'linkprotect on':
                    if sender in lineMID:
                        if settings["qrprotect"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Linkprotect Already On ")
                            else:
                                line.sendMessage(to,"Linkprotect Already On ")
                        else:
                            settings["qrprotect"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Linkprotect Already On ")
                            else:
                                line.sendMessage(to,"Linkprotect Already On ")
                                
                elif text.lower() == 'linkprotect off':
                    if sender in lineMID:
                        if settings["qrprotect"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Linkprotect Already Off ")
                            else:
                                line.sendMessage(to,"Linkprotect Already Off ")
                        else:
                            settings["qrprotect"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Linkprotect Already Off ")
                            else:
                                line.sendMessage(to,"Linkprotect Already Off ")                        
#==============================================================================#
                elif text.lower() == 'aku' or text.lower() == 'me':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus) 

                elif text.lower() == 'mid':
                    line.sendMessage(msg.to,lineMID)
                    
                elif text.lower() == 'tagme':
                	sendMessageWithMention(to, lineMID)
     
#==============================================================================#
                elif text.lower() == 'creator':
                    line.sendContact(to, "u9922f516e7fac1ea266f55a148e76217")
                                  
                elif text.lower() == 'myname':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"DisplayName:\n\n" + me.displayName)
                    
                elif text.lower() == "update pict":
                    settings["changePicture"] = True
                    line.sendMessage(to, "Send image")
                    
                elif text.lower() == "update pict group":
                    if msg.toType == 2:
                        if to not in settings["changeGroupPicture"]:
                            settings["changeGroupPicture"].append(to)
                        line.sendMessage(to, "Send image ")
                        
                elif text.lower() == 'mybio':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"StatusMessage:\n\n" + me.statusMessage)
                    
                elif text.lower() == 'pp':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                    
                elif text.lower() == 'myvid':
                    me = line.getContact(lineMID)                  
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                    
                elif text.lower() == 'cover':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
   
#___________________UNSEND_______________
                elif text.lower() == 'unsend:on':
                    if msg._from in lineMID:
                        wait["unsend"] = True
                        line.sendMessage(msg.to, "Unsend message enable")
                elif text.lower() == 'unsend:off':
                    if msg._from in lineMID:
                        wait["unsend"] = False
                        line.sendMessage(msg.to, "Unsend message disable")
                 
                elif msg.text.lower().startswith("getcontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                            
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            ret_ = ls
                        line.sendMessage(msg.to, str(ret_))
                        
                elif msg.text.lower().startswith("getname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                            
                elif msg.text.lower().startswith("getbio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                            
                elif msg.text.lower().startswith("pict "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                            
                elif msg.text.lower().startswith("get videoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                            
                            
#_______________VKICK______________________                            
                elif "vkick" in text.lower():
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:                              
                                line.kickoutFromGroup(msg.to, [mention['M']])
                                line.inviteIntoGroup(msg.to,[mention['M']])
                                line.cancelGroupInvitation(msg.to,[mention['M']])
                            except:
                                line.sendMessage(to, "Error")
 
#_____________KICK____________________                               
                elif "kick" in text.lower():
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                line.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                line.kickoutFromGroup(msg.to, [mention['M']])
                        else:
                            pass                               

#_____________NUKE_________________
                elif "Nuke" in msg.text:
                    if msg.toType == 2:
                        _name = msg.text.replace("Nuke","")
                        gs = line.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            line.sendMessage(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:
                                    line.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    pass
                                    
                elif "Nk:" in msg.text:
                    if msg.toType == 2:
                        _name = msg.text.replace("Nk:","")
                        gs = line.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            line.sendMessage(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:
                                    line.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    pass                                    
                            
                elif msg.text.lower().startswith("cover "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
  
                elif msg.text.lower().startswith("copy "):
                    if msg._from in lineMID:
                               #script clone profile Eg Scr
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                link = "http://dl.profile.line-cdn.net/" + line.getContact(ls).pictureStatus
                                path = line.downloadFileURL(str(link))
                                contact = line.getContact(ls)
                                line.updateProfilePicture(path)
                                nama = line.getProfile()
                                nama.displayName = contact.displayName
                                line.updateProfile(nama)
                                status = line.getProfile()
                                status.statusMessage = contact.statusMessage
                                line.updateProfile(status)
                                jp = line.getContact(sender).displayName
                                line.sendMessage(msg.to,"Berhasil Clone Profile "+jp)
 
                elif text.lower() == 'backup':
                 try:
                    line.updateProfilePicture(mybackup.pictureStatus)
                    line.updateProfile(mybackup)
                    line.sendMessage(msg.to, "Backup profile succes...")
                 except Exception as e:
                    line.sendMessage(msg.to, str (e))                             

                elif text.lower() == 'res':
                    try:
                        link = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                        path = line.downloadFileURL(str(link))
                        contact = line.getContact(lineMID)
                        line.updateProfilePicture(path)
                        nama = line.getProfile()
                        nama.displayName = str(myProfile["displayName"])
                        line.updateProfile(nama)
                        status = line.getProfile()
                        status.statusMessage = str(myProfile["statusMessage"])
                        line.updateProfile(status)
                        line.sendMessage(msg.to, "Done Backup Profile ")
                    except:
                        line.sendMessage(msg.to, "Invalid")
 
                elif msg.text.lower().startswith("restore"):
                           if msg._from in lineMID:
                              try:
                                  lineProfile.displayName = str(myProfile["displayName"])
                                  lineProfile.statusMessage = str(myProfile["statusMessage"])
                                  lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  line.updateProfileAttribute(8, lineProfile.pictureStatus)
                                  line.updateProfile(lineProfile)
                                  sendMention(msg.to, sender, "「 Restore Profile 」\nNama ", " \nBerhasil restore profile")
                              except:
                                  line.sendMessage(msg.to, "Gagal restore profile")
                                  
                elif text.lower() == 'pmpict':
                    contact = line.getContact(msg.to)
                    path =("http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                    line.sendImageWithURL(msg.to, path)
                    
                elif text.lower() == 'pmcover':
                    contact = line.getContact(msg.to)
                    cu = line.getProfileCoverURL(msg.to)
                    #cu = channel.getProfileCoverURL(msg.to)
                    #h = client.getHome(msg.to)
                    path = str(cu)
                    line.sendImageWithURL(msg.to, path)            

                elif msg.text.lower().startswith("gcall "):
                        if msg.toType == 2:
                            sep = text.split(" ")
                            strnum = text.replace(sep[0] + " ","")
                            num = int(strnum)
                            line.sendMessage(to, "Mengundang %s  call grup!" %str(num))
                            for var in range(0,num):
                                group = line.getGroup(to)
                                members = [contact.mid for contact in group.members]
                                line.acquireGroupCallRoute(to)
                                line.inviteIntoGroupCall(to, contactIds=members)
                                
                elif msg.text.lower().startswith("jumlahtag: "):
                  #if wait["selfbot"] == True:
                   if sender in lineMID:
                        proses = text.split(":")
                        strnum = text.replace(proses[0] + ":","")
                        num =  int(strnum)
                        Setmain["RAlimit"] = num
                        line.sendMessage(msg.to,"♻Total Spamtag Diubah Menjadi " +strnum)

                elif msg.text.lower().startswith("colek "):
                  #if wait["selfbot"] == True:
                   if sender in lineMID:
                       if 'MENTION' in msg.contentMetadata.keys()!=None:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            zx = ""
                            zxc = " "
                            zx2 = []
                            pesan2 = "@a"" "
                            xlen = str(len(zxc))
                            xlen2 = str(len(zxc)+len(pesan2)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':key1}
                            zx2.append(zx)
                            zxc += pesan2
                            msg.contentType = 0
                            msg.text = zxc
                            lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                            msg.contentMetadata = lol
                            jmlh = int(Setmain["RAlimit"])
                            if jmlh <= 1000:
                                for x in range(jmlh):
                                    try:
                                        line.sendMessage1(msg)
                                    except Exception as e:
                                        line.sendMessage(msg.to,str(e))
                            else:
                                line.sendMessage(msg.to,"Jumlah melebihi 1000")
                                
                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                            for x in range(jmlh):
                                line.sendMessage(msg.to, teks)
                            else:
                                line.sendMessage(msg.to, "")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "")
                            
                elif msg.text in ["."]:
                    line.sendMessage(msg.to,"Assalamu alaikum wr.wb...")

                elif msg.text in [".."]:
                    line.sendMessage(msg.to,"Wa'alaikum salam wr.wb...")            
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Target ditambahkan!")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                            
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[◑ The End  ◑]")

                elif "autoreject " in msg.text.lower():
                    xpesan = msg.text.lower()
                    xres = xpesan.replace("autoreject ","")
                    if xres == "off":
                        settings['autorejc'] = False
                        line.sendMessage(msg.to,"AutoReject already Off")
                    elif xres == "on":
                        settings['autorejc'] = True
                        line.sendMessage(msg.to,"AutoReject already On")
                        
                elif text.lower() == 'contact on':
                    if settings["contact"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(to,"Contact turned On")
                        else:
                            line.sendMessage(to,"Contact turned On")
                    else:
                        settings["contact"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(to,"Contact turned On")
                        else:
                            line.sendMessage(to,"Contact turned On")
                elif text.lower() == 'contact off':
                    if settings["contact"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(to,"Contact turned Off")
                        else:
                            line.sendMessage(to,"Contact turned Off")
                    else:
                        settings["contact"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(to,"Contact turned Off")
                        else:
                            line.sendMessage(to,"Contact turned Off")
                        
                elif "mimic " in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Reply Message On")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Reply Message Off")

                elif msg.text.lower().startswith("sider on"):
                    try:
                        del cctv['point'][msg.to]
                        del cctv['sidermem'][msg.to]
                        del cctv['cyduk'][msg.to]
                    except:
                        pass
                    cctv['point'][msg.to] = msg.id
                    cctv['sidermem'][msg.to] = ""
                    cctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"Sider Dkz turned On")

                elif msg.text.lower().startswith("sider off"):
                    if msg.to in cctv['point']:
                        cctv['cyduk'][msg.to]=False
                        line.sendMessage(msg.to, "ᴄᴄᴛv ʏᴀɴɢ ᴛᴇʀᴛᴀɴɢᴋᴀᴘ:\n"+cctv['sidermem'][msg.to])
                        line.sendMessage(to,"Sider Dkz turned Off")
                    else:
                        line.sendMessage(msg.to, "On aja belum ")

#==============================================================================#                       
                elif text.lower() == 'welcome on':
                  if settings["welcomemsg"] == True:
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"WelcomeMessage Turned On")
                  else:
                    settings["welcomemsg"] = True
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"WelcomeMessage Turned On")
                        
                elif text.lower() == 'welcome off':
                  if settings["welcomemsg"] == False:
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"WelcomeMessage Turned Off")
                  else:
                    settings["welcomemsg"] = False
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"WelcomeMessage Turned Off")

#==============================================================================#                       
                elif text.lower() == 'leavemsg on':
                  if settings["leavemsg"] == True:
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"LeaveMessage Turned On")
                  else:
                    settings["leavemsg"] = True
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"LeaveMessage Turned On")
                        
                elif text.lower() == 'leavemsg off':
                  if settings["leavemsg"] == False:
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"LeaveMessage Turned Off")
                  else:
                    settings["leavemsg"] = False
                    if settings["lang"] == "JP":
                        line.sendMessage(to,"LeaveMessage Turned Off")
#--------------------------------------------------------
                elif 'Set welcome ' in msg.text:
                   if msg._from in lineMID:
                      spl = msg.text.replace('Set welcome ','')
                      if spl in [""," ","\n",None]:
                          line.sendMessage(msg.to, "Gagal mengganti Welcome")
                      else:
                          settings["welcome"] = spl
                          line.sendMessage(msg.to, "WelcomeMessage diubah jadi :\n\n{}".format(str(spl)))
                          
                          
                elif text.lower() == "cek welcome":
                    if msg._from in lineMID:
                       line.sendMessage(msg.to, "WelcomeMessage :\n\n" + str(settings["welcome"]))


 #--------------------------------------------------------
                elif 'Set leavemsg ' in msg.text:
                   if msg._from in lineMID:
                      spl = msg.text.replace('Set leavemsg ','')
                      if spl in [""," ","\n",None]:
                          line.sendMessage(msg.to, "Gagal mengganti LeaveMsg")
                      else:
                          settings["keluar"] = spl
                          line.sendMessage(msg.to, "LeaveMessage diubah jadi :\n\n{}".format(str(spl)))
                          
                          
                elif text.lower() == "cek leavemsg":
                    if msg._from in lineMID:
                       line.sendMessage(msg.to, "LeaveMessage :\n\n" + str(settings["keluar"]))
#=============RESPON1=============================                      
                elif 'Set respon1 ' in msg.text:
                   if sender in lineMID:
                      spl = msg.text.replace('Set respon1 ','')
                      if spl in [""," ","\n",None]:
                          line.sendMessage(msg.to, "Gagal mengganti Respon1")
                      else:
                          settings["tag"] = spl
                          line.sendMessage(msg.to, "Respon1 Text Diubah Menjadi :\n\n{}".format(str(spl)))
                          
                elif text.lower() == "cek respon1":
                    if sender in lineMID:
                            line.sendMessage(msg.to, "Respon1 Text Kamu :\n\n" + str(settings["tag"]))
                       
 #=============RESPON2=============================                      
                elif 'Set respon2 ' in msg.text:
                   if sender in lineMID:
                      spl = msg.text.replace('Set respon2 ','')
                      if spl in [""," ","\n",None]:
                          line.sendMessage(msg.to, "Gagal mengganti Respon2")
                      else:
                          settings["tag2"] = spl
                          line.sendMessage(msg.to, "Respon2 Image Diubah Menjadi :\n\n{}".format(str(spl)))
                          
                elif text.lower() == "cek respon2":
                    if sender in lineMID:
                       line.sendMessage(msg.to, "Respon2 TagImage Kamu :\n\n" + str(settings["tag2"]))

  #=============RESPON3============================                      
                elif 'Set respon3 ' in msg.text:
                   if sender in lineMID:
                      spl = msg.text.replace('Set respon3 ','')
                      if spl in [""," ","\n",None]:
                          line.sendMessage(msg.to, "Gagal mengganti Respon3")
                      else:
                          settings["tag3"] = spl
                          line.sendMessage(msg.to, "Respon3 PM Diubah Menjadi :\n\n{}".format(str(spl)))
                          
                elif text.lower() == "cek respon3":
                    if sender in lineMID:
                       line.sendMessage(msg.to, "Respon3 PM Kamu :\n\n" + str(settings["tag3"]))    
 
  #=============RESPON3============================                      
                elif 'Set autolike ' in msg.text:
                   if sender in lineMID:
                      spl = msg.text.replace('Set autolike ','')
                      if spl in [""," ","\n",None]:
                          line.sendMessage(msg.to, "Gagal mengganti autolike")
                      else:
                          wait["comment1"] = spl
                          line.sendMessage(msg.to, "Autocommand like diubah menjadi :\n\n{}".format(str(spl)))
#=============RESPON3============================                      
                elif 'Set sidertext ' in msg.text:
                   if sender in lineMID:
                      spl = msg.text.replace('Set sidertext ','')
                      if spl in [""," ","\n",None]:
                          line.sendMessage(msg.to, "Gagal mengganti Sider")
                      else:
                          settings["mention"] = spl
                          line.sendMessage(msg.to, "Sider Diubah Menjadi :\n\n{}".format(str(spl)))
                          
                elif text.lower() == "cek sidertext":
                    if sender in lineMID:
                       line.sendMessage(msg.to, "Sider Kamu :\n\n" + str(settings["mention"]))    

                elif 'Set responpc ' in msg.text:
                   if sender in lineMID:
                      spl = msg.text.replace('Set responpc ','')
                      if spl in [""," ","\n",None]:
                          line.sendMessage(msg.to, "Gagal mengganti ResponPc")
                      else:
                          settings["responpc"] = spl
                          line.sendMessage(msg.to, "Respon Pc diganti jadi :\n\n".format(str(spl)))
                                                    
                elif text.lower() == "cek responpc":
                    if sender in lineMID:
                       line.sendMessage(msg.to, "Respon Pc mu :\n\n"+ str(settings["responpc"]))
       
                elif text.lower() == "cek autolike":
                    if sender in lineMID:
                       line.sendMessage(msg.to, "AutoLike mu :\n\n"+ str(wait["comment1"]))
       
                elif text.lower() == 'gcreator':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    
                elif text.lower() == 'gid':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "[ID Group : ]\n" + gid.id)
                    
                elif text.lower() == 'gpict':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                    
                elif text.lower() == 'gname':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                    
                elif text.lower() == 'gurl':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            line.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                            
                elif text.lower() == 'link on':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "Berhasil membuka grup qr")
                            
                elif text.lower() == 'link off':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "Berhasil menutup grup qr")
                            
                elif text.lower() == 'reject':                            
                    gid = line.getGroupIdsInvited()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        line.sendMessage(msg.to,"Reject GroupInvited Done")
                    else:
                        line.sendMessage(msg.to,"Done")
     
                elif text.lower() == 'cancel':
                       if msg._from in lineMID: 
                        if msg.toType == 2:
                            group = line.getGroup(msg.to)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                line.cancelGroupInvitation(msg.to,[_mid])
                            line.sendMessage(msg.to,"I pretended to cancel and canceled.")
                   
                elif text.lower() == 'ginfo':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
                    
                elif text.lower() == 'memlist':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                        
                        
                elif text.lower() == 'groups':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))
                        
                        
                elif msg.text in ["Autolike"]:
                  if sender in lineMID:
                    print ("[Command]Like executed")
                    line.sendMessage(msg.to,"Auto Like Is running")
                    try:
                      autolike()
                    except:
                      pass                        

                        
                elif "/ti/g/" in msg.text.lower():
                    if settings["autoJoinTicket"] == True:
                        link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        links = link_re.findall(text)
                        n_links = []
                        for l in links:
                            if l not in n_links:
                                n_links.append(l)
                        for ticket_id in n_links:
                            group = line.findGroupByTicket(ticket_id)
                            line.acceptGroupInvitationByTicket(group.id,ticket_id)
                            line.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                        
                elif text.lower() == 'tagmem' or text.lower() == 'tag' or text.lower() == 'hi' or text.lower() == 'dkz' or text.lower() == 'cling' or text.lower() == 'hem' or text.lower() == 'absen' or text.lower() == 'muach' or text.lower() == 'hai' or text.lower() == "dor":
                    group = line.getGroup(msg.to)
                    members = [contact.mid for contact in group.members]
                    tags = []
                    for i in range(0, len(members), 20):
                        tags.append(list(members[i:i+20]))
                    for t in tags:
                        msg = ttypes.Message(to=to)
                        tst ="❨✪❩ ᴅᴋᴢ ᴍᴇɴᴛɪᴏɴs ❨✪❩ \n\n"
                        tst += u''
                        s=len(tst)
                        d=[]
                        for i in range(len(t)):
                            d.append({"S":str(s), "E" :str(s+4), "M":t[i]})
                            s += 5
                            tst +=u'@jek\n'
                        msg.text = tst.rstrip()
                        msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                        line.talk.sendMessage(0,msg)
                        jp = line.getContact(lineMID).displayName
                    else:
                    	line.sendMessage(to,"╭════════════════╮\n❨✪❩ ᴍᴇɴᴛɪᴏɴᴇs ʙʏ : " + jp+"\n╰════════════════╯")
                        

#==============================================================================#   
                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    line.sendMessage(msg.to, readTime)                 

                elif text.lower() == "remove chat":
                    if msg._from in lineMID:
                       try:
                           line.removeAllMessages(op.param2)
                           line.sendMessage(msg.to,"Chat dibersihkan...")
                       except:
                           pass
             

                elif msg.text.startswith("Music "):
                        try:
                            query = msg.text.replace("Music ","")
                            query = urllib.parse.quote(query)
                            url = "https://www.youtube.com/results?search_query=" + query
                            response = urllib.request.urlopen(url)
                            html = response.read()
                            soup = BeautifulSoup(html, "html.parser")
                            results = soup.find(attrs={'class':'yt-uix-tile-link'})
                            dl=("https://www.youtube.com" + results['href'])
                            vid = pafy.new(dl)
                            stream = vid.streams
                            for s in stream:
                                vin = s.url
                                hasil = 'Hasil Info Music:\n\n'
                                hasil += vid.title
                                hasil +='\n» Penulis : ' + str(vid.author)
                                hasil +='\n» Durasi : ' + str(vid.duration)
                                hasil +='\n» Suka : ' + str(vid.likes) 
                                hasil +='\n» Penonton : ' + str(vid.viewcount) 
                                hasil +='\n» Rating : ' +str(vid.rating)
                                hasil +='\n» Diterbitkan : ' + str(vid.published)
                                hasil +='\n» Channel : Jeckydkz.music.com'
                            line.sendMessage(msg.to,hasil)
                            line.sendAudioWithURL(msg.to,vin)
                            line.sendVideoWithURL(msg.to,vin)
                            print (" Yt-mp3 Succes open")
                        except:
                            line.sendMessage(msg.to, "Maaf Keyword anda salah")

                elif "kalkulator" in msg.text.lower():
                    try:
                        sep = msg.text.split(" ")
                        cal = msg.text.replace(sep[0] + " ","")
                        result = requests.get("http://calcatraz.com/calculator/api?c="+urllib.parse.quote(cal))
                        data = result.text
                        line.sendMessage(to,"Hasil:\n\n"+ cal+ " = " +str(data))
                    except Exception as error:
                        logError(error)
                        line.sendMessage(to, str(error))
                    
                elif "instagram" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ Total Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            line.sendImageWithURL(to, str(path))
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "Pengguna tidak ditemukan")

                elif msg.text.lower().startswith("movie"):
                    try:
                        sep = msg.text.split(" ")
                        search = msg.text.replace(sep[0] + " ","")
                        apiKey = "zbYyMGhWy06DDsSHeUAK3GHQkEbCL8"
                        api = requests.get("https://farzain.xyz/api/film.php?apikey={}&id={}".format(str(apiKey), str(search)))
                        data = api.text
                        data = json.loads(data)
                        if data["status"] == "success":
                            anu = "[ Result Film ]"
                            anu += "\nTitle : {}".format(str(data["Title"]))
                            anu += "\nYear : {}".format(str(data["Year"]))
                            anu += "\nRated : {}".format(str(data["Rated"]))
                            anu += "\nReleased : {}".format(str(data["Released"]))
                            anu += "\nDuration : {}".format(str(data["Runtime"]))
                            anu += "\nGenre : {}".format(str(data["Genre"]))
                            path = str(data["Poster"])
                            line.sendImageWithURL(msg.to, str(path))
                            line.sendMessage(msg.to, str(anu))
                        else:
                            sendMentionV2(msg.to, "Maaf @!,hasil pencarin tidak ditemukan", [sender])
                    except Exception as error:
                        line.sendMessage(msg.to, str(error))

 #___________BROADCAST_______________
                elif msg.text.lower().startswith("broadcast "):   
                   sep = text.split(" ")
                   txt = text.replace(sep[0] + " ","")
                   groups = line.groups
                   for group in groups:
                       line.sendMessage(group, "Broadcast:\n\n{}".format(str(txt)))

                elif text.startswith("Led "):
                   separate = text.split(" ")
                   teks = text.replace(separate[0] + " ","")
                   url = "https://ari-api.herokuapp.com/led?text="+teks+"&sign=PB"
                   line.sendImageWithURL(to, url)

                elif text.startswith("Poster "):
                   separate = text.split(" ")
                   teks = text.replace(separate[0] + " ","")
                   url = "https://ari-api.herokuapp.com/neon?text="+teks+"&color=blue"
                   line.sendImageWithURL(to, url)

                elif text.startswith("Fs "):
                   sep = text.split(" ")
                   txt = text.replace(sep[0] + " ","")
                   url = "https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=nda123&text={}".format(txt)
                   line.sendImageWithURL(to, url)

                elif text.startswith("Coba "):
                   sep = text.split(" ")
                   txt = text.replace(sep[0] + " ","")
                   url = "https://rest.farzain.com/api/cooltext.php?text={}&apikey=nda123".format(txt)
                   line.sendImageWithURL(to, url)

                elif text.startswith("Anu "):
                   txt = text.replace("Anu ","")
                   url = "https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=nda123&text={}".format(txt)
                   line.sendImageWithURL(to, url)
                   
                elif text.lower() == "kontak me":
                   line.sendMessage(to, "Nama mu : " + line.getContact(sender).displayName + "\n\nBio mu : \n" + line.getContact(sender).statusMessage + "\n\nLink profil mu :\nhttp://dl.profile.line-cdn.net/" + line.getContact(sender).pictureStatus)
                   line.sendMessage(to, "Mid mu : \n" + sender)
                   
                elif text.lower() == "info me":
                    status = ["Status Kehidupan : Menjomblo", "Status Kehidupan : Menjones", "Status Kehidupan : Menikah", "Status Kehidupan : Menyendiri"]
                    muka = ["Wajah : Jelek dekil", "Wajah : Cantik", "Wajah : Bengkok", "Wajah : Item mutung", "Wajah : Rata"]
                    jenis = ["Jenis kelamin : Laki - laki", "Jenis kelamin : Perempuan", "Jenis kelamin : Waria", "Jenis kelamin : Tidak punya"]
                    line.sendMessage(to, "Nama : " + line.getContact(msg._from).displayName + "\n" + random.choice(jenis) + "\n" + random.choice(muka) + "\n" + random.choice(status))

                elif text.startswith("Smule "):
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split("-")
                            search = str(count[0])
                            r = requests.get("https://www.smule.com/"+search+"/performances/json")
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                ret_ = "Record Smule:\n"
                                for aa in data["list"]:
                                    no += 1
                                    ret_ += "\n" + str(no) + ". " + str(aa["title"])
                                ret_ += "\n\nSelanjutnya ketik: smule {}-nomor\nuntuk melihat detailnya. ".format(str(search))
                                line.sendMessage(msg.to,ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["list"][num - 1]
                                    smule = str(b["web_url"])
                                    c = "Judul Oc: "+str(b["title"])
                                    c += "\nPembuat: "+str(b["owner"]["handle"])
                                    c += "\nTotal like: "+str(b["stats"]["total_loves"])+" like"
                                    c += "\nTotal comment: "+str(b["stats"]["total_comments"])+" comment"
                                    c += "\nStatus VIP: "+str(b["owner"]["is_vip"])
                                    c += "\nStatus Oc: "+str(b["message"])
                                    c += "\nCreated Oc: {}".format(b["created_at"][:10])
                                    c += "\nDidengarkan: {}".format(b["stats"]["total_listens"])+" orang"
                                    hasil = "Detail Record\n\n"+str(c)
                                    dl = str(b["cover_url"])
                                    line.sendImageWithURL(msg.to,dl)
                                    line.sendMessage(msg.to, hasil, {'AGENT_NAME': ' URL Smule','AGENT_LINK': 'https://www.smule.com/{}'.format(str(b['owner']['handle'])),'AGENT_ICON': 'https://png.icons8.com/color/50/000000/speaker.png' })
                                    with requests.session() as s:
                                        s.headers['user-agent'] = 'Mozilla/5.0'
                                        r = s.get("https://sing.salon/smule-downloader/?url=https://www.smule.com{}".format(urllib.parse.quote(smule)))
                                        data = BeautifulSoup(r.content, 'html5lib')
                                        get = data.select("a[href*=https://www.smule.com/redir?]")[0]
                                        title = data.findAll('h2')[0].text
                                        imag = data.select("img[src*=https://www.smule.com/redir?]")[0]
                                        if 'Smule.m4a' in get['download']:
                                            line.sendMessage(msg.to,"Type: Audio\n\nPlease wait for audio...")
                                            line.sendAudioWithURL(msg.to, get['href'])
                                        else:
                                            line.sendMessage(msg.to,"Type: Video\n\nPlease wait for video...")
                                            line.sendVideoWithURL(msg.to, get['href'])
                                except Exception as e:
                                    line.sendMessage(msg.to,"Result Error:\n"+str(e))


                elif text.startswith("Ceksmule "):
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get("https://www.smule.com/{}".format(urllib.parse.quote(search)))
                                gunakan = BeautifulSoup(r.content, 'html5lib')
                            for getinfosmule in gunakan.findAll('script',{'type':'text/javascript'})[1]:
                                getJsonSmule = re.search(r'DataStore.Pages.Profile\s*=\s*(\{.+\})\s*;', getinfosmule).group(1)
                                data = json.loads(getJsonSmule)
                            for smuleProfile in data:
                                ret_ = "Profile Smule:\n"
                                ret_ += "\n• Id Smule: @{}".format(str(data["user"]["handle"]))
                                ret_ += "\n• Total Rekaman: {} record".format(str(data["user"]["num_performances"]))
                                ret_ += "\n• Pengikut: {} orang".format(str(data["user"]["followers"]))
                                ret_ += "\n• Mengikuti: {} orang".format(str(data["user"]["followees"]))
                                ret_ += "\n• Bio: {}".format(str(data["user"]["blurb"]))
                                if data["user"]["is_verified"] == True:
                                    ret_ += "\n• Verifikasi: Sudah"
                                else:
                                    ret_ += "\n• Verifikasi: Belum"
                                if data["user"]["is_vip"] == True:
                                    ret_ += "\n• Akun VIP: Iya"
                                else:
                                    ret_ += "\n• Akun VIP: Tidak"
                                    
                                path = data["user"]["pic_url"]
                                name = "INFO PROFILE SMULE"
                                url = "https://www.smule.com/{}".format(search)
                                iconlink = data["user"]["pic_url"]
                            line.sendMessage(to, str(ret_))
                            line.sendImageWithURL(msg.to, str(path))
#======
                elif text.lower() == '.bye':
                  if msg.toType == 2:
                    ginfo = line.getGroup(msg.to)
                    try:
                        line.sendMessage(msg.to,"Bye! "  +  str(ginfo.name))
                        line.leaveGroup(msg.to)
                    except:
                        pass    
#____________________________________

                elif "image: " in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))

                elif "youtube" in msg.text.lower():
                          if msg._from in lineMID:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "💿 Judul 🎼〘 " + vid.title + " 〙"
                                    author = '\n\n✏ Author : ' + str(vid.author)
                                    durasi = '\n📟 Duration : ' + str(vid.duration)
                                    suka = '\n👍 Likes : ' + str(vid.likes)
                                    rating = '\n⭐ Rating : ' + str(vid.rating)
                                    deskripsi = '\n📋 Deskripsi : ' + str(vid.description)
                                line.sendVideoWithURL(msg.to, me)
                                line.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                line.sendMessage(msg.to,str(e))                                

            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
                    
            elif settings["contact"] == True:
                msg.contentType = 0
                line.sendMessage(msg.to,msg.contentMetadata["mid"])
                if 'displayName' in msg.contentMetadata:
                    contact = line.getContact(msg.contentMetadata["mid"])
                    try:
                        cu = line.channel.getCover(msg.contentMetadata["mid"])
                    except:
                        cu = ""
                    line.sendMessage(to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                else:
                    contact = line.getContact(msg.contentMetadata["mid"])
                    try:
                        cu = line.channel.getCover(msg.contentMetadata["mid"])
                    except:
                        cu = ""
                    line.sendMessage(to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 1:
                if settings["changePicture"] == True:
                    path = line.downloadObjectMsg(msg_id)
                    settings["changePicture"] = False
                    line.updateProfilePicture(path)
                    line.sendMessage(to, "Berhasil mengubah foto profile")

                if msg.toType == 2:
                    if to in settings["changeGroupPicture"]:
                        path = line.downloadObjectMsg(msg_id)
                        settings["changeGroupPicture"].remove(to)
                        line.updateGroupPicture(to, path)
                        line.sendMessage(to, "Berhasil mengubah foto group")
                        
            elif msg.contentType == 16:
                    mid = data["actorId"]
                    postId = data["activityExternalId"]
                    line.likePost(to, mid, postId, likeType=1001)
                    line.createComment(to, mid, postId, "AutoLike by: Team Dkz Protection ")
#==============================================================================#
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in lineMID:
                    pass
                ginfo = line.getGroup(op.param1)
                contact = line.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                line.sendImageWithURL(op.param1, image)
                
        if op.type == 13:
            if lineMID in op.param3:
              if settings["autojj"] == "wl":
                if op.param2 in periksa["wl"]:
                  line.acceptGroupInvitation(op.param1)
                else:
                    if settings['autorejc'] == True:
                        line.rejectGroupInvitation(op.param1)
                    else:
                        pass
              elif settings["autojj"] == "all":
                  line.acceptGroupInvitation(op.param1)
              else:
                  if settings['autorejc'] == True:
                        line.rejectGroupInvitation(op.param1)
                  else:
                        pass

        if op.type == 26:
          if wait["Mute"] == False:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                if settings["autoBalas"] == True:
                    if msg.toType == 0:                	
                        line.sendChatChecked(sender,msg_id)
                        contact = line.getContact(sender)
                        mids = [contact.mid]
                        text = "[ Auto Respon ]\n\nHallo @!\nMohon Maaf Saya Sedang Sibuk, Ini Adalah Pesan Otomatis, Jika Ada Yang Penting Mohon Hubungi Saya Nanti, Terimakasih..."
                        summon(op.param1)
                else:
                    to = receiver
            else:
                to = receiver
                if msg.contentType == 0:
                    if settings["autoRead"] == True:
                        line.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)                        
                if settings["unsendMessage"] == True:
                    try:
                        msg = op.message
                        if msg.toType == 0:
                            line.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                        else:
                            line.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                            msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    except Exception as error:
                        logError(error)          

                if msg.contentType == 0:
                    if text is None:
                        return
                    if "/ti/g/" in msg.text.lower():
                        if settings["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = line.findGroupByTicket(ticket_id)
                                line.acceptGroupInvitationByTicket(group.id,ticket_id)
                                line.sendMessage(to, "Berhasil join ke group %s" % str(group.name))

#___________________RESPON TEXT__________________
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                if settings["autoRespon"]:
                                    contact = line.getContact(sender)
                                    line.sendMessage(to, settings["tag"])
                                break
                                

#___________________RESPON KICKTAG_________________
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                if settings["autoKick"]:
                                    contact = line.getContact(sender)
                                    jp = line.getContact(sender).displayName
                                    line.sendMessage(to, "Please SHUT THE FUCK UP")
                                    line.kickoutFromGroup(msg.to,[sender])
                                break                                

#___________________RESPON IMAGE_________________
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                if settings["autoResponImage"]:
                                    contact = line.getContact(sender)
                                    anu = contact.displayName
                                    path = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                                    line.sendMessage(to, settings["tag2"])
                                    line.sendImageWithURL(msg.to, str(path))
                                break
                                                             
  #___________________RESPON PM________________
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                if settings["autoResponPm"]:
                                    contact = line.getContact(sender)
                                    line.sendMessage(sender, settings["tag3"])
                                break              
                                
#___________________________                             
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                if msg.to in responPc:
                                    G = line.getGroup(to)
                                    contact = line.getContact(sender)
                                    anu = contact.displayName
                                    #sid = str(tikel["sid"])
                                    #spkg = str(tikel["spkg"])
                                    anu = contact.displayName
                                    line.sendMessage(sender, settings["responpc"])
                                    #line.sendSticker(sender, spkg, sid)
                                break                           
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    line.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)
                if msg.contentType == 16:
                   url = msg.contentMetadata["postEndUrl"]
                   line.likePost(url[25:58], url[66:], likeType=1001)
                   line.createComment(url[25:58], url[66:], wait["comment1"])
                   line.sendMessage(msg.to, "╭═════════════════╮\n  » ᴅᴇᴛᴇᴄᴛ ᴘᴏsᴛ ʙʏ: ᴛᴇᴀᴍ ᴅᴋᴢ\n  » ᴀᴜᴛᴏʟɪᴋᴇ ʜᴀs ʙᴇᴇɴ sᴇɴᴛ\n╰═════════════════╯")
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

#==============================================================================#
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass

#==============================================================================#
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = line.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n☛ " + Name
                        summon(op.param1,[op.param2])
                        line.sendMessage(op.param1,settings["mention"])
                        ginfo = line.getGroup(op.param1)
                        contact = line.getContact(op.param2).picturePath
                        image = 'http://dl.profile.line.naver.jp'+contact
                        line.sendImageWithURL(op.param1, image)       

        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                line.sendMessage(msg.to, "[̟]: " + data['result']['response'].encode('utf-8'))
                                
    except Exception as error:
        logError(error)
#==============================================================================#
def autolike():
    count = 1
    while True:
        try:
           for posts in line.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                   line.likePost(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print ("Like")
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          line.createComment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def autoLike():
    count = 1
    while True:
        try:
          # for posts in cl.getFeed(postLimit=10, commentLimit=1, likeLimit=1, order='TIME')["result"]["feed"]:
             if hasil["postInfo"]["homeId"]["postId"] is False:
                if wait["sukaPost"] == True:
                   line.likePost(hasil["userMid"]["writerMid"], hasil["postInfo"]["postId"], likeType=1001)
                   print ("Like")
                   if wait["commentOn"] == True:
                      if hasil["homeId"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          line.createComment(posts["userMid"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
            
def autoLiked():
	#if settings["sukaPost"] == True:
		lastTimeLiking = time.time()
		if time.time() - lastTimeLiking >= 60*60:
			listLikeType = 1001
			myComment = "[ Auto Like by: Team Dkz Protection ]"
			feed = client.getFeed()
			if feed["message"] != 'succes':
				lastTimeLiking = time.time()
				return True
			del feed["result"]["feedInfos"]
			result = ["result"]["feeds"]
			for res in result:
				postInfo = res["post"]["postInfo"]
				homeId = postInfo["homeId"]
				postId = postInfo["postId"]
				likeStat = postInfo["liked"]
				if likeStat == True:
					continue
				else:
					line.likePost(homeId, postId, listLikeType)
					line.createComment(homeId, postId, myComment)
					lastTimeLiking = time.time()

thread1 = threading.Thread(target=autoLike)
thread1.daemon = True
thread1.start()         
while True:
  try:
      Ops = line.poll.fetchOperations(line.revision, 50)
      for op in Ops:
        if op.type != 0:
          line.revision = max(line.revision, op.revision)
          lineBot(op)
  except Exception as E:
    E = str(E)
    if "reason=None" in E:
      print (E)
      time.sleep(60)
      restart_program()
        
        

        
        
