class Email:
    def send(self,msg):
        print()
class Gmail(Email):
    def send(self,msg):
        print("Sending '{}' from Gmail",format(msg))
class Yahoo(Email):
    def send(self,msg):
        print("Sending '{}' from Yahoo",format(msg))
client1=Gmail()
client1.send("Hello!")
client2=Yahoo()
client2.send("Hi")
