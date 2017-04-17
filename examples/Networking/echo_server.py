import socket

srv = socket.socket()
srv.bind(('localhost', 8000))
srv.listen(1)

conn, addr = srv.accept()
srv.close()

while True:
    buf = conn.recv(1000)
    print 'Received', buf.rstrip()
    if not buf:
        break
    conn.send(buf)
