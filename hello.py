import socket
def justEnter(hostname:str):
   f = socket.gethostbyname(hostname)
   return f
print(justEnter("movie.af"))

      
     