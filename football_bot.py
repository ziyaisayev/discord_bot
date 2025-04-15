import discord
import os


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


career_scorers = {
    "cristiano ronaldo": 933,
    "lionel messi": 821,
    "robert lewandowski": 640,
    "karim benzema": 445,
    "zlatan ibrahimović": 573,
    "luis suárez": 540,
    "romário": 753,
    "pelé": 767,
    "ferenc puskás": 746,
    "gerd müller": 735,
    "neymar": 450,
    "edinson cavani": 430,
    "thierry henry": 411,
    "raul": 404,
    "andriy shevchenko": 389,
    "alessandro del piero": 346,
    "samuel eto'o": 426,
    "didier drogba": 366,
    "wayne rooney": 366,
    "kaka": 237,
    "sergio agüero": 379,
    "ruud van nistelrooy": 349,
    "robin van persie": 336,
    "mohamed salah": 320,
    "erling haaland": 245
}


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower().strip()


    for player in career_scorers:
        if player in msg:
            await message.channel.send(f"{player.title()} has scored approximately {career_scorers[player]} goals in their career.")
            break

client.run(os.getenv('TOKEN'))
