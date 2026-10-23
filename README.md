# Local Network Chat Client

A lightweight multi-threaded Python client script designed to connect to a local TCP chat server. It supports asynchronous message sending and receiving over sockets.

## 📌 Features

* **Multi-threaded Architecture**: Runs a background daemon thread (`receive_message`) to continuously listen for incoming messages without blocking user input.
* **Simple CLI Interface**: Clean command-line interface prompting for a username and interactive chat input.
* **Graceful Disconnection**: Supports typing `'exit'` to cleanly terminate the session and close open socket handles.
* **Error Handling**: Gracefully handles `ConnectionRefusedError` if the server is offline or unreachable.

## 🛠️ Prerequisites

* **Python 3.x** installed.
* No external third-party dependencies required (uses built-in `socket` and `threading` libraries).
* An active **TCP Chat Server** listening on `127.0.0.1:5000` (or configured host/port).

## 🚀 How to Run

1. **Start the Chat Server** first (ensure it is configured to accept incoming TCP connections on host `127.0.0.1` and port `5000`).

2. **Run the Client Script**:
   ```bash
   python client.py
   ```

3. **Enter Your Username** when prompted:
   ```text
   =======================================================
                   Local Network Chat
   =======================================================

   Your Name: Alice
   Connected! Type 'exit' to leave.
   You: Hello world!
   ```

4. **Exit the Chat**:
   Type `exit` in the console and press **Enter** to leave the room and close the connection.

## ⚙️ Configuration

To connect to a server hosted on a different machine on your local network, modify the following variables in the script:

```python
HOST = "192.168.x.x"  # Replace with target server IP address
PORT = 5000           # Match the target server port
```

## 📐 Code Overview

| Component | Description |
| --- | --- |
| `socket.AF_INET, socket.SOCK_STREAM` | Creates an IPv4 TCP socket connection. |
| `receive_message(client)` | Function running in a daemon thread to receive incoming messages up to 1024 bytes. |
| `client.send(...)` | Encodes user strings to UTF-8 bytes and transmits them to the server. |
| `finally: client.close()` | Ensures the socket connection closes cleanly upon exit or exception. |