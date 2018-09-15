import os
import sys

def main():
    print('this is main')
    print('args:', ' '.join(sys.argv[1:]))

if __name__ == '__main__':
    sys.exit(main())
