'''
Bot created for dicord

'''


import discord
import asyncio
import multiprocessing


client = discord.Client()

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


async def AutoLinkPoster(var1, url, Num, var2):
    
    Duration = int(var1)
    await client.wait_until_ready()
    #channel = discord.Object(id=Num)

    while not client.is_closed:
        await client.send_message(Num.channel, (var2.mention+' '+url))
        await asyncio.sleep(Duration) # task runs every 60 seconds or the duration provided
        
async def AutoMacroPoster(var1, url, Num, var2):
    
    Duration = int(var1)
    await client.wait_until_ready()
   # channel = discord.Object(id=Num)

    while not client.is_closed:
        await client.send_message(Num.channel, url)
        await asyncio.sleep(Duration) # task runs every 60 seconds or the duration provided
        
        
async def AlertWhenServerUp(MyVar2):
    '''
    This will run as a background task and an be called mutliple times by different people. It accepts the channel id and the user name who called it through on_message. It will crawl aries homepage and check to see if it is online every minute. If it is, then the infinite loop will exit and a message to the user who called this will be sent saying that servers are up
    '''
    await client.wait_until_ready()
    while True:
        ''' This loop will continue looping and scraping aries front website to see if server is online. If it is, then it will break the loop and alert person who called this func'''
        #Place to crawl front page to see if website is up or not
        
    
        await asyncio.sleep(60) # task runs every 60 seconds or the duration provided
        
    ''' Sending the alert message to the author since servers are up now'''
    await client.send_message(MyVar2, 'The servers are up now. Hope I was useful to you. If you have any other useful alert ideas then DM them to Selezar. Enjoy!')
  
  
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
    

@client.event
async def on_message(message):
    author = message.author
    try:
        print ('Message from: '+str(author)+' : '+str(message.content)+' | '+str(message.server)+' | '+str(message.channel))
    except UnicodeEncodeError:
        pass
    
    if 'Greet Me' in message.content:
        await client.send_message(message.channel, ('How are you doing, '+(author.mention)+' ?') )
        
    if 'Good and you?' in message.content:
        await client.send_message(message.channel, 'I am well. What is my purpose?')
        
    if 'You post memes only' in message.content:
        await client.send_message(message.channel, 'I post memes only? Oh my god ((´д｀))')
        
    if 'Kappa' in message.content:
        await client.send_message(message.channel, 'https://static-cdn.jtvnw.net/emoticons/v1/2867/3.0')
        
    if 'PogChamp' in message.content:
        await client.send_message(message.channel, 'https://static-cdn.jtvnw.net/emoticons/v1/88/3.0')
        
    if 'FeelsGoodMan' in message.content or 'feelsgoodman' in message.content or 'Feelsgoodman' in message.content:
        await client.send_message(message.channel, 'http://i.imgur.com/xe9OmYW.png')
        
    if 'FeelsBadMan' in message.content or 'feelsbadman' in message.content or 'Feelsbadman' in message.content:
        await client.send_message(message.channel, 'http://i.imgur.com/4sDbxbJ.png')
        
    if 'FeelsAngryMan' in message.content or 'feelsangryman' in message.content or 'Feelsangryman' in message.content:
        await client.send_message(message.channel, 'http://i.imgur.com/dG3TMFB.png')
        
    if '(╯°□°）╯︵ ┻━┻' in message.content:
        await client.send_message(message.channel, ' ┬──┬◡ﾉ(° -°ﾉ)'+'Calm down, '+(author.mention))
        
    if '!post this every' in message.content:
        if 'http' in message.content:
            Num = message
            var2 = author
            
            await client.send_message(message.channel, 'Link recorded. I will post it here periodically in the duration provided. Leave it to me '+(author.mention))
            StrippedCommand = (message.content.strip('!post this every '))
            TimeProvided = StrippedCommand[0:StrippedCommand.index(' ')]
            Url = StrippedCommand.strip(TimeProvided+' | ')
            
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
            Url = StrippedCommand.strip(TimeProvided+' | ')
            
            client.loop.create_task(AutoMacroPoster(TimeProvided, Url, Num, var2))
            
    if '!Are the forums up?' in message.content or '!ping forums' in message.content:
        if ping("http://aries.elluel.net/") == True:
            await client.send_message(message.channel, ('The servers are up and functioning, '+(author.mention)) )
        elif  ping("http://aries.elluel.net/") == False:
            await client.send_message(message.channel, ('Forums are still down but are being worked upon currently, '+(author.mention)) )
            
    if '!Alert Me' in message.content:
        MyVar2 = author
        await client.send_message(message.channel, ('Command understood. I will send you a private message the minute servers are up. '+(author.mention)) )
        client.loop.create_task(AlertWhenServerUp(MyVar2))

            




if __name__ == '__main__':
    email = 'place the email id of your bot here'
    password = 'place the password of your bot here'
    client.login(email, password)
    client.accept_invite('https://discord.gg/aYhuDWH')
    client.run(email, password)
