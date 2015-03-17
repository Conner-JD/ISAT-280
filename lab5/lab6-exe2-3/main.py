from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
import mysql.connector
from mysql.connector import errorcode
from kivy.uix.popup import Popup
from kivy.uix.label import Label

#ip='192.168.0.1'
ip='134.126.23.200'
dbname='my280'

class LoginScreen(Screen):
    def __init__(self, *args, **kwargs):       
       super(LoginScreen, self).__init__(*args, **kwargs)

    def login_auth(self):

        # gets the data from the text inputs on the login page
        uname = self.ids['uname_input']
        pword = self.ids['pass_input']

        # make sure that the values are not null
        if len(uname.text) > 0:
            if len(pword.text) > 0:
                query = self.manager.retrieve("SELECT * FROM userme WHERE username = \"%s\" AND password = \"%s\"" % (uname.text, pword.text))
                print query, self.manager.screen_names[2]
               
                if query == []:
                    popup = Popup(title='Invalid Credentials', content=Label(text='Username or Password is Incorrect'), size_hint=(None, None), size=(400, 100))
                    popup.open()
                elif query == None:
                    popup = Popup(title='Connection', content=Label(text='Could not connect to the database'), size_hint=(None, None), size=(400, 100))
                    popup.open()
                else:
                    uid, firstname, lastname, username, password= query[0]
                    loggedinuser = username
                    self.manager.current=self.manager.screen_names[2]
                    self.manager.screens[2].ids['uname_label'].text = "Welcome back %s" % (firstname)+"\nWhich sensor data are you after?"

            else:
                popup = Popup(title='Invalid Credentials', content=Label(text='Please Enter a Password'), size_hint=(None, None), size=(400, 100))
                popup.open()
        else:
            popup = Popup(title='Invalid Credentials', content=Label(text='Please Enter a Username'), size_hint=(None, None), size=(400, 100))
            popup.open()

class NewUserScreen(Screen):
    def __init__(self, *args, **kwargs):
       super(NewUserScreen, self).__init__(*args, **kwargs)

    def GetStarted(self):
        first = self.ids['first_input'].text
        last = self.ids['last_input'].text
        uname = self.ids['uname_input'].text
        pword= self.ids['pass_input'].text

        if (((len(first) > 0 and len(last)> 0) and (len(uname) > 0)) and (len(pword) > 0)):
            results = self.manager.create_account("INSERT INTO userme (firstname, lastname, username, password) VALUES ('%s','%s','%s','%s')" % (first,last,uname,pword))

            if results == 1:
                popup = Popup(title='Congratulations', content=Label(text='Thank you, please sign in'), size_hint=(None, None), size=(400, 100))
                self.manager.current=self.manager.screen_names[0]
                self.ids['first_input'].text=''
                self.ids['last_input'].text=''
                self.ids['uname_input'].text=''
                self.ids['pass_input'].text=''
                popup.open()
            elif results == 0:
                popup = Popup(title='Sorry :(', content=Label(text='Your username is already in use'), size_hint=(None, None), size=(400, 100))
                self.ids['uname_input'].text = ""
                popup.open()
            elif results == 2:
                popup = Popup(title='Sorry :(', content=Label(text='Didnt connect'), size_hint=(None, None), size=(400, 100))
                popup.open()
        else:
            popup = Popup(title='Sorry :(', content=Label(text='missing input'), size_hint=(None, None),size=(400,100))
            popup.open()

class WhatScreen(Screen):
    def __init__(self, *args, **kwargs):
       super(WhatScreen, self).__init__(*args, **kwargs)

class AccountMgr(ScreenManager):
    def __init__(self, *args, **kwargs):       
       super(AccountMgr, self).__init__(*args, **kwargs)

    def create_account (self, sql):
        try:
            cnx = mysql.connector.connect(user='root', password='checkout', host=ip, database=dbname)
            cur = cnx.cursor()
            cur.execute(sql)

            cnx.commit()

            cur.close()
            cnx.close()
            return(1)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return(2)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists")
                return(2)
            else:
                print(err)

    def retrieve (self, sql):
        try:

            cnx = mysql.connector.connect(user='root', password='checkout', host=ip, database=dbname)
            # set the cursor to extract the data
            cur = cnx.cursor()
            cur.execute(sql)

            return cur.fetchall()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return(0)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists")
                return(0)
            else:
                print(err)
        else:
            cnx.close()
            return(0)
          
class AccountMgrApp(App):
    def __init__(self, *args, **kwargs):       
       super(AccountMgrApp, self).__init__(*args, **kwargs)

    def build(self):
        return AccountMgr()

if __name__=='__main__':
    AccountMgrApp().run()
