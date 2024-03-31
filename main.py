from kivy.app import App
from kivy.lang import Builder

from email.mime.text import MIMEText
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager , Screen
import smtplib as smtp
from email.mime.text import MIMEText
from email.header import Header
import datetime

Builder.load_file("background.kv")
# using now() to get current time
current_time = datetime.datetime.now()

def sending_msg(message):


    login = 'musicdruin@gmail.com'
    password = 'jeyk zfpx xkaa ysnb'

    server = smtp.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(login, password)

    subject = 'Оповещение'
    text = f'Здравствуйте, ваш ребёнок  {current_time} отсутствовал в школе'

    mime = MIMEText(text, 'plain', 'utf-8')
    mime['Subject'] = Header(subject, 'utf-8')

    server.sendmail(login, message, mime.as_string())







Window.clearcolor = (.14,.14,.14,1)


class Hack(App):
    def build(self):


        box = BoxLayout(orientation = "vertical",  padding=[5,5,5, 500],spacing = 9 )
        box.add_widget(Label(text="gmail получателя"))
        inty = self.textinput = TextInput(border = (8,8,8,8))
        box.add_widget(inty)

        box.add_widget( Button( text = "оповещение" ,background_color = [.08,.9,.45,1] ,background_normal ='', on_press = self.btn_press))
        return box
    def btn_press(self,obj):
        inform = (self.textinput.text)
        sending_msg(inform)





if __name__ == "__main__":
    Hack().run()
