import json
from telethon import TelegramClient
from os.path import isfile

if (isfile('config.json')):
    config = json.load(open('config.json'))
else:
    config = {
        'api_id': input('api_id: '),
        'api_hash': input('api_hash: '),
        'channel_username': input('channel_username: ')
    }
    json.dump(config, open('config.json', 'w'))

client = TelegramClient('annon', config['api_id'], config['api_hash'])

async def main():
    async for message in client.iter_messages(config['channel_username']):
        print(message.id, message.text)
        if message.media is not None:
            print('File Name :' + str(message.file.name))
            path = await client.download_media(message=message, file="downloads")
            print('File saved to', path)  # printed after download is done

with client:
    client.loop.run_until_complete(main())
