import requests
import eventlet
import time
def test():
    eventlet.monkey_patch()
    with eventlet.Timeout(2,False):
        time.sleep(3)
        return 'aaa'



if __name__ == '__main__':
    listTest = []
    listTest.append(1)
    listTest.append(3)
    listTest.append(2)
    for i in listTest:
        print(i)
    listTest.remove(2)
    for i in listTest:
        print(i)