# telegram_bot

## Setup

1. Search for BotFather on telegram app
2. Follow instructions
3. Click bot username to activate
4. Copy bot token



## API

[Doc](https://core.telegram.org/bots/api#available-methods)

- `https://api.telegram.org/bot{TOKEN}/{METHOD_NAME}`

- request above url using methods from doc
- add `setWebhook`once to connect my server(ex. ngrok) with telegram server



## ngrok

- setWebhook example

```python
import requests

# URL
METHOD_NAME = 'setWebhook'
TOKEN = '<token>'
URL = f'https://api.telegram.org/bot{TOKEN}/{METHOD_NAME}'

# receiving URL
ngrok_url = 'https://<url>.ngrok.io/telegram'

webHook_url = f'{URL}?url={ngrok_url}'
print(webHook_url)
```

