# zaun.py 🐍

### Usage/ Rest
```py
from itchat import rest

client = rest.SyncREST()
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



### Other libs for itchat

- [itchat.js](https://github.com/itchatapp/itchat.js)
