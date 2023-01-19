import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord import app_commands
import os
import youtube_dl
import json
import random
import time


#set the client and the chdir
intents = discord.Intents().all()
bot = commands.Bot(command_prefix = "!?!", intents = intents)
os.chdir(r"/home/pioucraft/Documents/programinc/discord-bot-main/")

#initialize the bot
@bot.event
async def on_ready():
    print("bot is ready")
    #sync commands
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception as e:
        print(f"failed to sync commands: {e}")



#/play command
@bot.tree.command(name=f"play", description="le bot va jouer la musique de ton choix")
async def play(interaction: discord.Interaction, music: str):
    if (interaction.user.voice):
        await interaction.response.send_message("je vais faire de mon mieux pour te satisfaire")
        channel = interaction.user.voice.channel
        voice = await channel.connect()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': 'bestaudio'}
        if music.startswith("https://"):
            #load an url
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(music, download=False)
                url2 = info['formats'][0]['url']
        else:
            #search on youtube
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                url = f"ytsearch: {music}"
                info = ydl.extract_info(url, download=False)['entries'][0]
                url2 = info['formats'][0]["url"]
        #play the music
        source = FFmpegPCMAudio(url2, **FFMPEG_OPTIONS)
        player = voice.play(source)

    else:
        await interaction.response.send_message("merci de rejoindre un salon vocal et de réessayer la commande")

#stop the music
@bot.tree.command(name="stop-music", description="le bot va arrêter de jouer la musique")
async def level(interaction: discord.Interaction):
    await interaction.response.send_message("j'essaie d'arrêter la musique")
    if (interaction.user.voice):
        await interaction.guild.voice_client.disconnect()



#show the level of the user
@bot.tree.command(name="level", description="affiche ton niveau ou celui d'un autre utilisateur")
async def level(interaction: discord.Interaction, user: discord.User):
    with open("users.json", "r") as f:
        users = json.load(f)
    
    #set an embed
    embed = discord.Embed(type = "rich", title = "niveau", description = f"{user.mention} est niveau {users[str(user.id)]['level']} et a {users[str(user.id)]['experience']} xp", color=0x2e60aa)
    embed.set_image(url = "https://media.tenor.com/iS-rIkKhpMgAAAAd/god-bless-america-american-flag.gif")
    await interaction.response.send_message(embed=embed)

#show the exact level of the user
@bot.tree.command(name="exactlevel", description="affiche ton niveau exact ou celui d'un autre utilisateur avec des décimales")
async def level(interaction: discord.Interaction, user: discord.User):
    with open("users.json", "r") as f:
        users = json.load(f)
    
    #set an embed
    embed = discord.Embed(type = "rich", title = "niveau exact", description = f"{user.mention} est niveau {str(float(users[str(user.id)]['experience']) ** (1/4))} et a {users[str(user.id)]['experience']} xp", color=0x2e60aa)
    embed.set_image(url = "https://media.tenor.com/iS-rIkKhpMgAAAAd/god-bless-america-american-flag.gif")
    await interaction.response.send_message(embed=embed)


#welcome message
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1062012487173681152)
    bienvenue = bot.get_channel(1050103281315233852)
    #set an embed
    embed = discord.Embed(type = "rich", title = "bienvenue", description = f"bienvenue {member.mention} sur america, n'oublie pas de regarder {bienvenue.mention}", color=0x2e60aa)
    embed.set_image(url = "https://media.tenor.com/iS-rIkKhpMgAAAAd/god-bless-america-american-flag.gif")
    await channel.send(embed=embed)




#quoifeur and xp
@bot.event
async def on_message(message):
    message.content = message.content
    message.content = message.content.lower()
    message.content = message.content.replace("kwa", "quoi")
    message.content = message.content.replace("qwa", "quoi")
    message.content = message.content.replace("koi", "quoi")
    message.content = message.content.replace("kaka", "caca")
    message.content = message.content.replace("oe", "ouais")
    message.content = message.content.replace(" ", "")
    message.content = message.content.replace("!", "")
    message.content = message.content.replace("?", "")
    message.content = message.content.replace("?", "")
    if not message.author.bot:
            with open("users.json", "r") as f:
                users = json.load(f)
    
            letters = len(message.content)
            if letters > 40:
                letters = 40
            await update_data(users, message.author, letters)
            users[str(message.author.id)]["experience"] = users[str(message.author.id)]["experience"] + letters
            await level_up(users, message.author, message.channel)

            with open("users.json", "w") as f:
                json.dump(users, f, indent=4)


            if message.content.endswith('quoi'):
                await message.channel.send("feur")
                print("feur")
            if message.content.endswith('non'):
                await message.channel.send("bril")
                print("bril")
            if message.content.endswith('oui'):
                await message.channel.send("stiti")
                print("stiti")
            if message.content.endswith('caca'):
                await message.channel.send("mogus")
                print("mogus")
            if message.content.endswith('ouais'):
                await message.channel.send("stern")
                print("stern")




