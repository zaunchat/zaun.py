# ItChat.py 🐍
### Usage
```py
import itchat

client = itchat.Client()

@client.listen
async def on_message(message: itchat.Message) -> None:
    print(message.content)

client.login("TOKEN")
```


#### ItChat.js: [Repo](https://github.com/itchatapp/itchat.js)