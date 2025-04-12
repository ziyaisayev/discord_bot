import discord
import os
import requests
import json
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
starter_encouragements = ["Cheer up!", "Hang in there.", "You are a great person / bot!"]
questions = ["How are you?", "How are you doing?", "How has your day been?"]
answers = ["I am fine, thank you!", "I am good, thank you!", "I am doing well, thank you!"]

ucl_winners = {
    "2000": "Real Madrid",
    "2001": "Bayern Munich",
    "2002": "Real Madrid",
    "2003": "AC Milan",
    "2004": "Porto",
    "2005": "Liverpool",
    "2006": "Barcelona",
    "2007": "AC Milan",
    "2008": "Manchester United",
    "2009": "Barcelona",
    "2010": "Inter Milan",
    "2011": "Barcelona",
    "2012": "Chelsea",
    "2013": "Bayern Munich",
    "2014": "Real Madrid",
    "2015": "Barcelona",
    "2016": "Real Madrid",
    "2017": "Real Madrid",
    "2018": "Real Madrid",
    "2019": "Liverpool",
    "2020": "Bayern Munich",
    "2021": "Chelsea",
    "2022": "Real Madrid",
    "2023": "Manchester City",
    "2024": "Real Madrid"
}

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$inspire"):
        q = get_quote()
        await message.channel.send(q)

    if any(word in message.content.lower() for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if any(word in message.content for word in questions):
        await message.channel.send(random.choice(answers))

    if message.content.strip() in ucl_winners:
        winner = ucl_winners[message.content.strip()]
        await message.channel.send(f"The UEFA Champions League winner in {message.content.strip()} was {winner}.")

client.run(os.getenv('TOKEN'))
