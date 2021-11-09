from multiprocessing import Pool
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
	for i in range (1,201):
		profile_name = "su"+ str(i)
		profiles.append(profile_name)
	print(profiles)
	export(profiles)

if __name__ == "__main__":
    main()