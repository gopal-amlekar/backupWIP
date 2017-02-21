import socket
import time

s = socket.socket()

def pubresp(message):
    print ("Published...")
    print (message)
payload = '%7B%22NAME%22%3A%22MUSIC_PLAYER%22%2C%20%22LOC%22%3A%22Child%20room%22%7D'    
url = 'http://pubsub.pubnub.com/publish/pub-c-c504d6fa-d3fe-48ad-b716-24f94c33d987/sub-c-fbde73de-6512-11e6-ac7d-02ee2ddab7fe/0/Channel_my/pubresp/' + payload

try:
    _, _, host, path = url.split('/', 3)
    print (host)
    print (path)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s.connect(addr)
    s.settimeout(60)
    s.send(bytes('GET /%s HTTP/1.1\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    n = 5
    while n > 0:
        data = s.recv(2)
        #print ("Getting data...")
        #print(str(data, 'utf8'), end='')
        if data:
            print(str(data, 'utf8'), end='')
        else:
            print ("Finished receiving data")
            break
        #print ("got data... LOOP %d", n)
        n = n-1
    #s.close()
    print ("Done with Publishing")
except:
    print ("Publish Probably timed out")
    pass


url = 'https://pubsub.pubnub.com/v2/subscribe/sub-c-fbde73de-6512-11e6-ac7d-02ee2ddab7fe/Channel_my/0?uuid=MPLAYER_CHILD_ROOM&tt=0&tr=0&state=READY'
try:
    _, _, host, path = url.split('/', 3)
    print (host)
    print (path)
    #addr = socket.getaddrinfo(host, 80)[0][-1]
    #s.connect(addr)
    #s.settimeout(30)
    s.send(bytes('GET /%s HTTP/1.1\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    n = 5
    while n > 0:
        data = s.recv(100)
        #print ("Getting data...")
        #print(str(data, 'utf8'), end='')
        if data:
            print(str(data, 'utf8'), end='')
        else:
            print ("Finished receiving data")
            break
        #print ("got data... LOOP %d", n)
        n = n-1
    #s.close()
    print ("Done with setting UUID")
except Exception as e:
    print (str(e))
    pass

        
url = 'http://pubsub.pubnub.com/time/0'
try:
    _, _, host, path = url.split('/', 3)
    print (host)
    print (path)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s.connect(addr)
    s.settimeout(60)
    s.send(bytes('GET /%s HTTP/1.1\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    n = 5
    while n > 0:
        data = s.recv(2)
        #print ("Getting data...")
        #print(str(data, 'utf8'), end='')
        if data:
            print(str(data, 'utf8'), end='')
        else:
            print ("Finished receiving data")
            break
        #print ("got data... LOOP %d", n)
        n = n-1
    #s.close()
    print ("Done with setting an forever open socket")
except:
    print ("Probably timed out")
    pass

s.settimeout(None)
url = 'http://pubsub.pubnub.com/stream/sub-c-fbde73de-6512-11e6-ac7d-02ee2ddab7fe/Channel_my/0/1000'

url2 = 'https://pubsub.pubnub.com/v2/presence/sub-key/sub-c-fbde73de-6512-11e6-ac7d-02ee2ddab7fe/channel/Channel_my/heartbeat?callback=0&state=%7B%22READY%22%7D'
t = time.time()
while 1:
    try:
        if time.time() > t+10:
            print ("Sending heartbeat")
            _, _, host, path = url2.split('/', 3)
            print (host)
            print (path)
            s.send(bytes('GET /%s HTTP/1.1\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
            t = time.time()
        else:    
            _, _, host, path = url.split('/', 3)
            print (host)
            print (path)
            s.send(bytes('GET /%s HTTP/1.1\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
            n = 500
            while n > 0:
                data = s.recv(100)
                #print ("Getting data...")
                #print(str(data, 'utf8'), end='')
                if data:
                    print(str(data, 'utf8'), end='')
                else:
                    print ("Finished receiving data")
                    break
                #print ("got data... LOOP %d", n)
                #n = n-1
                #s.close()
            print ("Done with streaming")
    except Exception as e:
        print (str(e))
        print ("Exiting...")
        s.close()
