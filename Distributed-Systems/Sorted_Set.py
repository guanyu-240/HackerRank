
# NOTE: Use this path to create the UDS Server socket
import socket
import struct
import functools
import threading

FMT = "!L"

data = {}

def add_score(s, key, score):
    if s not in data: data[s] = {key: score}
    else: data[s][key] = score
        
def get_value(s, key):
    if s not in data:
        return 0
    target_set = data[s]
    if key in target_set:  
        return target_set[key]
    return 0
    
def get_size(s):
    if s in data:
        return len(data[s])
    else:
        return 0
    
def get_range(sets, lower, upper):
    ret = []
    for s in sets:
        if s in data:
            tmp_set = data[s]
            for k in tmp_set:
                v = tmp_set[k]
                if lower<=v<=upper: ret.append([k,v])
    ret.sort()
    return functools.reduce(lambda x, y: x + y, ret)
    
def remove(s, key):
    if s not in data: return
    target = data[s]
    if key in target:
        del target[key]

def write_ret(conn, x):
    conn.send(struct.pack(FMT, len(x)))
    for e in x: 
        conn.send(struct.pack(FMT, e))
    
def get_cmd_from_socket(conn, cmd):
    n = struct.unpack(FMT, conn.recv(4))[0]
    for _ in range(n):
        cmd.append(struct.unpack(FMT, conn.recv(4))[0])


def process_connection(conn):
    while True:
        cmd = []
        get_cmd_from_socket(conn, cmd)
        cmd_type = cmd[0]
        ret = []
        if cmd_type == 1:
            add_score(*cmd[1:])
        elif cmd_type == 2:
            remove(*cmd[1:])
        elif cmd_type == 3:
            ret.append(get_size(*cmd[1:]))
        elif cmd_type == 4:
            ret.append(get_value(*cmd[1:]))
        elif cmd_type == 5:
            sets = cmd[1:-3]
            lower,upper = cmd[-2:]
            ret = get_range(sets, lower, upper)
        elif cmd_type == 6:
            conn.close() 
            break
        write_ret(conn, ret)

        
# NOTE: Use this path to create the UDS Server socket
SERVER_SOCKET_PATH = "./socket";
BACKLOG=10

def main():
    sock = socket.socket(socket.AF_UNIX)
    sock.bind(SERVER_SOCKET_PATH)
    sock.listen(BACKLOG)
    while True:
        conn = sock.accept()[0]
        t = threading.Thread(target=process_connection, args=(conn,))
        t.start()
    sock.close()
        
if __name__ == "__main__":
    main()
