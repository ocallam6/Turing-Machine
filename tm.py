
def padding(input_string):
	if(input_string[0]!='B'):
		input_string.insert(0,'B')
	if(input_string[len(input_string)-1]!='B'):
		input_string.append('B')
	return input_string

def quintuples_input():
	quintuples=[]
	done=['Done','done','DONE']
	print('------------------------------------------------')
	print('Enter quintuples, pressing enter after each one.')
	print('Quintuples should be of form: n01Lm')
	print('Where n,m are nonegative integers.')
	print('B is the blank symbol')
	print('There must be a quintuple with 0 as initial state.')
	print('Type "done" when finished')
	print('------------------------------------------------')

	while True:
		x=input()
		if(x in done):
			break
		else:
			quintuples.append(x)
	return quintuples


def machine(quintuples,input_string,state,cell):
	if(cell<0):
		input_string.remove('B')
		print(''.join(input_string))
		return
	left=['l','L']
	right=['r','R']
	input_string=padding(input_string)
	possible_quintuples=[]
	actual_quintuple=[]
	for i in range(0,len(quintuples)):
		if(state==quintuples[i][0]):
			possible_quintuples.append(quintuples[i])
	for i in range(0,len(possible_quintuples)):
		if(input_string[cell]==possible_quintuples[i][1]):
			actual_quintuple.append(possible_quintuples[i])
	if not actual_quintuple:
		input_string.remove('B')
		input_string.remove('B')
		print(''.join(input_string))
		return
	if(len(actual_quintuple)>1):
		print('Inconsistent Turing Machine')
		exit()
	else:

		input_string[cell]=actual_quintuple[0][2]
		if(actual_quintuple[0][3] in left):
			cell=cell-1
		if(actual_quintuple[0][3] in right):
			cell=cell+1
		state=actual_quintuple[0][4]
		machine(quintuples,input_string,state,cell)


def input_binary():
	print('What is the input string in binary?')
	return list(input())

def main():
	initial_cell=1
	initial_state='0'
	input_string=input_binary()
	quintuples=quintuples_input()
	machine(quintuples,input_string,initial_state,initial_cell)


main()
	
