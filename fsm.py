from transitions.extensions import GraphMachine

from utils import send_text_message,send_button_message
from linebot.models import MessageTemplateAction

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"
    def on_enter_menu(self, event):
        title = 'Welcome'
        text = 'Japan travel checklist'
        btn = [
            MessageTemplateAction(
                label = 'visit japan web',
                text ='visit japan web'
            ),
            MessageTemplateAction(
                label = 'accommodation',
                text = 'accommodation'
            ),
            MessageTemplateAction(
                label = 'airline tickets',
                text ='airline tickets'
            ),
            MessageTemplateAction(
                label = 'attraction',
                text ='attraction'
            ),
        ]
        url = 'https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/1200px-Flag_of_Japan.svg.png'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_airline(self, event):
        text = event.message.text
        return text.lower() == "airline tickets"
    def on_enter_airline(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "及早查看各個航空機票時間和價錢\n早去晚回的班機比較昂貴喔\n連結:https://www.skyscanner.com.tw/")
        self.go_back()
    def is_going_to_vjw(self, event):
        text = event.message.text
        return text.lower() == "visit japan web"
    def on_enter_vjw(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "現在入境日本非常容易\n只需要填寫visit japan web即可\n連結:https://vjw-lp.digital.go.jp/zh-hant/")
        self.go_back()
    def is_going_to_hotel(self, event):
        text = event.message.text
        return text.lower() == "accommodation"
    def on_enter_hotel(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "及早訂房以免想要的住的地方已經客滿\n如果離地鐵或火車站近一點比較好喔\nAgoda連結:https://www.agoda.com/zh-tw/ \nBooking連結:https://www.booking.com/index.zh-tw.html")
        self.go_back()
    def is_going_to_attraction(self, event):
        text = event.message.text
        return text.lower() == "attraction"
    def on_enter_attraction(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "很多景點門票都可以在klook購買例如: 環球影城\n連結:https://www.klook.com/zh-TW/experiences/coureg-mcate/12-2-japan-attractions/?spm=Experience_Vertical.CountryCard&clickId=66e78ac683")
        self.go_back()
    '''
    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()
    '''
    '''
    def on_exit_menu(self):
        print("Leaving menu")
    
    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()
    def on_exit_state2(self):
        print("Leaving state2")
    '''
