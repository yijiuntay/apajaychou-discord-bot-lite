import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.command()
async def hello(ctx):
  await ctx.send("Apa Jaychou!")


@client.command(pass_context=True)
async def join(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("You need to be in a voice channel to use this command.")


@client.command(pass_context=True)
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("Jay Out")
  else:
    await ctx.send("I'm not in a voice channel")


@client.command()
async def multiq(ctx, *, message: str):
  queue = []
  songs = message.split("\n")
  for song in songs:
    try:
      if int(song[0]):
        queue.append({
          'title': song.split(".")[1],
          'sequence': int(song.split(".")[0])
        })
    except ValueError:
      queue.append({'title': song, 'sequence': 0})

  def getSequence(e):
    return e['sequence']

  queue.sort(key=getSequence)
  print(queue)

  for item in queue:
    await ctx.send("m!play " + item['title'])

client.run(os.environ['BOT_TOKEN'])
