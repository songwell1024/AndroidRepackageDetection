import requests
import eventlet
import time
def test():
    eventlet.monkey_patch()
    with eventlet.Timeout(2,False):
        time.sleep(3)
        return 'aaa'



if __name__ == '__main__':
    try:
        print(test())
    except:
        print("aaaaaaaaaaaaa")