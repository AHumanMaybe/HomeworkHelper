import discord
from discord.ext import commands
from discord import Interaction
from openai import OpenAI


KEY = "SECRET"
openClient = OpenAI(api_key=KEY)

chat_log = []

client = commands.Bot(command_prefix=".", intents= discord.Intents.all())


@client.command()
async def do(ctx, *msg):
    chat_log.append({"role": "user", "content": " ".join(msg)})
    response = openClient.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_log
    )
    chat_log.append(response.choices[0].message)
    await ctx.send(response.choices[0].message.content)

client.run("MTE4NzIxMjQ5NTcwMjczNjkyNg.GTWfYH.NcDUXZ2Gexk_kVRAjxr2g1PSH423POTXqgHh_E")