import os
import discord
import time
import random
import praw

tocken = 'NzQ4MjAyNDUxNDc5NDI5MTkw.X0Z_1Q.rLPx4SJheg_M6ePYUzk9vnfP1xs'

class MyClient(discord.Client):
    
    async def on_ready(self):
        print('Logged on as %s' % self.user)

    async def on_message(self, message):
        
        reddit = praw.Reddit(client_id="Ym_oZmw_yo_5WA",
                     client_secret="DXsGGW49zxOyzYHuG--c0BHlaxE",
                     user_agent="edward.com")
        
        subs = reddit.subreddit('askreddit').top('hour')

        questions = []
        for sub in subs:
            questions.append(sub.title)
        
        send = questions[random.randint(0,len(questions)-1)]
        # msg = message.content
        # id = msg.split('&')[1].split('>')[0]
        # print(id)
        # mention = '<@%s>' % id
        # print(mention)
        # print('Message From %s: %s' % (message.author, message.content))
        user = discord.utils.get(message.channel.members, name = 'edwardwawrzynek')
        # print(user.mention)
        if message.content.startswith('!Edward.com') or message.content.startswith('!Ed'):
            # print(mention +' test')
            # print(user.mention+' test')
            await message.channel.send(user.mention+ ' '+ send)


client = MyClient()
client.run(tocken)