from udp_test import make_udp_client

if __name__ == '__main__':
    make_udp_client()


# binding server on localhost:10000
# waiting for receiveing message...
# received 32 bytes from ('127.0.0.1', 57065)
# b'the message to be sent to server'
# send 32 bytes to ('127.0.0.1', 57065)
# waiting for receiveing message...

# sending message to server
# waiting to receive...
# received b'the message to be sent to server'
