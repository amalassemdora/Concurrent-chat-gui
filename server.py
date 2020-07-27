from tkinter import *
from socket import * 

client = None

name = "Server"

def connectToChat():
    addMsgTolayout("Start Listening for client")
    Thread(target = handleClient ).start()
    
    
def handleClient():
    global client
    soc = socket(AF_INET , SOCK_STREAM)
    soc.bind((ip.get() , int(port.get())))
    soc.listen(5)    
    while True:
        con , ad = soc.accept()
        addMsgTolayout("Client :" + str(ad[0]) )
        client = con    
        rec()
    
def send():
    msg=msgToSend.get()
    # format msg to be sent
    messageToSend = "{}:{}".format(name,msg)
    messageToSend = messageToSend.encode("utf-8")
    client.send(messageToSend)
    # add client msg to text
    addMsgTolayout("me:{}".format(msg))
    # empty fields
    msgToSend.delete(0,END)
    
    

#window
wind = Tk()
wind.title("Amal Chat Room") # title

ip = Entry(wind )
ip.pack(pady= 3 )
ip.insert( 0 , "127.0.0.1" ) # add default ip (index , value)


port = Entry(wind)
port.pack( pady= 2)
port.insert(0 , "6002") # add default port 

username = Entry(wind)
username.pack( pady= 3)


btnConnect=Button(wind,text="Start Chat",command=connectToChat)
btnConnect.pack()


text = Text(wind ,height = 10 )
text.pack(fill=X )

msgToSend = Entry(wind)
msgToSend.pack()

btnSend=Button(wind,text="Send",command=send)
btnSend.pack()


from threading import Thread

def addMsgTolayout(msg):
    text.insert(END , '\n')
    text.insert(END , msg)
    
          

def rec():
    while True:
      msg = client.recv(1024).decode("utf-8")
      addMsgTolayout(msg)
      

#to run the window
wind.mainloop()



    

