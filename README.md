# CS494ChatRoomProj
This is a chat room software based on UDP protocol. 
# About this Project
## About the Internetwork Part
This Project is Hosting on AliClould Platform. the domain is malker.cn prot is 9999 (if u cant get the ipaddress, u need add dns21.hichina.com or dns22.hichina.com) 
## About Client Part
In order to prevent being suspected of cheating, I deleted all third-party software packages downloaded by npm (thank you Bart). Although the Javascript file can theoretically realize all the contents of the client, it has been abolished at present. What really works is the Python file in it. The client is only used to transmit and receive information. In order to protect the data, the client does not design any information storage function.
### Regarding the instructions used in the client test and the corresponding scoring items
```Python 3
commad_lib = [
    b'Server status', # Client can connect to a server
    b'Creat new room', # Client can create a room / Client can join a room
    b'Get Room Info', # Client can list members of a room
    b'Get Room List', # Client can list all rooms
    b'Get Room Chat History', 
    b'Send Message ~20~ This is a Test Message frome Client'# Client can send messages to a room
    b'Disconnect!' # Client can disconnect from a server
    b'Server plz shut down' # Server can disconnect from clients
    # Client can gracefully handle server crashes
    # Server can gracefully handle client crashes
]
```
## About Server Part
The server side implements all information storage, including server logs and room information. 
* The chat history of the room, 
* the joining information of the room. 
* Even set up the corresponding class for the room to store the password, but, in order to facilitate the test, the password of each room has become 123456 by default.
###  Corresponding functions implemented on the server side
* Server Process
* Server can help Client create a room
* Server can help Client list all rooms
* Server can help Client join a room
* Multiple clients can connect to a server
* Server can disconnect from clients
* Server can gracefully handle client crashes
* Cloud connected server
# Public Repo's Log
```
2021/03/05 15
make repo public
```