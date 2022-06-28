import itchat
import logging
bot = itchat.Client(ws_url="wss://8080-artythedev-codespacesre-v1llgo5psyv.ws-eu47.gitpod.io/ws")

logging.basicConfig(level=logging.DEBUG)

@bot.listen
async def on_ready():
    print(bot.me.username)
    
bot.login("private-token")