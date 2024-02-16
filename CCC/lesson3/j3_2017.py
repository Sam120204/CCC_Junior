start_coord = raw_input().split()
xs = int(start_coord[0])
ys = int(start_coord[1])
end_coord = raw_input().split()
xe = int(end_coord[0])
ye = int(end_coord[1])
batt = int(raw_input())


def j3_2017():
	global xs, ys, xe, ye, batt
	if batt == 0 and xs == xe and ys == ye:
		return True
	elif batt == 0:
		return False
	else:
		return move_car(xs-1, ys, xe, ye, batt) or move_car(xs+1, ys, xe, ye, batt) \
		or move_car(xs, ys-1, xe, ye, batt) or move_car(xs, ys+1, xe, ye, batt)



def move_car(x1, y1, x2, y2, bat):
	bat = bat - 1
	if bat == 0:
		if x1 == x2 and y1 == y2:
			return True
		else:
			return False
	else:
		x_new = x1 + 1
		if move_car(x_new, y1, x2, y2, bat):
			return True
		x_new = x1 - 1
		if move_car(x_new, y1, x2, y2, bat):
			return True
		y_new = y1 + 1
		if move_car(x1, y_new, x2, y2, bat):
			return True
		y_new = y1 - 1
		if move_car(x1, y_new, x2, y2, bat):
			return True
		return False



if __name__ == "__main__":
	if j3_2017():
		print("Y")
	else:
		print("N")