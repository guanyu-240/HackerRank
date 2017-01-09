# NOTE: Use this path to create the UDS Server socket
import socket
import struct
import threading

SERVER_SOCKET_PATH = "./socket";
BACKLOG=8
FMT = "!I"

data = {}

def add_score(s, key, score):
    if s not in data: data[s] = {key: score}
    else: data[s][key] = score
    return None
        
def get_value(s, key):
    if s not in data: return 0
    else:
        ret = data[s].get(key)
        return ret if ret else 0
    
def get_range(args):
    sets = args[:-3]
    lower,upper = args[-2:]
    ret = []
    for s in sets:
        if s not in data: continue
        for k,v in data[s].items():
            if lower<=v<=upper: ret.append([k,v])
    ret.sort()
    ret = reduce(lambda x,y: x+y, ret)    
    return ret
    
def remove(s, key):
    target = data.get(s)
    if target and key in target:
        del target[key]
    return None

def write_ret(conn, x):
    if x is None:
        conn.send(struct.pack(FMT, 0))
    elif isinstance(x, int):
        conn.send(struct.pack(FMT, 1))
        conn.send(struct.pack(FMT, x))
    elif isinstance(x, list):
        conn.send(struct.pack(FMT, len(x)))
        for e in x: conn.send(struct.pack(FMT, e))
    
def get_cmd_from_socket(conn):
    n = struct.unpack(FMT, conn.recv(4))[0]
    ret = []
    for _ in xrange(n):
        ret.append(struct.unpack(FMT, conn.recv(4))[0])
    return ret

def process_connection(conn):
    while True:
        cmd = get_cmd_from_socket(conn)
        if cmd[0] == 1:
            write_ret(conn, add_score(*cmd[1:]))
        elif cmd[0] == 2:
            write_ret(conn, remove(*cmd[1:]))
        elif cmd[0] == 3:
            write_ret(conn, (0 if cmd[1] not in data else len(data[cmd[1]])))
        elif cmd[0] == 4:
            write_ret(conn, get_value(*cmd[1:]))
        elif cmd[0] == 5:
            write_ret(conn, get_range(cmd[1:]))
        elif cmd[0] == 6:
            conn.close() 
            break

def main():
    sock = socket.socket(socket.AF_UNIX)
    sock.bind(SERVER_SOCKET_PATH)
    sock.listen(BACKLOG)
    while True:
        conn,addr = sock.accept()
        t = threading.Thread(target=process_connection, args=(conn,))
        t.start()
    sock.close()
        
if __name__ == "__main__":
    main()
