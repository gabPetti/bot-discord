import discord
import asyncio
from openai import OpenAI
from discord import FFmpegPCMAudio
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ["TOKEN"]
openaiToken = os.environ["AIKEY"]

client = genai.Client(api_key=AIKEY)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.content.startswith('$eae'):
            await message.channel.send('bom dia patriota!')

        if message.content.startswith('$piada'):
            response = client.models.generate_content(
                model="gemini-2.0-flash", contents="Conte uma piada boa em até 5 sentenças"
            )
            await message.channel.send(response.text)
            
        
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