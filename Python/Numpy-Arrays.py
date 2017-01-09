import numpy
import sys
    
def main():
    arr = numpy.array(list(reversed(map(float, raw_input().split()))))
    print arr

if __name__ == "__main__":
    main()
