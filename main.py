import os

os.system('pip install -U discord==1.7.3')
os.system('pip install -U discord.py==1.7.3')

import discord, asyncio

token = "" #tokenid
replyMessage = 'Hello seilors ahoy'
channelId = 00000000
delay = 61

mainMessages = [
'Hello seilors',
'Seilors ahhoy',
'Ah dont spam keep calm sir',
'Dont forget keep calm',
'Experience the power of community with SeiNetwork!',
'SeiNetworkunlocking your full potential!',
'At SeiNetwork, we never stop striving for excellence',
'Join SeiNetwork and discover a world of possibilities',
'Sei can killer ethereum',
'At SeiNetwork, we believe in pushing boundaries and breaking limits',
'Join us and be a part of the SeiNetwork family',
'Hello everyone seilors ahoy',
'SeiNetwork where innovation and creativity thrive!',
'Unlock your potential with the support of SeiNetwork',
'At SeiNetwork, we believe in the power of collaboration and teamwork',
'Join SeiNetwork and let us help you achieve your goals',
'SeiNetwork where we celebrate diversity and inclusivity',
'Good project SeiNetwork',
'Keep active sir and get role',
'dont spaming oke ?'
]


class Main(discord.Client):
    async def on_ready(self):
        print('Logged in as %s.' % self.user)
        while True:
            channel = self.get_channel(channelId)
            for i, msg in enumerate(mainMessages):
                await channel.send(msg)
                print(f'Sent message {i+1} in #{channel.name}.')
                await asyncio.sleep(delay)


    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel):
            if message.author.id != self.user.id:
                with open('blacklist.txt', 'r', encoding = 'UTF-8') as file:
                    if str(message.author.id) not in file.read():
                        await message.reply(replyMessage)
                        print('Replied to %s.' % message.author.name)
                        with open('blacklist.txt', 'a', encoding = 'UTF-8') as file:
                            file.write('%s\n' % message.author.id)

if __name__ == '__main__':
    Main().run(token, bot = False)