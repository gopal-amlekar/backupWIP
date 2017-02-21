
srv=net.createConnection(net.TCP, 0)
srv:on("receive", function(sck, c)
    print("message recd: ", c )
    end)

srv:connect(80, "pubsub.pubnub.com")

srv:on("connection", function(sck,c)
    print (c)
    sck:send("GET /publish/pub-c-c504d6fa-d3fe-48ad-b716-24f94c33d987/sub-c-fbde73de-6512-11e6-ac7d-02ee2ddab7fe/0/Channel_hw/0/%22LUA on PI%22 HTTP/1.1\r\nHost: pubnub\r\nConnection: keep-alive\r\nAccept: */*\r\n\r\n")
    sck:send("GET /stream/sub-c-fbde73de-6512-11e6-ac7d-02ee2ddab7fe/Channel_hw/0/1000 HTTP/1.1\r\nHost: pubnub\r\nConnection: keep-alive\r\nAccept: */*\r\n\r\n")
    end)
    
a = 1000
repeat 
   print ("value of a: ", a)
   a = a-1
until (a)