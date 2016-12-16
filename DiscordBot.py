'''
Bot created for discord by Selezar using discord python 2 library. Most of the functions are for the game Aries Maplestory.

This was a valuable learning experience as I haven't ever used asyncio before or a library with almost zero community examples. Had to fumble around in the dark a lot but hopefully people in the future will be able to use this to minimize some of the anguish and frustration I went through. Brush up on your object oriented programming btw before attempting to make sense of this.

This uses the library asyncio in python extensively. It has a steep learning curve as the syntax is quite different

'''


import discord
import asyncio
import urllib
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import os
import requests
from robobrowser import RoboBrowser
from collections import OrderedDict
import random


client = discord.Client()

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

''' These async functions work concurrently with the main loop. Think of it like a threading alternative'''

async def AutoLinkPoster(var1, url, Num, var2):
    ''' A simple auto link poster '''
    Duration = int(var1)
    await client.wait_until_ready()
    #channel = discord.Object(id=Num)
    
    while not client.is_closed:
        await client.send_message(Num.channel, (var2.mention+' '+url))
        await asyncio.sleep(Duration) # task runs every 60 seconds or the duration provided
        
async def AutoMacroPoster(var1, url, Num, var2):
    ''' A simple Macro recorder and poster '''
    Duration = int(var1)
    await client.wait_until_ready()
   # channel = discord.Object(id=Num)
    counter = 0
    while not client.is_closed:
        counter +=1
        await client.send_message(Num.channel, url)
        await asyncio.sleep(Duration) # task runs every 60 seconds or the duration provided
        if counter>5:
            break
        
        
async def AlertWhenServerUp(MyVar2):
    '''
    This will run as a background task and an be called mutliple times by different people. It accepts the channel id and the user name who called it through on_message. It will crawl aries homepage and check to see if it is online every minute. If it is, then the infinite loop will exit and a message to the user who called this will be sent saying that servers are up
    '''
    await client.wait_until_ready()
    while True:
        ''' This loop will continue looping and scraping aries front website to see if server is online. If it is, then it will break the loop and alert person who called this func'''
        url = 'http://aries.elluel.net/'

        browser = RoboBrowser(history=True,parser='html.parser',user_agent='Chrome/41.0.2228.0')
        browser.open(url)

        MyButton = browser.find('button')

        if 'ONLINE' in MyButton.text:
            break
        await asyncio.sleep(60) # task runs every 60 seconds or the duration provided
        
    ''' Sending the alert message to the author since servers are up now'''
    await client.send_message(MyVar2, 'The servers are up now. Hope I was useful to you. If you have any other useful alert ideas then DM them to me. Enjoy!')
    
    
    
  
async def MonitorForumThread(Msg, ForumThread ,GUY):
    '''
    This will run as a background infinite loop task on aries forums. It will monitor the thread passed into this function and check to see if the requested user is in the seen category. If it is then the loop will break and the person who called this function will be sent a personal DM saying that the person has this thread.
    '''
    await client.wait_until_ready()
    BreakVar = False
    while True:
        ForumURL = ForumThread
        
        base_url = 'http://elluel.net/'
        
        browser = RoboBrowser(history=True,parser='html.parser',user_agent='Chrome/41.0.2228.0')
        browser.open(base_url)
        form = browser.get_form(id = 'navbar_loginform')
        
        form["vb_login_username"] = 'Selezar'
        form["vb_login_password"] = 'spiderman211'
        
        browser.submit_form(form)
        
        
        browser.open(ForumURL)
        
        
        MyLinks = browser.find('ul',{'class':'commalist'}).find_all('li')
        
        for line in MyLinks:
            #print (line.text)
            if GUY in line.text:
                BreakVar = True
                
        if BreakVar == True:
            break
        await asyncio.sleep(300) # task runs every 60 seconds or the duration provided
    await client.send_message(Msg.author, GUY+' has seen the thread '+ForumThread+' now in the last 5 mins. Enjoy.')
    

  
def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0  
    
def StalkAriesForum(message, author, MUVAR3):
    '''
    This will stalk aries forum profile page and return what the person is currently doing and when the last active action was
    '''
    base_url = 'http://elluel.net/'
    
    browser = RoboBrowser(history=True,parser='html.parser',user_agent='Chrome/41.0.2228.0')
    browser.open(base_url)
    form = browser.get_form(id = 'navbar_loginform')
    
    form["vb_login_username"] = 'Selezar'
    form["vb_login_password"] = 'spiderman211'
    
    browser.submit_form(form)
    
    StalkedURL = 'http://elluel.net/member.php?'+MUVAR3
    browser.open(StalkedURL)
    
    CurrentActivity = ''
    LastActivity = ''
    

    MyLinks = browser.find('div',{'class':'blockrow member_blockrow'}).find_all('dd')
    
    for line in MyLinks:
        if 'Viewing' in line.text:
            CurrentActivity = line.text
        if 'AM' in line.text or 'PM' in line.text:
            LastActivity = line.text
        
    
    ReturnList = []
    ReturnList.append(LastActivity)
    ReturnList.append(CurrentActivity)
    
    return ReturnList
    
    
