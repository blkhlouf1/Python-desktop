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

start_time = time.time()from multiprocessing import Pool
import subprocess
import time
from multiprocessing.pool import ThreadPool
import random
import threading
import time

MAX_THREADS = 15
print_lock = threading.Lock()


def open_profile(profilename):
		strin = '"C:\Program Files\Cyberfox\Cyberfox.exe"'+' -p ' + profilename + " -no-remote" + " imacros://run/?m=saber.js"
		subprocess.run(strin)
		time.sleep(10)




def export(profilename):
    pool = ThreadPool(processes=MAX_THREADS)
    pool.map_async(open_profile, profilename)
    pool.close()
    pool.join()  # block until all threads exit

def main():
	profiles = []
	for i in range (1,600):
		profile_name = "su"+ str(i)
		profiles.append(profile_name)
	print(profiles)
	export(profiles)

if __name__ == "__main__":
    main()