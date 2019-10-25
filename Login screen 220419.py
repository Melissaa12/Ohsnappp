from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from libdw import pyrebase
Window.clearcolor=(1,1,1,1)

class MyLabel(Label):

    def init(self, kwargs):
        Label.__init__(self, **kwargs)
        self.bind(size=self.setter('text_size'))
        self.padding = (20, 20)
        self.font_size = 45
         
        self.halign='left'
        self.valign='middle'

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)

        layout = FloatLayout(size=(10,10))
        l1 = MyLabel(text="Username",color=[255,255,255,1],size_hint=(.5,.5),pos_hint={"center_x":.2,"center_y":.4})
        layout.add_widget(l1)


        self.username=TextInput(text='',size_hint=(.5,.05),pos_hint={"center_x":.55,"center_y":.4})
        layout.add_widget(self.username)

        l2 = MyLabel(text="Password",color=[255,255,255,1],size_hint=(.5,.5),pos_hint={"center_x":.2,"center_y":.35})
        layout.add_widget(l2)

        self.password=TextInput(text='',size_hint=(.5,.05),pos_hint={"center_x":.55,"center_y":.35})
        layout.add_widget(self.password)

        btn = Button(text="Login", on_press=self.login, size_hint=(.15,.05),pos_hint={"center_x":.55,"center_y":.25})
        layout.add_widget(btn)

        self.l3 = Image(source='ohsnapicon.jpg',size_hint=(.5,.5),pos_hint={"center_x":.6,"center_y":.7})
        layout.add_widget(self.l3)

        self.add_widget(layout)

        
    def login(self, instance):
        user = self.username.text
        passw = self.password.text
        if user=='oka' and passw=='simon':
            self.manager.transition.direction = 'left'
            # modify the current screen to a different "name"
            self.manager.current = 'control'
        else:
            self.l3=MyLabel(text="ACCESS DENIED! TRY AGAIN!")
            user=''
            passw=''
            self.manager.current = 'login'

class ControlScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        layout = FloatLayout(size=(10,10))
        
        _90 = Button(text=" 90° ", font_size=24 , size_hint=(.2,.2),pos_hint={"center_x":.35,"center_y":.90}, on_press=self.nine)
        layout.add_widget(_90)
        
        self.pic90 = Image(source='90.jpg',size_hint=(.2,.2),pos_hint={"center_x":0.1,"center_y":0.90})
        layout.add_widget(self.pic90)
        
        _80 = Button(text=" 80° ", font_size=24 , size_hint=(.2,.2),pos_hint={"center_x":.35,"center_y":.70}, on_press=self.eight)
        layout.add_widget(_80)
        
        self.pic80 = Image(source='80.jpg',size_hint=(.2,.2),pos_hint={"center_x":0.1,"center_y":0.70})
        layout.add_widget(self.pic80)
        
        _70 = Button(text=" 70° ", font_size=24 , size_hint=(.2,.2),pos_hint={"center_x":.35,"center_y":.50}, on_press=self.seven)
        layout.add_widget(_70)
        
        self.pic70 = Image(source='70.jpg',size_hint=(.2,.2),pos_hint={"center_x":0.1,"center_y":0.50})
        layout.add_widget(self.pic70)

        _60 = Button(text=" 60° ", font_size=24 , size_hint=(.2,.2),pos_hint={"center_x":.35,"center_y":.3}, on_press=self.six)
        layout.add_widget(_60)
        
        self.pic60 = Image(source='60.jpg',size_hint=(.2,.2),pos_hint={"center_x":0.1,"center_y":0.3})
        layout.add_widget(self.pic60)
        
        _50 = Button(text=" 50° ", font_size=24 , size_hint=(.2,.2),pos_hint={"center_x":.35,"center_y":.1}, on_press=self.five)
        layout.add_widget(_50)
        
        self.pic50 = Image(source='50.jpg',size_hint=(.2,.2),pos_hint={"center_x":0.1,"center_y":0.1})
        layout.add_widget(self.pic50)
        
        _40 = Button(text=" 40° ", font_size=24 , size_hint=(.2,.2),pos_hint={"center_x":.9,"center_y":.9}, on_press=self.four)
        layout.add_widget(_40)
        
        self.pic40 = Image(source='40.jpg',size_hint=(.2,.2),pos_hint={"center_x":0.65,"center_y":0.9})
        layout.add_widget(self.pic40)
        
        _30 = Button(text=" 30° ",font_size=24 , size_hint=(.2,.2),pos_hint={"center_x":.9,"center_y":.7}, on_press=self.three)
        layout.add_widget(_30)
        
        self.pic30 = Image(source='30.jpg',size_hint=(.2,.2),pos_hint={"center_x":0.65,"center_y":0.7})
        layout.add_widget(self.pic30)
        
        _20 = Button(text=" 20° ", font_size=24 , size_hint=(.2,.2),pos_hint={"center_x":.9,"center_y":.5}, on_press=self.two)
        layout.add_widget(_20)
        
        self.pic20 = Image(source='20.jpg',size_hint=(.2,.2),pos_hint={"center_x":0.65,"center_y":0.5})
        layout.add_widget(self.pic20)
        
        _10= Button(text=" 10° ", font_size=24 , size_hint=(.2,.2),pos_hint={"center_x":.9,"center_y":.3}, on_press=self.one)
        layout.add_widget(_10)
        
        self.pic10 = Image(source='10.jpg',size_hint=(.2,.2),pos_hint={"center_x":0.65,"center_y":0.3})
        layout.add_widget(self.pic10)
        
        _0 =Button(text=" 0° ", font_size=24 , size_hint=(.2,.2),pos_hint={"center_x":.9,"center_y":.1}, on_press=self.zero)
        layout.add_widget(_0)
        
        self.pic0 = Image(source='0.jpg',size_hint=(.2,.2),pos_hint={"center_x":0.65,"center_y":0.1})
        layout.add_widget(self.pic0)
        
        
        self.add_widget(layout)
        
    def nine(self,value):
        url = "https://ohsnappp-837d7.firebaseio.com"
        apikey = "AIzaSyAOKIBnAUiI9VSt3x1FoocWp0udv34xdqA"

        config = {
    "apiKey": apikey,
    "databaseURL": url,
}

        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        db.child('Joel').set(90)
        
    def eight(self,value):
        url = "https://ohsnappp-837d7.firebaseio.com"
        apikey = "AIzaSyAOKIBnAUiI9VSt3x1FoocWp0udv34xdqA"

        config = {
    "apiKey": apikey,
    "databaseURL": url,
}

        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        db.child('Joel').set(80)

    def seven(self,value):
        url = "https://ohsnappp-837d7.firebaseio.com"
        apikey = "AIzaSyAOKIBnAUiI9VSt3x1FoocWp0udv34xdqA"

        config = {
    "apiKey": apikey,
    "databaseURL": url,
}

        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        db.child('Joel').set(70)
        
    def six(self,value):
        url = "https://ohsnappp-837d7.firebaseio.com"
        apikey = "AIzaSyAOKIBnAUiI9VSt3x1FoocWp0udv34xdqA"

        config = {
    "apiKey": apikey,
    "databaseURL": url,
}

        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        db.child('Joel').set(60)
        
    def five(self,value):
        url = "https://ohsnappp-837d7.firebaseio.com"
        apikey = "AIzaSyAOKIBnAUiI9VSt3x1FoocWp0udv34xdqA"

        config = {
    "apiKey": apikey,
    "databaseURL": url,
}

        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        db.child('Joel').set(50)
        
    def four(self,value):
        url = "https://ohsnappp-837d7.firebaseio.com"
        apikey = "AIzaSyAOKIBnAUiI9VSt3x1FoocWp0udv34xdqA"

        config = {
    "apiKey": apikey,
    "databaseURL": url,
}

        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        db.child('Joel').set(40)
        
    def three(self,value):
        url = "https://ohsnappp-837d7.firebaseio.com"
        apikey = "AIzaSyAOKIBnAUiI9VSt3x1FoocWp0udv34xdqA"

        config = {
    "apiKey": apikey,
    "databaseURL": url,
}

        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        db.child('Joel').set(30)

    def two(self,value):
        url = "https://ohsnappp-837d7.firebaseio.com"
        apikey = "AIzaSyAOKIBnAUiI9VSt3x1FoocWp0udv34xdqA"

        config = {
    "apiKey": apikey,
    "databaseURL": url,
}

        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        db.child('Joel').set(20)

    def one(self,value):
        url = "https://ohsnappp-837d7.firebaseio.com"
        apikey = "AIzaSyAOKIBnAUiI9VSt3x1FoocWp0udv34xdqA"

        config = {
    "apiKey": apikey,
    "databaseURL": url,
}

        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        db.child('Joel').set(10)

    def zero(self,value):
        url = "https://ohsnappp-837d7.firebaseio.com"
        apikey = "AIzaSyAOKIBnAUiI9VSt3x1FoocWp0udv34xdqA"

        config = {
    "apiKey": apikey,
    "databaseURL": url,
}

        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        db.child('Joel').set(0)

class SwitchScreenApp(App):
    def build(self):
            sm = ScreenManager()
            lg = LoginScreen(name='login')
            ct = ControlScreen(name='control')
            sm.add_widget(lg)
            sm.add_widget(ct)
            sm.current = 'login'
            return sm
        
if __name__ == '__main__':
    SwitchScreenApp().run()
