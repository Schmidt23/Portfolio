import SocketServer


#Server
class ThreadedEchoRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.currentThread()
        response = '%s: %s' %(cur_thread.getName(), data)
        self.request.send(response)
        return

class ThreadedEchoServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass



if __name__ == "__main__":

    import socket
    import threading

    address = ('localhost', 0) #get address from kernel
    server = ThreadedEchoServer(address, ThreadedEchoRequestHandler)
    ip, port = server.server_address #get given port

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()
    print 'server loop running on thread:', t.getName()

    #Connect to server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))

    #Send the data
    message = "Testtestests"
    print "Sending: %s" % message
    len_sent= s.send(message)

    #receive response
    response = s.recv(1024)
    print 'Received: "%s"' % response

    #Clean up
    s.close()
    server.socket.close()