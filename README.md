# zaun.py 🐍

### Usage/ Rest
```py
from zaun import rest

client = rest.SyncREST()
client.set_token("TOKEN")

res = client.get('/users/@me')

print(res)
```

### Usage/ Client
```py
import zaun

client = zaun.Client()

@client.listen
async def on_message(message: zaun.Message) -> None:
    print(message.content)

client.login("TOKEN")
```



### Other libs for Zaun

- [zaun.js](https://github.com/itchatapp/zaun.js)
