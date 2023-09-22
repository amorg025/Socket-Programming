# Simple Python Web Server

This is a basic Python web server implemented using sockets. It can serve static files over HTTP using the GET method.

## Getting Started

To run this web server, follow these steps:

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the server.py file.

3. Run the server using the following command:

```
python3 webserver.py
```
4. The server will start and print "Ready to serve..." in the terminal.

## Usage

1. Place the HTML and other static files you want to serve in the same directory as `webserver.py`.

2. Open a web browser and enter the following URL:
http://localhost:80/


Replace `localhost` with the IP address or hostname of the machine running the server if needed.

3. The server will respond with the requested files or a "404 Not Found" error if the file is not found.

## Features

- Supports serving static files (HTML, CSS, JavaScript, etc.) over HTTP.
- Handles GET requests only.
- Provides basic error handling for file not found (404).

## Customization

You can customize the following in the `server.py` file:

- `serverPort`: Change the port number on which the server listens (default is 80).
- Modify the code to handle other HTTP methods or add more advanced features as needed.