#update the user data if not in users.json
async def update_data(users, user, letters):
    if not user.bot:
        if not str(user.id) in users:
            users[str(user.id)] = {}
        if not "experience" in users[str(user.id)]:
            users[str(user.id)]["experience"] = letters
            users[str(user.id)]["level"] = 1

#level up the user if enough xp
async def level_up(users, user, channel):
    experience = users[str(user.id)]["experience"]
    lvl_start = users[str(user.id)]["level"]
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await channel.send("{} a atteint le niveau {}".format(user.mention, lvl_end))
        users[str(user.id)]["level"] = lvl_end

        #add roles
        if lvl_end >= 5 and not discord.utils.get(user.guild.roles, name="americain bg") in user.roles:
            await channel.send("bravo {} tu as atteint le niveau 5, tu vas donc recevoir le role americain bg".format(user.mention))
            await user.add_roles(discord.utils.get(user.guild.roles, name="americain bg"))

        if lvl_end >= 10 and not discord.utils.get(user.guild.roles, name="americain très bg") in user.roles:
            await channel.send("bravo {} tu as atteint le niveau 10, tu vas donc recevoir le role americain très bg".format(user.mention))
            await user.add_roles(discord.utils.get(user.guild.roles, name="americain très bg"))

        if lvl_end >= 15 and not discord.utils.get(user.guild.roles, name="americain ultra mega bg") in user.roles:
            await channel.send("bravo {} tu as atteint le niveau 15, tu vas donc recevoir le role americain ultra mega bg".format(user.mention))
            await user.add_roles(discord.utils.get(user.guild.roles, name="americain ultra mega bg"))
        
        if lvl_end >= 20 and not discord.utils.get(user.guild.roles, name="tah l'americain") in user.roles:
            await channel.send("bravo {} tu as atteint le niveau 20, tu vas donc recevoir le role americain tah l'americain".format(user.mention))
            await user.add_roles(discord.utils.get(user.guild.roles, name="tah l'americain"))
            

