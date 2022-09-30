#error and exception are the same
#everithing starts from basic exception
#to catch the expection we can use the Try/Except finally(optional) contruct
import time


def causeError():
    try:
        return 1/1
    except Exception:
        print('There was some sort of errow')
    finally:#this is useful for debugging reason of the block. It will be execute no matter what.
        print('this will always execute')

#causeError()


def causeError1():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1/0
    except Exception:
        print('There was some sort of errow')
    finally:#this is useful for debugging reason of the block. It will be execute no matter what.
        print(f'function took {time.time()-start} seconds to execute')

##causeError1()

#caching eception by Type

def causeError2():
    try:
        return 1 + 'f'
    except TypeError:
        print('There was type error')
    except ZeroDivisionError:
        print('There was zero division error')

#causeError2()

#using a decorator
def handleException(func):
    def wrapper():
        try:
            func()
        except TypeError:
            print('There was type error')
        except ZeroDivisionError:
            print('There was zero division error')
        except Exception:
            print('There was some sort of error')
    return wrapper

@handleException
def causeError3():
    return 1/0

#causeError3()

#using decorator with argument to manage functions with parameters and raise statement
 
def handleException1(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print('There was type error')
        except ZeroDivisionError:
            print('There was zero division error')
        except Exception:
            print('There was some sort of error')
    return wrapper

@handleException1
def raiseError(n):
    if n == 0:
        raise Exception()#else statement is not needed
    print(n)

raiseError(2)