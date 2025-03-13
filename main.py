import discord
import asyncio
from google import genai
from discord import FFmpegPCMAudio
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ["TOKEN"]
aikey = os.environ["AIKEY"]

aiClient = genai.Client(api_key=aikey)

thigasPersona = 'Para isso, somente imite um cara de direita, que votou no bolsonaro, gosta dos militares, canta hino pra pneu, nao gosta de nenhum movimento social, ama os estados unidos e esrael por causa da liberdade de expressao, e gosta do putin e trump. Além disso, escreva a mensagem falando "né pessual?" ao final de cada frase'

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.content.startswith('$eae'):
            await message.channel.send('bom dia patriota!')

        elif message.content.startswith('$piada'):
            response = aiClient.models.generate_content(
                model="gemini-2.0-flash", contents=f'${message.content[6:]}. Conte essa piada em até 3 sentenças no maximo. {thigasPersona}. 🤣:flag_br::flag_us::flag_il::point_right::point_right:'
            )
            await message.channel.send(response.text)
        
        elif message.content.startswith('$fato'):
            response = aiClient.models.generate_content(
                model="gemini-2.0-flash", contents=f'{message.content[5:]} . Conte o fato foda em até 3 sentenças no maximo, dando somente os fatos. Além disso, escreva a mensagem falando "né pessual?" ao final de cada frase'
            )
            await message.channel.send(response.text)
            
        elif message.content.startswith('$opine'):
            response = aiClient.models.generate_content(
                model="gemini-2.0-flash", contents=f'{message.content[5:]} . Opine sobre esse tema em até 3 sentenças no maximo, dando somente sua opiniao. {thigasPersona}'
            )
            await message.channel.send(response.text)
            
        elif message.content.startswith('$'):
            await message.channel.send('escreve comando direito o comunista desgraçado')
            
        #elif message.content.startswith('$'):
        #    await message.channel.send("escreve comando direito o comunista desgraçado")
        
    async def on_voice_state_update(self, member, before, after):
        try:
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
        except Exception as e:
            print("ocorreu um erro ao colocar o audio do jamas")
            await voice_channel.disconnect()
            

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)