'''
politics part

'''
#/drop command
@bot.tree.command(name="drop", description="drop une lootbox avec des politiciens et des armes dedans")
async def drop(interaction: discord.interactions):
    with open("users.json", "r") as f:
        users = json.load(f)
    await update_politic_data(interaction.user, users)
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)
    if time.time() - users[str(interaction.user.id)]["politics"]["lastdrop"] != 30 * 60:
        with open("politics.json", "r") as f:
            politics = json.load(f)
        #get a politic
        if random.randint(1, 1) == 2:
            politic = random.randint(0, 45)
            politic_name = politics[politic]["presidentName"]
            party = politics[politic]["politicalParty"]
            politic_id = str(politics[politic]["_id"])
            embed = discord.Embed(type = "rich", title = politic_name, description = f"bravo, tu as gagneé {politic_name} du parti {party}", color=0x2e60aa)
            embed.set_image(url = politics[politic]["imgThumb"])
            await interaction.response.send_message(embed=embed)

            #save the politic to the users.json
            with open("users.json", "r") as f:
                    users = json.load(f)
            if not politic_id in users[str(interaction.user.id)]["politics"]:
                users[str(interaction.user.id)]["politics"]["number"] += 1
                users[str(interaction.user.id)]["politics"][politic_id] = True
                users[str(interaction.user.id)]["politics"]["lastdrop"] = time.time()
                with open("users.json", "w") as f:
                    json.dump(users, f, indent=4)
            else:
                await interaction.response.send_message("tu as déja ce politicien")

        #get a gun
        elif random.randint(1, 1) == 1:
            with open("guns.json", "r") as f:
                guns = json.load(f)
            gun = random.randint(0, 9)
            gun_name = guns[gun]["name"]
            rarity = random.randint(1, 5)
            basefirerate = random.randint(10, 100)
            firerate = basefirerate * rarity
            embed = discord.Embed(type="rich", title=gun_name, description=f"bravo tu as gagné un/une {gun_name} qui fait {str(firerate)} dégats par seconde et qui est de rareté {await rarity_name(rarity)}")
            await interaction.response.send_message(embed=embed)

            #store the data of the guns into users.json
            with open("users.json", "r") as f:
                users = json.load(f)
            await update_politic_data(interaction.user, users)
            gun_id = users[str(interaction.user.id)]["guns"]["number"]
            users[str(interaction.user.id)]["guns"]["number"] += 1
            users[str(interaction.user.id)]["guns"][gun_id] = {}
            users[str(interaction.user.id)]["guns"][gun_id]["rarity"] = str(rarity)
            users[str(interaction.user.id)]["guns"][gun_id]["basefirerate"] = str(basefirerate)
            users[str(interaction.user.id)]["guns"][gun_id]["firerate"] = str(firerate)
            users[str(interaction.user.id)]["guns"][gun_id]["_id"] = guns[gun]["_id"]
        
            users[str(interaction.user.id)]["politics"]["lastdrop"] = time.time()
            with open("users.json", "w") as f:
                json.dump(users, f, indent=4)

        #get money
        elif random.randint(1, 1) == 1:
            money = random.randint(1, 100)
            await interaction.response.send_message(f"bravo tu as gagné {str(money)} $")
            with open("users.json", "r") as f:
                users = json.load(f)
            await update_politic_data(interaction.user, users)
            users[str(interaction.user.id)]["politics"]["lastdrop"] = time.time()
            users[str(interaction.user.id)]["money"] = int(users[str(interaction.user.id)]["money"]) + money
            with open("users.json", "w") as f:
                json.dump(users, f, indent=4)

    else: 
        waitime = int(30 - ((time.time() - users[str(interaction.user.id)]["politics"]["lastdrop"]) / 60)) 
        await interaction.response.send_message(f"tu dois encore attendre {waitime} minutes avant ton prochain drop")
#show the money
@bot.tree.command(name="money", description="montre l'argent d'un utilisateur")
async def drop(interaction: discord.interactions, user: discord.User):
    with open("users.json", "r") as f:
            users = json.load(f)
    embed = discord.Embed(type = "rich", title = "argent", description = f"{user.mention} a {users[str(user.id)]['money']} $", color=0x2e60aa)
    embed.set_image(url = "https://media.tenor.com/iS-rIkKhpMgAAAAd/god-bless-america-american-flag.gif")
    await interaction.response.send_message(embed=embed)
    

#pay someone
@bot.tree.command(name="pay", description="envoyer de l'argent a un autre utilisateur")
async def pay(interaction: discord.Interaction, receiver: discord.User, amount: int):
    with open("users.json", "r") as f:
        users = json.load(f)
    if users[str(interaction.user.id)]["money"] < amount:
        await interaction.response.send_message("tu n'as pas assez d'argent")
    elif str(amount).startswith("-"):
        await interaction.response.send_message("tu ne peux pas envoyer un nombre négatif d'argent")
    else:
        await update_politic_data(receiver, users)
        users[str(interaction.user.id)]["money"] -= amount
        users[str(receiver.id)]["money"] += amount
        await interaction.response.send_message(f"{amount}$ ont étés transférés a {receiver.mention}")
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)




async def update_politic_data(user, users):
    if not user.bot:
        if not str(user.id) in users:
            users[str(user.id)] = {}
        if not "politics" in users[str(user.id)]:
            users[str(user.id)]["money"] = 1
            users[str(user.id)]["guns"] = {}
            users[str(user.id)]["guns"]["number"] = 0
            users[str(user.id)]["politics"] = {}
            users[str(user.id)]["politics"]["number"] = 0
            users[str(user.id)]["politics"]["lastdrop"] = 0

async def rarity_name(rarity):
    if rarity == 1:
        rarity = "common"
    elif rarity == 2:
        rarity = "uncommon"
    elif rarity == 3:
        rarity = "rare"
    elif rarity == 4:
        rarity = "epic"
    elif rarity == 5:
        rarity = "legendary"
    return rarity

#run the bot with the token
bot.run(token)