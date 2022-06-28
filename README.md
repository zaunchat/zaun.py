# ItChat.py 🐍

### Usage/ Rest
```py
from itchat.rest import SyncREST

client = SyncREST()
client.set_token("TOKEN")

res = client.get('/users/@me')

print(res)
```

### Usage/ Client
```py
import itchat

client = itchat.Client()

@client.listen
async def on_message(message: itchat.Message) -> None:
    print(message.content)

client.login("TOKEN")
```


#### ItChat.js: [Repo](htts://github.com/itchatapp/itchat.js)