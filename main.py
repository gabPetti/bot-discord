import discord
import asyncio
from google import genai
from discord import FFmpegPCMAudio
import os
from dotenv import load_dotenv
import json

print('startin bot...')
load_dotenv()

token = os.environ["TOKEN"]
aikey = os.environ["AIKEY"]

aiClient = genai.Client(api_key=aikey)

thigasPersona = 'Para isso, somente imite um cara de direita, que votou no bolsonaro, gosta dos militares, canta hino pra pneu, nao gosta de nenhum movimento social, ama os estados unidos e esrael por causa da liberdade de expressao, e gosta do putin e trump. Além disso, escreva a mensagem falando "né pessual?" ao final de cada frase'

def reward(member):
    # Load JSON data from a file
    with open("balance.json", "r") as file:
        data = json.load(file)

    # Increase the 'give' field
    if member not in data:
        data[member] = 10
    else:
        data[member] += 10

    # Save updated data back to the file
    with open("balance.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Updated successfully!")

class MyClient(discord.Client):
    async def on_ready(self):
      try:
        print(f'Logged on as {self.user}!')
      except Exception as e:
        print(e)

    async def on_message(self, message):
        if message.content.startswith('$eae'):
            await message.channel.send('bom dia, patriota!')

        elif message.content.startswith('$piada'):
            response = aiClient.models.generate_content(
                model="gemini-2.0-flash", contents=f'${message.content[6:]}. Conte essa piada em até 3 sentenças no maximo. {thigasPersona}. 🤣:flag_br::flag_us::flag_il::point_right::point_right:'
            )
            await message.channel.send(response.text)
            reward(message.author.name)
        
        elif message.content.startswith('$fato'):
            response = aiClient.models.generate_content(
                model="gemini-2.0-flash", contents=f'{message.content[5:]} . Conte o fato foda em até 3 sentenças no maximo, dando somente os fatos. Além disso, escreva a mensagem falando "né pessual?" ao final de cada frase'
            )
            await message.channel.send(response.text)
            reward(message.author.name)
            
        elif message.content.startswith('$opine'):
            response = aiClient.models.generate_content(
                model="gemini-2.0-flash", contents=f'{message.content[5:]} . Opine sobre esse tema em até 3 sentenças no maximo, dando somente sua opiniao. {thigasPersona}'
            )
            await message.channel.send(response.text)
            reward(message.author.name)

        elif message.content.startswith('$jumpscare'):
            author = message.author
            # search for the author's channel
            if author.voice:
                try:
                    authorChannel = author.voice.channel
                    voice_channel = await authorChannel.connect()

                    audio = FFmpegPCMAudio('jumpscare.mp3')

                    voice_channel.play(audio)

                    await asyncio.sleep(5)
                    await voice_channel.disconnect()
                except Exception as e:
                    print("ocorreu um erro ao colocar o audio do jumpscare: ", e)
                    await voice_channel.disconnect()
            
            else:
                await message.channel.send('O alombado nao na call e quer dar susto nosoto')

        elif message.content == '$grana':
            with open("balance.json", "r") as file:
                data = json.load(file)
            
            if message.author.name not in data:
                await message.channel.send(f"tu eh pobre")
            else:
                await message.channel.send(f"saldo: {data[message.author.name]} pila")

        elif message.content.startswith('$'):
            await message.channel.send('escreve comando direito o comunista desgraçado')
                    
    async def on_voice_state_update(self, member, before, after):
        try:
            membro = member.name
            fodidos = {
                'calicute_': ['jamal.mp3', 10],
                'senhor_jp': ['amigo-boi.mp3', 4],
                'palmadinha': ['olhaeleae.mp3', 6]
            }
            if (before.channel == None) and (membro in fodidos):
                
                # Connect to the voice channel
                channel = after.channel
                voice_channel = await channel.connect()

                # Play the audio file
                audio = FFmpegPCMAudio(fodidos[membro][0])
                voice_channel.play(audio)

                # Optionally, disconnect after a short duration
                await asyncio.sleep(fodidos[membro][1])  # Adjust time based on the length of the audio
                await voice_channel.disconnect()
        except Exception as e:
            print("ocorreu um erro ao colocar o audio do jamas:", e)
            await voice_channel.disconnect()
            

intents = discord.Intents.all()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)