
import tempfile
import sys
import getpass
username = getpass.getuser()


# input_file = open("Rainmeter.ini", "r", 1)
# output_file = open("Rainmeter_new.ini","w")
input_file = tempfile.TemporaryFile(mode = "r+")

input_real = open("C:\\Users\\"+username+"\\AppData\\Roaming\\Rainmeter\\Rainmeter.ini", "r")

for line in input_real:
	input_file.write(line)

input_file.seek(0)
input_real.close()


output_file = open("C:\\Users\\"+username+"\\AppData\\Roaming\\Rainmeter\\Rainmeter.ini", "w")

skins_file = open("skins.txt", "r", 1)
global skins_list
skins_list = []

for line in skins_file:
	skins_list.append('[' + line.rstrip())
print ('arranging anything starting with ', skins_list)
skins_file.close()

active = False
x = -1
y = -1

for line in input_file:
	# line.replace(" ", "")

	if line[0] == '[' and any(line.startswith(name) for name in skins_list):
		# print("triggered by " + line)
		active = True

	# if line[0] == '[':
	# 	currentskin = line

	if not active:
		output_file.write(line)
	else:
		if line[0:7].lower() == 'windowx':
		


			


input_file.close()
output_file.close()









