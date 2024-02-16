def j1_2017_sol():
	x = int(raw_input())
	y = int(raw_input())
	if x > 0 and y > 0:
		print(1)
	elif x < 0 and y > 0:
		print(2)
	elif x < 0 and y < 0:
		print(3)
	else:
		print(4)



def j2_2017_sol():
	N = int(raw_input())
	k = int(raw_input())
	N_sum = N
	new_N = N
	for i in range(k):
		new_N = int(str(new_N) + "0")
		N_sum += new_N
	print(N_sum)



def j1_2016_sol():
	wins = 0
	for i in range(6):
		res = raw_input()
		if res == "W":
			wins += 1
	if wins >= 5:
		print(1)
	elif wins >= 3:
		print(2)
	elif wins >= 1:
		print(3)
	else:
		print(-1)


def j2_2016_sol():
	matrix = []
	for i in range(4):
		line = raw_input()
		str_array = line.split()
		int_array = [int(s) for s in str_array]
		matrix.append(int_array)
	sum_1 = sum(matrix[0])
	for i in range(1, 4):
		if sum(matrix[i]) != sum_1:
			print("not magic")
			return
	for i in range(4):
		row_sum = 0
		for j in range(4):
			row_sum += matrix[j][i]
		if row_sum != sum_1:
			print("not magic")
			return
	print("magic")


if __name__ == "__main__":
	#j1_2017_sol()
	#j2_2017_sol()
	#j1_2016_sol()
	j2_2016_sol()