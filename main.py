import discord
import asyncio
from discord import FFmpegPCMAudio

token = 'MTM0ODM1ODE3NDcwMDMzOTI5MQ.GBhZw6.mu8i-yvSYsOG8keUEnDXoHf9U1tlewC1Sn_-5M'

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.content.startswith('$eae'):
            await message.channel.send('bom dia patriota!')
        
    async def on_voice_state_update(self, member, before, after):
        # Check if the member joins a voice channel and matches the specific ID
        membro = member.name
        if (before.channel == None) and (membro == 'calicute_'):
            
            # Connect to the voice channel
            channel = after.channel
            voice_channel = await channel.connect()

            # Play the audio file
            audio = FFmpegPCMAudio('jamal.mp3')
            voice_channel.play(audio)

            # Optionally, disconnect after a short duration
            await asyncio.sleep(10)  # Adjust time based on the length of the audio
            await voice_channel.disconnect()

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)