
import threading
import time



def longsquare(number, results):
    time.sleep(1)
    #return number*number
    results[number]= number**2

#[print(longsquare(number)) for number in [1,2,3,4,5]]
#since it is impossible to retieve the results of our threading computation,
# we need to use#the following approach based on dictionary
results = {}
#manual creation of the thread
#t1 = threading.Thread(target=longsquare, args=(1,results))
#t2 = threading.Thread(target=longsquare, args=(2,results))
#the trule of thumb is put the thread in a list
threads = [threading.Thread(target=longsquare, args=(n, results)) for n in range(0,100)]
[t.start() for t in threads]
[t.join() for t in threads]
#manual starting and joining
#t1.start()
#t2.start()
#t1.join()
#t2.join()

print(results)