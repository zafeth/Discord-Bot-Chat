import os
import asyncio
import discord

os.system('pip install -U discord==1.7.3')
os.system('pip install -U discord.py==1.7.3')

token = "xxxx" #TokenIdYour
replyMessage = 'Hallo bang'
channelId = 111111 #channeild
delay = 15

mainMessages = [
    'hadeh',
    'gw baru join ni bang',
    'gimana cara naik levelnya',
    'infonya dong bang cara dapet airdrop',
    'ajarin gw bang cara garapnya',
    'sombonk amat ini',
    'oke gw udh mulai paham',
    'gw paham cara ngerjainnya',
    'aduh cape',
    'gw mau menyerah aja deh'
]

class Main(discord.Client):
    async def on_ready(self):
        print('Logged in as %s.' % self.user)
        while True:
            channel = self.get_channel(channelId)
            for i, msg in enumerate(mainMessages):
                sent_message = await channel.send(msg)
                print(f'Sent message {i+1} in #{channel.name}.')
                await asyncio.sleep(delay)
                await sent_message.delete()  # Delete the sent message

    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel):
            if message.author.id != self.user.id:
                with open('blacklist.txt', 'r', encoding='UTF-8') as file:
                    if str(message.author.id) not in file.read():
                        sent_message = await message.reply(replyMessage)
                        print('Replied to %s.' % message.author.name)
                        await asyncio.sleep(delay)
                        await sent_message.delete()  # Delete the sent message
                        with open('blacklist.txt', 'a', encoding='UTF-8') as file:
                            file.write('%s\n' % message.author.id)

if __name__ == '__main__':
    Main().run(token, bot=False)
