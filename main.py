import discord
import os
import random
from discord.ext import tasks, commands
from time import time

songs = ["The sun, the moon, the stars",
         "Painters of the Tempest",
         "The words I never said",
         "Oxalis",
         "Highway to Oblivion",
         "Play with fire (ft. Yacht Money)",
         "Love Nwantiti (ah ah ah)",
         "Flowers",
         "Je te laisserai des mots",
         "Infinity",
         "Galaxy Collapse",
         "Blue Zenith",
         "Yomi Yori",
         "Freedom Dive"]

shuffleSong = random.choice(songs)

client = commands.Bot(command_prefix="-",
                      help_command=None,
                      activity=discord.Activity(type=discord.ActivityType.listening, name=shuffleSong))

tiktok_beatmaps = ["virginity syndrome"]
spamTriggers = ["@everyone", "@here"]


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    poiu = random.choice(songs)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=shuffleSong))

    bert = client.get_channel(898815070207877133)
    await bert.send("I have come online once more")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mc = message.channel
    msg = message.content
    msgL = message.content.lower()

    if "727" in msg:
        await mc.send("WYSI")

    if (any(word in msg for word in tiktok_beatmaps)) or ("where" in msgL and "maps" in msgL):
        await mc.send("All of the beatmaps are very accessible if you read the channel names and use any form of problem solving. <#810996735274254337> Good day :D")

    if ("where" in msgL) and ("skin" in msgL):
        await mc.send("Do !skin in <#898404919164403732> to get Davolafs skin")

    if (msgL.startswith("hello chimera")) or (msgL.startswith("hi chimera")):
        await mc.send("Hello! What is your name?")

        def check(m):
            return m.channel == mc and not m.author == client.user

        nameMsg = await client.wait_for("message", check=check)
        if any(word in spamTriggers for word in nameMsg.content):
            return
        else:
            await mc.send(f"Hello {nameMsg.content}!")

    if (mc.id == 909685766244945921) or (any(word in msg for word in spamTriggers)):
        try:
            with open("../softbans.log", "a", encoding="utf8") as file:
                file.write(str(time()) + " ||| MESSAGE BEGIN ||| " +
                           msg + " ||| MESSAGE END |||")
        except:
            print("Could not open the softban logging file!")

        if len(message.author.roles) <= 2:
            await message.author.ban(reason="Softbanned bozo")
            await message.guild.unban(discord.Object(message.author.id))
            await mc.send(f"{message.author} has been softbanned")

        elif message.author.id == 591047383044063244:
            return

        elif len(message.author.roles) > 2:
            if message.channel.id == 909685766244945921:
                await message.delete()
            else:
                return
    await client.process_commands(message)


@client.command()
async def shuffle(ctx):
    shuffleSong = random.choice(songs)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=str(shuffleSong)))
    await ctx.send(f"I am now listening to: {shuffleSong}")


@client.command()
async def help(ctx):
    embed = discord.Embed(title="Chimera Commands", color=0x27005e)

    embed.add_field(name="Rock, Paper, Scissors", value="-rps <arg> ; Play a game of rock, paper,           scissors!",
                    inline=False)

    embed.add_field(name="Advice for osu!", value="-better ; Shows the best way to get better         at osu!",
                    inline=False)

    embed.add_field(name="Tips for new osu! players", value="-tips ; common mistakes I (Wind) see all           the time",
                    inline=False)

    embed.add_field(name="RNG 1-100", value="-roll                      <optional phrase> ; Roll a random                   number 1-100",
                    inline=False)

    embed.add_field(name="8 ball", value="-yn <optional                 phrase> ; Classic 8 ball.. just                     Chimera",
                    inline=False)

    await ctx.send(embed=embed)


@client.command()
async def act(ctx, arg, * , activity):
    if ctx.author.id == 591047383044063244:
        argLower = arg.lower()

        if argLower == "playing":
            await client.change_presence(activity=discord.Game(name=str(activity)))
            await ctx.send(f"My activity has been changed to 'Playing {activity}'")

        elif argLower == "listening":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=str(activity)))
            await ctx.send(f"My activity has been changed to 'Listening to {activity}'")

        elif argLower == "streaming":
            await client.change_presence(activity=discord.Streaming(name=str(activity), url="https://www.twitch.tv/sevendeadlywinds"))
            await ctx.send(f"My activity has been changed to 'Streaming {activity}'")

        elif argLower == "watching":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(activity)))
            await ctx.send(f"My activity has been changed to 'Watching {activity}'")

        else:
            await ctx.send("Invalid Syntax Bozo")

    else:
        await ctx.send("This command is restricted for Wind!")


