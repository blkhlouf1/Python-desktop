import os
import shutil




def create_profiles(profile_name, start_number, final_number):

    for i in range(start_number,final_number+1):
        # Source path
        src = r'C:\Users\Bilal\AppData\Roaming\8pecxstudios\Cyberfox\Profiles\ajgr52r3.default'
        # Destination path
        dest = r'C:\Users\Bilal\AppData\Roaming\8pecxstudios\Cyberfox\Profiles\\'+profile_name+str(i)
        # Copy the content of source to destination
        destination = shutil.copytree(src, dest)
        #Add profile to Profile manager
        f = open("C:\\Users\Bilal\AppData\Roaming\8pecxstudios\Cyberfox\profiles.ini", "a")
        Profilename = "\n\n[Profile"+str(i)+"]"+"\nName=su"+str(i)+"\nIsRelative=1"+"\nPath=Profiles/su"+str(i)
        f.write(Profilename)
        f.close() 


def main():
    create_profiles("su", 10, 15)
    
if __name__ == "__main__":
    main()
