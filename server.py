import hashlib
import socket
import threading
from mysql.connector import pooling

db_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    pool_reset_session=True,
    host='sql3.freesqldatabase.com',
    user='sql3663427',
    password='2qAN3996zk',
    database='sql3663427'
)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))

server.listen()

def handle_connection(c):
    data_received = c.recv(1024).decode()
    username, password = data_received.split('|')
    password = hashlib.sha256(password.encode()).hexdigest()

    try:
        connection = db_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM userdata WHERE username = %s AND password = %s", (username, password))

        if cursor.fetchall():
            c.send("True".encode())
        else:
            c.send("False".encode())

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()