@client.command()
async def rps(ctx, arg):
    poss = ["rock", "paper", "scissors"]
    comp = random.choice(poss)
    if ctx.author.id == 591047383044063244:
        await ctx.send(f"I chose {comp}- Oh its you Wind... You win :/")

    elif arg.lower() == comp:
        await ctx.send("Draw!")

    elif arg.lower() == "rock":
        if comp == "scissors":
            await ctx.send(f"I chose {comp}, You win!")
        else:
            await ctx.send(f"I chose {comp}, I win!")
    elif arg.lower() == "paper":
        if comp == "rock":
            await ctx.send(f"I chose {comp}, You win!")
        else:
            await ctx.send(f"I chose {comp}, I win!")
    elif arg.lower() == "scissors":
        if comp == "paper":
            await ctx.send(f"I chose {comp}, You win!")
        else:
            await ctx.send(f"I chose {comp}, I win!")

    else:
        await ctx.send(f"You did that wrong.. its rock, paper, or scissors bozo.")


@client.command()
async def better(ctx):
    await ctx.send(
        "The #1 way to get better is to practice. Its like asking how you get better at a sport. Stop thinking there is an easy way around getting better at osu! and just play the game.")


@client.command()
async def tips(ctx):
    embed = discord.Embed(title="Getting better at osu!", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                          description="So, you want to get better at osu? Congratulations.. Here are some common mistakes I see many new players make", color=0x27005e)

    embed.set_author(name="Made by: Wind#0629", url="https://twitter.com/WindsDeadly",
                     icon_url="https://imgur.com/t/osu/ZcvGtex")

    embed.add_field(name="God Complex",
                    value="This is something largely seen in 2 phases. The first day, and the time when your rank is around 100k. **Stop asking** 'Is ____ good for <insert playtime or rank here>' because it is likely to be entirely normal.", inline=False)

    embed.add_field(name="Overcomplicating the game.",
                    value="I cannot stress this enough. **You are playing a game about clicking circles**. Stop overcomplicating the game, and just play. Skillsets exist but you can focus on that when you get better at the fundementals", inline=False)

    embed.add_field(name="Trying ridiculous maps.",
                    value="Stop thinking retry spamming 7 stars will make you any better. Challenge yourself, but do not instantly go to 7 stars without even passing a 5 star.", inline=False)

    embed.add_field(name="**Disclaimer**",
                    value="Remember: **This is focused towards new players** so if you do not agree with something, you are either the type of player I am talking about-- or an actually decent player.", inline=False)

    embed.set_footer(
        text=f"Information requested by: {ctx.author.display_name}")
    await ctx.send(embed=embed)


@client.command()
async def roll(ctx):
    await ctx.send(random.randint(1, 101))


@client.command()
async def say(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)


@client.command(name="2b")
async def toBe(ctx):
    await ctx.send("To be, or not to be, that is the question: Whether tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles and by opposing, end them")


@client.command()
async def yn(ctx):
    o = random.randint(1, 1001)
    print(o)
    if o in range(1, 101):
        await ctx.send("Yes")
    if o in range(101, 201):
        await ctx.send("No")
    if o in range(201, 301):
        await ctx.send("Maybe")
    if o in range(301, 401):
        await ctx.send("Maybe not")
    if o in range(401, 501):
        await ctx.send("It is possible")
    if o in range(501, 601):
        await ctx.send("Without a doubt")
    if o in range(601, 701):
        await ctx.send("Probably not")
    if o in range(701, 801):
        await ctx.send("Absolutely not")
    if o in range(801, 901):
        await ctx.send("Never")
    if o in range(901, 1001):
        await ctx.send("Always")


@client.command()
async def numguess(ctx):
        exceptNumber = random.randint(1 , 101)

        embed = discord.Embed(title="Guess the number that is missing!")
        x = 1
        print("Check 1")
        while x <= 100:
                x = x+1
                print("Check 2")
                if x == exceptNumber:
                        x = x+1
        embed.add_field(name=x)
        print("Check 3")
        

        ctx.send(embed=embed)


@client.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.CommandNotFound):
        return

    elif isinstance(error, commands.CommandOnCooldown):
        error_message = f"This command is on cooldown!"

    elif isinstance(error, commands.MissingPermissions):
        error_message = f"You do not have permission to use this command!"

    elif isinstance(error, commands.UserInputError):
        error_message = f"You did that wrong bozo."

    else:
        error_message = f"Something went wrong.. but I'm not sure what"
        print(error)

    await ctx.send(error_message)


@tasks.loop(hours=1)
async def water():
    remindingChannel = client.get_channel(527876598834135047)
    await remindingChannel.send("Drink water guys!")


@water.before_loop
async def before_water():
    await client.wait_until_ready()





water.start()


client.run(os.getenv("Key"))
