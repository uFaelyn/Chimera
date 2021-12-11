import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import tasks, commands
import time
import asyncio
from asyncio.tasks import sleep

songs = ['The sun, the moon, the stars',
          'Painters of the Tempest',
          'The words I never said',
          'Oxalis',
          'Highway to Oblivion',
          'Play with fire (ft. Yacht Money)',
          'Love Nwantiti (ah ah ah)',
          'Flowers',
          'Je te laisserai des mots',
          'Infinity',
          'Galaxy Collapse',
          'Blue Zenith',
          'Yomi Yori',
          'Freedom Dive']

poiu = random.choice(songs)

client = commands.Bot(command_prefix="-", 
          help_command = None,
          
          activity = discord.Activity(type=discord.ActivityType.listening, name=str(poiu)))
    

name = ['Chimera']
skin = [' skin', ' Skin']
WYSI = ['727']
tiktok_beatmaps = ['virginity syndrome']

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    poiu = random.choice(songs)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=str(poiu)))

    bert = client.get_channel(898815070207877133)
    await bert.send('I have come online once more')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mc = message.channel
    msg = message.content
    msgl = message.content.lower()

    if (any(word in msg for word in WYSI)):
        await mc.send('WYSI')

    if (any(word in msg for word in tiktok_beatmaps)) or ('where' in msgl and 'maps' in msgl):
        await mc.send('All of the beatmaps are very accessible if you read the channel names and use any form of problem solving. <#810996735274254337> Good day :D')

    if 'where' in msgl and 'skin' in msgl:
        await mc.send('Do !skin in <#898404919164403732> to get Davolafs skin')
    
    if message.channel.id == 909685766244945921 or '@everyone' in message.content:
        print('Success' , "\n" , message.content)
        if len(message.author.roles) <= 2:
            print('Check 1')
            await message.author.ban(reason = 'Softbanned bozo')
            await message.guild.unban(discord.Object(message.author.id))
            await mc.send(f'{message.author} has been softbanned')
            print('Check 2, softban successful')
            
        elif message.author.id == 591047383044063244:
            return

        elif len(message.author.roles) > 2:
            if message.channel.id == 909685766244945921:
            
                await message.delete()
                print('Seems good')

            else:
              return
    
    await client.process_commands(message)

@client.command()
async def shuffle(ctx):
    poiu = random.choice(songs)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=str(poiu)))
    await ctx.send(f'I am now listening to: {poiu}')


@client.command()
async def help(ctx):
    embed=discord.Embed(title='Chimera Commands', color=0x27005e) 
    
    embed.add_field(name='Rock, Paper, Scissors', value='-rps <arg> ; Play a game of rock, paper,           scissors!', 
    inline=False)

    embed.add_field(name='Advice for osu!', value='-better ; Shows the best way to get better         at osu!', 
    inline=False) 

    embed.add_field(name='Tips for new osu! players', value='-tips ; common mistakes I (Wind) see all           the time', 
    inline=False) 

    embed.add_field(name='RNG 1-100', value='-roll                      <optional phrase> ; Roll a random                   number 1-100', 
    inline=False)

    embed.add_field(name='8 ball', value='-yn <optional                 phrase> ; Classic 8 ball.. just                     Chimera', 
    inline=False)
                                  
    await ctx.send(embed=embed)

@client.command()
async def act(ctx, arg, activity):
    if ctx.author.id == 591047383044063244:
        if arg == 'playing':
            await client.change_presence(activity=discord.Game(name=str(activity)))
            await ctx.send(f'My activity has been changed to "Playing {activity}"')

        elif arg == "listening":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=str(activity)))
            await ctx.send(f'My activity has been changed to "Listening to {activity}"')

        elif arg == 'streaming':
            await client.change_presence(activity=discord.Streaming(name=str(activity)                           , url='https://www.twitch.tv/sevendeadlywinds'))
            await ctx.send(f'My activity has been changed to "Streaming {activity}"')

        elif arg == 'watching':
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(activity)))
            await ctx.send(f'My activity has been changed to "Watching {activity}"')
        else:
            await ctx.send('Invalid Syntax Bozo')

    else:
        await ctx.send('This command is restricted for Wind!')

@client.command()
async def rps(ctx , arg):
    poss = ['rock' , 'paper' , 'scissors']
    comp = random.choice(poss)
    if arg == comp:
        await ctx.send('Draw!')
    elif arg == 'rock':
        if comp == 'scissors':
            await ctx.send(f'I chose {comp}, You win!')
        else:
            await ctx.send(f'I chose {comp}, I win!')
    elif arg == 'paper':
        if comp == 'rock':
            await ctx.send(f'I chose {comp}, You win!')
        else:
            await ctx.send(f'I chose {comp}, I win!')
    elif arg == 'scissors':
        if comp == 'paper':
            await ctx.send(f'I chose {comp}, You win!')
        else:
            await ctx.send(f'I chose {comp}, I win!')

@client.command()
async def better(ctx):
    await ctx.send(
        'The #1 way to get better is to practice. Its like asking how you get better at a sport. Stop thinking there is an easy way around getting better at osu! and just play the game.')

@client.command()
async def tips(ctx):
    embed=discord.Embed(title="Getting better at osu!", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="So, you want to get better at osu? Congratulations.. Here are some common mistakes I see many new players make", color=0x27005e)
    embed.set_author(name="Made by: Wind#0629", url="https://twitter.com/WindsDeadly", icon_url='https://imgur.com/t/osu/ZcvGtex')
    embed.add_field(name="God Complex", value='This is something largely seen in 2 phases. The first day, and the time when your rank is around 100k. **Stop asking** "Is ____ good for <insert playtime or rank here>" because it is likely to be entirely normal.', inline=False)
    embed.add_field(name="Overcomplicating the game.", value="I cannot stress this enough. **You are playing a game about clicking circles**. Stop overcomplicating the game, and just play. Skillsets exist but you can focus on that when you get better at the fundementals", inline=False)
    embed.add_field(name="Trying ridiculous maps.", value="Stop thinking retry spamming 7 stars will make you any better. Challenge yourself, but do not instantly go to 7 stars without even passing a 5 star.", inline=False)
    embed.add_field(name="**Disclaimer**", value="Remember: **This is focused towards new players** so if you do not agree with something, you are either the type of player I am talking about-- or an actually decent player.", inline=False)
    embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

@client.command()
async def roll(ctx):
    await ctx.send(random.randint(1 , 101))

@client.command()
async def yn(ctx):
    o = random.randint(1 , 1001)
    print(o)
    if o in range(1 , 101):
        await ctx.send('Yes')
    if o in range(101 , 201):
        await ctx.send('No')
    if o in range(201 , 301):
        await ctx.send('Maybe')
    if o in range(301 , 401):
        await ctx.send('Maybe not')
    if o in range(401 , 501):
        await ctx.send('It is possible')
    if o in range(501 , 601):
        await ctx.send('Without a doubt')
    if o in range(601 , 701):
        await ctx.send('Probably not')
    if o in range(701 , 801):
        await ctx.send('Absolutely not')
    if o in range(801 , 901):
        await ctx.send('Never')
    if o in range(901 , 1001):
        await ctx.send('Always')


        
@tasks.loop(hours=1)
async def water():
    Nerd = client.get_channel(527876598834135047)
    await Nerd.send('Drink water guys!')


@water.before_loop
async def before_water():
    await client.wait_until_ready()

water.start()
            


keep_alive()
client.run(os.getenv('Key'))
