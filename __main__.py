from src.plumberhub.Client import PlumberHubClient
import time

def p(sample):
    print(sample.at)

def onclose():
    print(88)

def onready():
    print('hello')

    device = client.get_device()
    gain = client.get_gain()
    sampling_rate = client.get_sampling_rate()
    
    print(device)
    print(gain)
    print(sampling_rate)
        
    time.sleep(10)
    client.start()

    master = client.is_master()
    print(master)
    

client = PlumberHubClient(
    hostname = '127.0.0.1',
    port = 8080,
    client_id = '314dee1f82e82106c8ab4d51ee933c9a4c09209dfebc35b2f2f5fd55be73302e',
    onsample = p,
    onerror = p,
    onclose = onclose,
    onready = onready
)

time.sleep(2)
# client.set_gain(24)
newgain = client.get_gain()

print('\nnew gain:' + str(newgain) + '\n')

client.stop()
client.close()