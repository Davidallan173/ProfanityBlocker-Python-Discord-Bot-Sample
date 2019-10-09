import discord
import ProfanityBlocker
import asyncio
import builtins
from ProfanityConfiguration import ProfanityConfiguration

builtins.config = ProfanityConfiguration()
builtins.client = discord.Client()

Licence, Email, Link, Phone = config.GetConfigVar("ProfaneData")
builtins.ProfaneService = ProfanityBlocker.ProfanityService(Licence,EmailFilter=Email, LinkFilter=Link,PhoneFilter=Phone)

@client.event
async def on_message(message):
    Profane = ProfaneService.ParseText(message.content)
    if Profane != message.content:
        if config.GetConfigVar("MessageOnProfane"):
            await message.channel.send(config.GetConfigVar("MessageProfane"))
        if config.GetConfigVar("DeleteOnProfaneMessage"):
            await message.delete()

loop = asyncio.get_event_loop()
loop.run_until_complete(client.start(config.GetConfigVar("BotToken")))