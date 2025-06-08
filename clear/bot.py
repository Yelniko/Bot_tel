import time
import telebot
import requests
import json

bot = telebot.TeleBot('')

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8,uk;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://hivescan.info',
    'Pragma': 'no-cache',
    'Referer': 'https://hivescan.info/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'page-size': '100',
    'data-size-limit': '100000',
}


@bot.message_handler(commands=['start'])
def main(message):

    trx_id_save = ""

    while True:
        response = requests.get('https://hafbe.openhive.network/hafah-api/accounts/hivemexc/operations', params=params, headers=headers)

        with open("../../bot_pars/index.json", 'w') as file:
            file.write(response.text)

        with open("../../bot_pars/index.json") as f:
            templates = json.load(f)

        trx_id = str(templates['operations_result'][0]['trx_id'])

        if trx_id_save != trx_id:
            trx_id_save = trx_id

            char = (f'<b>Block:</b> { templates["operations_result"][0]["block"]}\n'
                    f'<b>Transaction:</b> { templates["operations_result"][0]["trx_id"]}\n'
                    f'<b>Time</b> { templates["operations_result"][0]["timestamp"].split("T")[0]}'
                    f' {templates["operations_result"][0]["timestamp"].split("T")[1]}\n'
                    f'<b>Operation:</b> { templates["operations_result"][0]["op"]["type"].split("_")[0]}\n'
                    f'<b>Content:</b> @{ templates["operations_result"][0]["op"]["value"]["from"]} '
                    f'{templates["operations_result"][0]["op"]["type"].split("_")[0]} '
                    f'{templates["operations_result"][0]["op"]["value"]["amount"]["amount"][:-3]}.'
                    f'{templates["operations_result"][0]["op"]["value"]["amount"]["amount"][-3:]} HIVE to '
                    f'@{templates["operations_result"][0]["op"]["value"]["to"]}\n')

            bot.send_message(message.chat.id, char, parse_mode='html')

            time.sleep(60)




if __name__ == "__main__":
    bot.infinity_polling()