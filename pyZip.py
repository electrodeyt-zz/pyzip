#PyZip
#Command line unzip
#Copyright (c) Alexander Richards
#Licensed under CC Attribution
import zlib
import shutil
import os
try:
    while True:
        print("PyZip 0.1")
        print("Commands: unzip, zip, exit")
        tempinput = input()
        if tempinput == "zip":
            print("PyZip does currently not support passwords. Please note this.")
            print("Enter Directory:")
            temp1name = input()
            print("Enter Directory to be ziped. DO NOT ENTER A FILE:")
            temp2path = input()
            print("The name of the Archive is the Name of the Directory.")
            print("Ziping. This may take some time.")
            print("Until it finishes or fails, no more output will apear.")
            os.chdir(temp2path)
            shutil.make_archive(temp2path, 'zip', temp2path)
            print("Done.")

        if tempinput == "unzip":
            print("PyZip does currently not support passwords. Please note this.")
            print("Please enter Filename and Directory, or if it is in the current directory please enter the Name (including .zip for both)")
            temp1name = input()
            if not zipfile.is_zipfile(temp1name):
                print("File is not a Zip File.")
                break
            print("File is a zip File. Please enter path.")
            temp2path = input()
            zipfile1 = zipfile.ZipFile(temp1name,"r")
            print("Extracting. This may take some time, depending on the size of the Archive.")
            print("Until it finishes or fails, no more output will apear.")
            zipfile1.extractall(temp2path)
            zipfile1.close()
            print("Done.")

        if tempinput == "exit":
            raise SystemExit

        
except Exception as e:
    print(str(e))
    if not e == "SystemExit":
        print("A bad happend. PyZip will now close.")
