# Question 1 Solution
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


# Question 2 Solution
def j2_2017_sol():
	N = int(raw_input())
	k = int(raw_input())
	N_sum = N
	new_N = N
	for i in range(k):
		#new_N = int(str(new_N) + "0")
		new_N = new_N * 10
		N_sum += new_N
	print(N_sum)



# Question 3 Solution
def j3_2017():
	start_coord = raw_input().split()
	xs = int(start_coord[0])
	ys = int(start_coord[1])
	end_coord = raw_input().split()
	xe = int(end_coord[0])
	ye = int(end_coord[1])
	batt = int(raw_input())
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


# Question 4 Answer

def choose_hour(hour):
    if hour == 11:
        return 12
    if hour == 12:
        return 1
    else:
        return hour + 1

def arithmetic_check(time_str):
    diff = float('inf')
    # remove the ":" character in the time string
    time_str = ''.join(time_str.split(':'))
    print time_str
    for i in range(len(time_str) - 1):
        if diff == float('inf'):
            diff = int(time_str[i+1]) - int(time_str[i])
            continue
        if int(time_str[i+1]) - int(time_str[i]) != diff:
            return False
    return True

def J4_2017_Sol():
    mins = int(raw_input())
    hour, minute = 12, 0
    count = 0
    for i in range(mins):
        time_str = ''
        if minute == 59:
            hour = choose_hour(hour)
            time_str += str(hour)
            time_str += '00'
            minute = 0
        elif minute < 9:
            time_str += str(hour)
            minute += 1
            time_str += str(0) + str(minute)
        else:
            time_str += str(hour)
            minute += 1
            time_str += str(minute)

        if arithmetic_check(time_str):
            count += 1      
    print count

# Question 5 answer

# Disclaimer: I found the answer of this question on github, however,
# I don't think it is the best solution to the problem, or the one
# that makes the most sense. Please feel free to upload your solution
# to this problem if you think up one! 

def get_length(height):
    lengths = count_sort[:]
    
    a = max(1, height - 2000)
    b = height - a
    
    num_boards = 0
    
    while (a <= (height //2)):
        if a == b:
            boards = lengths[a] // 2
            lengths[a] -= boards * 2
            
            num_boards += boards
        else:
            boards = min(lengths[a], lengths[b])
            
            lengths[a] -= boards
            lengths[b] -= boards
            
            num_boards += boards
        a += 1
        b -= 1
    return num_boards

def J5_2017_Sol():
    count_sort = [0 for i in range(2001)]
    
    N = int(input())
    L = list(map(int, input().split()))
    for Li in L:
        count_sort[Li] += 1
    print(count_sort)
    
    max_boards = 0
    max_board_length = 0
    for i in range(2, 4001):
        board = get_length(i)
        if board > max_boards:
            max_boards = board
            max_board_length = 0
        if board == max_boards:
            max_board_length += 1
    print(max_boards, max_board_length)    


