import discord
import asyncio
from openai import OpenAI
from discord import FFmpegPCMAudio
import os

token = os.environ["TOKEN"]
openaiToken = os.environ["OPENAI"]

openaiClient = OpenAI(
  api_key=openaiToken,
  base_url="https://api.deepseek.com"
)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.content.startswith('$eae'):
            await message.channel.send('bom dia patriota!')

        if message.content.startswith('$piada'):
            completion = await openaiClient.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": "Conte uma piada boa em até 5 sentenças",
                    },
                ],
            )
            print(completion.choices[0].message.content)
            await message.channel.send(completion.choices[0].message.content)
            
        
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