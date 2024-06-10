import discord
from discord.ext import commands
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo-16k",
  messages=[],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Bot settings
TOKEN = 'YOUR_BOT_TOKEN'
PREFIX = '$'
SOME_SETTING = False


# Create bot instance with the specified prefix
bot = commands.Bot(command_prefix=PREFIX)

# Example setting usage (this is just an example and can be adapted to your bot's needs)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    if SOME_SETTING:
        print("Some setting is enabled")
    else:
        print("Some setting is disabled")

# Example command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot with the specified token
bot.run(TOKEN)