import discord
import os

from dotenv import load_dotenv, find_dotenv


intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.presences = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

def code(env_code_name):
    load_dotenv(find_dotenv())
    try:
        return os.environ.get(env_code_name)
    except(TypeError):
        print('Make sure project directory contains .env file.')


try:
    client.run(code('CODE'))
except(TypeError):
    print('',
          'Failure to start.',
          'Make sure project directory contains .env file.',
          sep = '\n')
except(discord.errors.LoginFailure):
    print('',
          'Invalid token was given.',
          'Make sure token is entered correctly/not expired.',
          sep = '\n')
