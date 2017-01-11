#!/bin/python

import sys

def matching_bracket(b):
    if b == '}': return '{'
    elif b == ')': return '('
    else: return '['

def is_balanced(s):
    st = []
    left = "([{"
    for b in s:
        if b in left: 
            st.append(b)
        elif len(st) == 0 or st[-1] != matching_bracket(b):
            return "NO"
        else:
            st.pop()
    return 'YES' if len(st) == 0 else 'NO'

t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    print is_balanced(s)
