from shutil import copyfile
import getpass
username = getpass.getuser()

copyfile("start.ini", "C:\\Users\\"+username+"\\AppData\\Roaming\\Rainmeter\\Rainmeter.ini")