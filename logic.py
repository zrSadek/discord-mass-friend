import discum
import json
import httpx
import colorama
from colorama import Fore
def Scraper(token,serverid,channelid):
    colorama.init()
    open('userids.txt', 'w').close()
    bot = discum.Client(token=token)

    def close_after_fetching(resp, guild_id):
     if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

    def get_members(guild_id, channel_id):
     bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
     bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
     bot.gateway.run()
     bot.gateway.resetSession()
     return bot.gateway.session.guild(guild_id).members

    members = get_members(serverid, channelid)
    memberslist = []

    for memberID in members:
     memberslist.append(memberID)
     print("[SCRAPER]" + memberID)

    f = open('userids.txt', "a")
    for element in memberslist:
     f.write(element + '\n')
    f.close()
    
    with open("userids.txt") as f:
        read = f.readlines()
    for line in read:
       if "515067662028636170" in line:
        print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Beemo")
       elif "242730576195354624" in line:
        print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Auttaja")
       elif "292953664492929025" in line:
           print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected UnbeliveaBoat") 
       elif "372022813839851520" in line:
           print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected AltDentifier")
       elif "512333785338216465" in line:
           print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Captcha.Bot")
       elif "370665722780712960" in line:
            print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected FTNL")
       elif "651095740390834176" in line:
             print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Security")
       elif "792081366862790687" in line:
                        print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Verifier")
       elif "536991182035746816" in line:
                            print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Wick")
       elif "746581603844751460" in line:
                                print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected YN9")
       elif "809104772178903051" in line:
                                    print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] MTS")
       elif "732756538053230612" in line:
                                        print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Security Bot")
       elif "593921296224747521" in line:
                                 print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Bleed")
       elif "548410451818708993" in line:
                               print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Wick Premium")          
       elif "703886990948565003" in line:
                               print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Double Counter")      
       elif "926978594301935637" in line:
                               print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Defender")                                                                                          
       elif "245675252821000193" in line:
                               print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Gaius")
       elif "769772015447703592" in line:
                                print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Beemo Helper")
       elif "80528701850124288" in line:
        print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected R.DANNY")
       elif "240254129333731328" in line:
        print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Vortex") 
       elif "776128410547126322" in line:
               print(f"{Fore.LIGHTRED_EX}⚠️ [DEBUG] Detected Blame")
 
        



def main():
    token = input("Token: ")
    serverid = input("Server ID: ")
    channelid = input("Channel ID: ")
    Scraper(token,serverid,channelid)