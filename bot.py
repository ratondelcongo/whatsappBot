from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import selenium
from time import sleep
import myWeather
import myExchange


class WhatsappBot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=chrome-data")
        self.chrome = webdriver.Chrome(options=chrome_options)
        self.chrome.get("http://web.whatsapp.com")
        self.last_message = "#main > div._1_q7u > div > div > div > div.FTBzM > div > div > div > div.copyable-text > div > span"
        self.message_input_selector = "#main > footer > div._2i7Ej.copyable-area > div._13mgZ > div > div._3u328.copyable-text.selectable-text"

    def send_message(self, message):
        message_field = self.chrome.find_element_by_css_selector(
            self.message_input_selector)
        message_field.clear()
        message_field.click()

        message_field.send_keys(message)
        message_field.send_keys(u'\ue007')

    def get_last_message(self):
        msgs = self.chrome.find_elements_by_css_selector(
            self.last_message)
        return msgs[-2].text


def main():
    bot = WhatsappBot()
    sleep(5)
    while True:
        try:
            msg = bot.get_last_message()
            msgs = msg.split(' ')
            msg = msgs[0]
            msg2 = msgs[-1]
            
            if msg == '!help' or msg == '!ayuda':
                message = '!tiempo > Temp/Hume'
                bot.send_message(message)
                message = '!dolar # > dolar a soles'
                bot.send_message(message)
                message = '!peso # > peso a soles'
                bot.send_message(message)

            if msg == '!tiempo' or msg == '!clima':
                message = myWeather.get_temp()
                bot.send_message(message)
                message = myWeather.get_hum()
                bot.send_message(message)

            if msg == '!dolar' and len(msgs) == 2:
                message = myExchange.get_exchange('USD',float(msg2))
                bot.send_message(message)

            if msg == '!peso' and len(msgs) == 2:
                message = myExchange.get_exchange('ARS',float(msg2))
                bot.send_message(message)

        except IndexError:
            pass
        except selenium.common.exceptions.StaleElementReferenceException:
            pass


if __name__ == "__main__":
    main()
