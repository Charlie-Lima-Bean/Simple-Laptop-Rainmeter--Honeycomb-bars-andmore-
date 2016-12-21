
import tempfile
import sys
import getpass
username = getpass.getuser()

def buckets(x, y):

	dX = 90
	dY = 80
	x_offset = 85
	y_offset = 60

	ret = [0,0]
	x -= x_offset
	y -= y_offset

	gridY = int(round(y/dY))

	ret[1] = gridY * dY + y_offset

	if gridY % 2 == 0:
		ret[0] += dX//2
		x -= dX//2

	gridX = int(round(x/dX))
	ret[0] += gridX *dX + x_offset

	return ret


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
			line = line.replace(" ", "")
			x = int(line[8:len(line)-1])

		elif line[0:7].lower() == 'windowy':
			line = line.replace(" ", "")
			y = int(line[8:len(line)-1])
		else:
			output_file.write(line)

		if x != -1 and y != -1:
			coords = buckets(x, y)
			output_file.write('WindowX='+str(coords[0])+'\n')
			output_file.write('WindowY='+str(coords[1])+'\n')

			# print("corrected ({:d},{:d}) to ({:d},{:d})".format(x,y,coords[0],coords[1]));
			# print('writing at ' + currentskin)
			x = -1
			y = -1
			active = False


			


input_file.close()
output_file.close()









