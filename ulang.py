import funlink as fl

def parse(line):
	res = line.split(" ")
	for i in range(0,res.count("")):
		res.pop(res.index(""))
	return res

def gethead(args):
	return args[0]

def getbody(args):
	body = []
	start = False
	for a in args:
		if a.startswith("{"):
			start = True
			body.append(a[1:])
		elif start and a.endswith("}"):
			body.append(a[:len(a)-1])
			return body
		elif start:
			if a == args[len(args)-1]:
				print("Error: } expected; getbody function in ulang.py")
			else:
				body.append(a)

def get_arr_body(args):
	body = []
	start = False
	for a in args:
		if a.startswith("["):
			start = True
			body.append(a[1:])
		elif start and a.endswith("]"):
			body.append(a[:len(a)-1])
			return body
		elif start:
			if a == args[len(args)-1]:
				print("Error: ] expected; getbody function in ulang.py")
			else:
				body.append(a)

def get_instructions(body):
	insts = []
	temp_inst = []
	for i in range(0,len(body)):
		if body[i] in [";\n",";"]:
			insts.append(temp_inst[:])
			temp_inst.clear()
		elif body[i] != "":
			temp_inst.append(body[i])
	if temp_inst.__len__() > 0:
		insts.append(temp_inst[:])
		temp_inst.clear()

	return insts

def get_arr_values(arr_body):
	insts = []
	temp_vals = []
	for i in range(0, len(arr_body)):
		if arr_body[i] in [",\n", ","]:
			insts.append(temp_vals[:])
			temp_vals.clear()
		elif arr_body[i] != "":
			temp_vals.append(arr_body[i])
	if temp_vals.__len__() > 0:
		insts.append(temp_vals[:])
		temp_vals.clear()

	return insts

def execute(inst):
	args = []
	if type(inst) is str:
		args = parse(inst)
	elif type(inst) is list:
		args = inst
	else:
		print("inst is neither list nor str (ulang.py)")
	fl.cmds[gethead(args)](args)