def GameUpdatesForum():
    '''
    This will return as a list the latest aries updates from the main forums
    '''
    MyUpdateList = []
    base_url = 'http://elluel.net/'
    
    browser = RoboBrowser(history=True,parser='html.parser',user_agent='Chrome/41.0.2228.0')
    browser.open(base_url)

    form = browser.get_form(id = 'navbar_loginform')
    
    form["vb_login_username"] = 'Selezar'
    form["vb_login_password"] = 'spiderman211'
    
    browser.submit_form(form)
    
    browser.open('http://elluel.net/showthread.php?15877-AriesMS-Official-Update-Fix-Log')
    
    MyLinks = browser.find('div',{'class':'spoiler'}).find_all('li')
    
    for line in MyLinks:
        MyUpdateList.append(line.text)
        
    return MyUpdateList
    
    
    
    
    
@client.event
async def on_message(message):
    '''
    This is the main event function. Everytime someone sends a message on any of the channels the bot is in, this function will trigger. All message are printed to the windows terminal. The IF statements deal with specific words spoken in the messages.
    '''
    AI = random.randint(0,5)
    author = message.author
    try:
        print ('Message from: '+str(author)+' : '+str(message.content)+' | '+str(message.server)+' | '+str(message.channel))
    except UnicodeEncodeError:
        pass
    
    if '!Help' in message.content and 'Selezar' not in str(author):
        await client.send_message(message.channel, ('```Markdown'+'\n'+'#Command 1  !Latest Update This will fetch the latest aries game updates from the forum'+'\n'+'#Command 2  !Alert Me  This will check to see if the game servers are up and automatially DM you when they are'+'\n'+'#Command 3  !Stalk <Forum ID>  This will return what the requested person is doing on the forums'+'\n'+'```') )    
    
    if client.user.mention in message.content and 'Selezar' not in str(author):
        await client.send_message(message.channel, ('`This is an automated message, I am currently away saving the world but will be back shortly.`'+(author.mention)) )
    
    if 'Greet Me' in message.content:
        await client.send_message(message.channel, ('How are you doing, '+(author.mention)+' ?') )
        
    if 'Good and you?' in message.content:
        await client.send_message(message.channel, 'I am well. What is my purpose?')
        
    if 'You post memes only' in message.content:
        await client.send_message(message.channel, 'I post memes only? Oh my god ((´д｀))')
    '''    
    if 'Kappa' in message.content:
        await client.send_message(message.channel, 'https://static-cdn.jtvnw.net/emoticons/v1/3286/1.0')
        
    if 'WutFace' in message.content:
        await client.send_message(message.channel, 'https://static-cdn.jtvnw.net/emoticons/v1/28087/1.0')
        
    if 'DansGame' in message.content:
        await client.send_message(message.channel, 'https://static-cdn.jtvnw.net/emoticons/v1/33/1.0')
        
    if 'OpieOp' in message.content:
        await client.send_message(message.channel, 'https://tppx.herokuapp.com/emotes/OpieOP.png')
        
    if 'BabyRage' in message.content:
        await client.send_message(message.channel, 'https://static-cdn.jtvnw.net/emoticons/v1/22639/1.0')
        
    if '4Head' in message.content:
        await client.send_message(message.channel, 'https://static-cdn.jtvnw.net/emoticons/v1/354/1.0')
        
    if 'MingLee' in message.content:
        await client.send_message(message.channel, 'https://static-cdn.jtvnw.net/emoticons/v1/68856/1.0')
        
    if 'BibleThump' in message.content:
        await client.send_message(message.channel, 'https://static-cdn.jtvnw.net/emoticons/v1/86/2.0')
        
    if 'haHAA' in message.content:
        await client.send_message(message.channel, 'http://images.akamai.steamusercontent.com/ugc/704037974368566170/B2C108C08257988EF3C3DDBBE88EAC2D9ACD2F5D/')
        
    if 'PogChamp' in message.content:
        await client.send_message(message.channel, 'http://static-cdn.jtvnw.net/emoticons/v1/88/1.0')
        
    if 'FeelsGoodMan' in message.content or 'feelsgoodman' in message.content or 'Feelsgoodman' in message.content:
        await client.send_message(message.channel, 'https://cdn.betterttv.net/emote/566c9fde65dbbdab32ec053e/1x')
        
    if 'FeelsBadMan' in message.content or 'feelsbadman' in message.content or 'Feelsbadman' in message.content:
        await client.send_message(message.channel, 'http://i.imgur.com/e8JnaSY.png')
        
    if 'FeelsBirthdayMan' in message.content or 'feelsbirthdayman' in message.content or 'Feelsbirthdayman' in message.content:
        await client.send_message(message.channel, 'https://cdn.betterttv.net/emote/55b6524154eefd53777b2580/1x')
        
    if 'FeelsAngryMan' in message.content or 'feelsangryman' in message.content or 'Feelsangryman' in message.content:
        await client.send_message(message.channel, 'http://i.imgur.com/dG3TMFB.png')
        
    if '(╯°□°）╯︵ ┻━┻' in message.content or '(╯°□°）╯︵ ┻━━┻' in message.content:
        if AI==0:
            await client.send_message(message.channel, ' ┬──┬◡ﾉ(° -°ﾉ)'+' Calm down, '+(author.mention))
        elif AI == 1:
            await client.send_message(message.channel, ' ┬──┬◡ﾉ(° -°ﾉ)'+' I really wish you people would stop doing this, '+(author.mention))
        elif AI == 2:
            await client.send_message(message.channel, ' ┬──┬◡ﾉ(° -°ﾉ)'+' Theres no reason to harm this poor table, '+(author.mention))
        elif AI == 3:
            await client.send_message(message.channel, ' ┬──┬◡ﾉ(° -°ﾉ)'+' One of these days I am going to snap.. '+(author.mention))
        elif AI == 4:
            await client.send_message(message.channel, ' （╯°□°）╯︵(\ .o.)\' LETS SEE HOW YOU LIKE BEING FLIPPED!'+(author.mention))
        elif AI == 5:
            await client.send_message(message.channel, ' （╯°□°）╯︵(\ .o.)\' WHY MUST YOU TEST MY PATIENCE!'+(author.mention))

    if '( ͡° ͜ʖ ͡°)' in message.content:
        await client.send_message(message.channel, ' (  ͡° ͜ʖ ͡° ) '+(author.mention))
        
    if '!post this every' in message.content:
        if 'http' in message.content:
            Num = message
            var2 = author
            
            await client.send_message(message.channel, 'Link recorded. I will post it here periodically in the duration provided. Leave it to me '+(author.mention))
            StrippedCommand = (message.content.strip('!post this every '))
            TimeProvided = StrippedCommand[0:StrippedCommand.index(' ')]
                        
            IndexOFPIPE = message.content.index('|')
            Url = message.content[IndexOFPIPE+2:-1]+message.content[-1:]
            
            client.loop.create_task(AutoLinkPoster(TimeProvided, Url, Num, var2))
            
        else:
            await client.send_message(message.channel, 'A valid link was not provided. Please check that the url and syntax is correct')
    
    if '!print all server members' in message.content:
        await client.send_message(message.channel, 'On terminal all the members of this server has been printed out')
        for person in message.server.members:
            print (person.id)
        
    if '!repeat this every' in message.content:
            Num = message
            var2 = author
            
            await client.send_message(message.channel, 'Macro recorded. I will post it here periodically in the duration provided. Leave it to me '+(author.mention))
            StrippedCommand = (message.content.strip('!repeat this every '))
            TimeProvided = StrippedCommand[0:StrippedCommand.index(' ')]
            
            IndexOFPIPE = message.content.index('|')
            Url = message.content[IndexOFPIPE+2:-1]+message.content[-1:]
            
            client.loop.create_task(AutoMacroPoster(TimeProvided, Url, Num, var2))
    '''        
    if '!Alert Me' in message.content and 'Selezar' not in str(author):
        MyVar2 = author
        await client.send_message(message.channel, ('```Command understood. I will send you a private message the minute servers are up. ```' ))
        client.loop.create_task(AlertWhenServerUp(MyVar2))

    if '!Stalk' in message.content and 'Selezar' not in str(author):
        MyVar1 = message
        MyVar2 = author
        Stalked = message.content[7:-1]+message.content[-1:]
        ThisList = StalkAriesForum(MyVar1,MyVar2, Stalked)
        if ThisList[1] == '':
            ThisList[1] = ' ??? '
        await client.send_message(message.channel, '```'+Stalked[Stalked.index('-'):]+' || '+'Current Activity:'+ThisList[1]+' | Last Active At:'+ThisList[0]+'```')
        
    if '!Latest Update' in message.content and 'Selezar' not in str(author):
        MyVar1 = message
        MyVar2 = author

        await client.send_message(message.channel, ('Searching forum for latest patch notes...   '+(author.mention)) )
        UpdateList = GameUpdatesForum()
        s = '\n'
        MyString = s.join(UpdateList)
        
        await client.send_message(message.channel, '```'+MyString+'```')
        
    if '!Subscribe Thread' in message.content and 'Selezar' not in str(author):
        MyVar1 = message
        MyVar2 = author
        FORUMURL = message.content[18:message.content.index('MONITOR')]
        Persons = message.content[message.content.index('MONITOR')+8:]
        await client.send_message(message.channel, '```You have been subscribed to this thread. I will DM you when '+Persons+' sees this thread```')
        client.loop.create_task(MonitorForumThread(MyVar1, FORUMURL, Persons))

        
            




if __name__ == '__main__':
    print ('Initialising Discord Bot')
    email = 'ekram_lol@hotmail.com'
    password = 'batman211'
    client.login(email, password)
    client.accept_invite('https://discord.gg/aYhuDWH')
    client.run(email, password)
