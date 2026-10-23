import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def receive_message(client):
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print(f"\nFriend: {message}")

        except OSError:
            break


client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

try:
    client.connect((HOST, PORT))

    print("\n" + "=" * 55)
    print("                Local Network Chat")
    print("=" * 55)

    username = input("\nYour Name: ").strip()

    client.send(username.encode())

    threading.Thread(
        target=receive_message,
        args=(client,),
        daemon=True
    ).start()

    print("Connected! Type 'exit' to leave.")

    while True:
        message = input("You: ")

        if message.lower() == "exit":
            break

        client.send(message.encode())

except ConnectionRefusedError:
    print("\nServer is not running")

finally:
    client.close()
    print("Chat closed")
