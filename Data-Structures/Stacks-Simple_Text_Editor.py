# Enter your code here. Read input from STDIN. Print output to STDOUT
class SimpleTextEditor:
    def __init__(self):
        self.text = []
        self.ops = []
    def append(self, s, orig=True):
        for c in s: self.text.append(c)
        if orig: self.ops.append((2, len(s)))
        
    def delete(self, k, orig=True):
        tmp = ""
        k = min(k, len(self.text))
        while k > 0: 
            tmp = self.text.pop() + tmp
            k -= 1
        if orig: self.ops.append((1, tmp))
        
    def print_char(self, k):
        print '' if k >= len(self.text) else self.text[k]
        
    def undo(self):
        if len(self.ops) == 0: return
        op = self.ops.pop()
        if op[0] == 1: self.append(op[1], orig=False)
        else: self.delete(op[1], orig=False)
            
def main():
    N = int(raw_input())
    editor = SimpleTextEditor()
    for _ in xrange(N):
        op = raw_input().split()
        if op[0] == '1': editor.append(op[1])
        elif op[0] == '2': editor.delete(int(op[1]))
        elif op[0] == '3': editor.print_char(int(op[1])-1)
        else: editor.undo()

if __name__ == "__main__":
    main()
