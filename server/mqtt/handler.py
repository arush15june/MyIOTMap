import paho.client as mqtt

HOST = 'localhost'
PORT = 1883

class MQTTConnector:
    
    def __init__(self, host, port):
        host = host
        port = port
        client = mqtt.Client()

    def connect():
        self.client.connect(self.host, self.port, 60)        

    def run(self):
        self.client.loop_forever()

class MQTTSubscriber:
    
    def __init__(self, *args, **kwargs): 
        super(MQTTSubscriber, self).__init__(*args, **kwargs)

class MQTTPublisher:
    
    def __init__(self, host)