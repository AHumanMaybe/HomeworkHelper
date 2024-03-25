import os
import dotenv
import discord
from discord.ext import commands
from discord import Interaction
from openai import OpenAI
import wolframalpha

wfclient = wolframalpha.Client('XR7X24-7VAK8HEGJQ')

dotenv.load_dotenv()

KEY = os.getenv("OPEN_API_KEY")
openClient = OpenAI(api_key=KEY)

chat_log = [{"role":"system", "content": "you are a homework assistance AI designed to provide support for people working on school assignments"}]

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

@client.command()
async def solve(ctx, *msg):
    query = " ".join(msg)
    res = wfclient.query(query)
    try:
        output = next(res.results).text
        await ctx.send(output)
    except StopIteration:
        await ctx.send("Stop Iteration Error Raised Bitch")

client.run("MTE4NzIxMjQ5NTcwMjczNjkyNg.Gi9IX3.U-CXspVZ9qgdlwdV_F9TSUNwjDkYScAVJkzG7c")