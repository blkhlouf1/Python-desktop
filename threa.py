import subprocess
import Pmw
import os
import threading
import time

# define the function callback to open the browser Site **************
def callback():
    Users = "su1"
    strin = '"C:\Program Files\Cyberfox\Cyberfox.exe"'+' -p ' + Users
    print(strin)
    p = subprocess.Popen(strin)

    

#Create Input ********************

start_time = time.time()
data = ['a','b','v','d','e','f','g','h']
arr = []
counter = 0

maxconnections = 2
# ...
pool_sema = threading.BoundedSemaphore(value=maxconnections)
print(pool_sema)
with pool_sema:
    
    try:
        threading.Thread(target=callback).start()
        pool_sema.release()
    finally:
        print("--- %s seconds ---" % (time.time() - start_time))
        


input('done.')
exit()
