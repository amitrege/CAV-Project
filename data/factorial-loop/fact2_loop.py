"""
	while(fact > 0) {
		i = i * fact;
		fact--; 	
	}
"""

import sys
import os
import string
import random

# Add indents based on unroll level
def add_indent(level, string):
	lines = string.splitlines()
	indent = ''
	for i in range(level):
		indent = indent + '\t'
	
	return ''.join(['\n' + indent + line for line in lines])

# Generate random string
def id_generator(size, chars):
	return ''.join(random.choice(chars) for _ in range(size))

# Generate random variable name satisfying C naming conventions
def random_name(size, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
	keywords = set(["auto","double","int","struct","break","else","long","switch","case","enum","register","typedef","char","extern","return","union","continue","for","signed","void","do","if","static","while","default","goto","sizeof","volatile""const","float","short","unsigned"])
	while True:	
		name = id_generator(size, chars)
		if not (name in keywords) and not (name[0] in set(string.digits)):
			return name

# generate a random number except n
def random_no_except_n(start, end, n):
	r = [x for x in range(start, end) if x != n]
	return random.choice(r)

# Store original output stream
orig_stdout = sys.stdout

unroll_string = """
	if ( {} {} {} ) {{ """

mult_string	= """	{} = {} * {} ;"""
mult_alt = """	{} *= {} ;"""

subt_string = """	{} -- ; """
subt_alt = """	{} = {} - 1 ;"""

loop_string = """
	while ( {} {} {} ) {{ """

close_braces = """}"""

final_brace = """} """

# Create Directory
dir_name = 'fact2_loop'
new_dir = os.path.join(os.getcwd(), dir_name)
os.mkdir(new_dir)

for unrolls in range(2):
	for copy in range(20):
	
	    # Create file
		f  = open(new_dir + '/'+ 'fact2_loop-copies' + str(copy) + '-unrolls' + str(unrolls) + '.c','w+')
		sys.stdout = f

		# Should not be a keyword (take only compilable examples)
		var_i = random_name(random.randint(1, 21))
		var_fact = random_name(random.randint(1, 21))

		# Print unrolls with indentif random.randint(0,1) == 0:
		for i in range(unrolls):
			if random.randint(0,3) == 0:
				print(add_indent(i, unroll_string.format(var_fact, '>', random_no_except_n(0,100,0))))
			elif random.randint(0,3) == 1:
				print(add_indent(i, unroll_string.format(var_fact, '<', random.randint(0,100))))
			elif random.randint(0,3) == 2:
				print(add_indent(i, unroll_string.format(var_fact, '<=', random.randint(0,100))))
			else:
				print(add_indent(i, unroll_string.format(var_fact, '>=', random.randint(0,100))))
			
			if random.randint(0,1) == 0:
				if random.randint(0,3) == 0:
				    print(add_indent(i+1, "    {} = {} {} {} ; ".format(var_i, var_i, '+', var_fact)))
				elif random.randint(0,3) == 1:
					print(add_indent(i+1, "    {} = {} {} {} ; ".format(var_i, var_i, '-', var_fact)))
				elif random.randint(0,3) == 2:
					print(add_indent(i+1, "    {} = {} {} {} ; ".format(var_i, var_i, '/', var_fact)))
			else:
				if random.randint(0,3) == 0:
				    print(add_indent(i+1, "    {} {}= {} ; ".format(var_i, '+', var_fact)))
				elif random.randint(0,3) == 1:
				    print(add_indent(i+1, "    {} {}= {} ; ".format(var_i, '-', var_fact)))
				elif random.randint(0,3) == 2:
				    print(add_indent(i+1, "    {} {}= {} ; ".format(var_i, '/', var_fact)))
			
			if random.randint(0,1) == 0:
				if random.randint(0,1) == 0:
				    print(add_indent(i+1, "    {} ++ ; ".format(var_fact)))
			else:
				if random.randint(0,3) == 0:
				    print(add_indent(i+1, "    {} = {} {} 1 ; ".format(var_fact, var_fact, '+')))
				elif random.randint(0,3) == 1:
				    print(add_indent(i+1, "    {} = {} {} 1 ; ".format(var_fact, var_fact, '*')))
				elif random.randint(0,3) == 2:
				    print(add_indent(i+1, "    {} = {} {} 1 ; ".format(var_fact, var_fact, '/')))

		if random.randint(0,3) == 0:
			print(add_indent(unrolls, loop_string.format(var_fact, '>', random_no_except_n(0,100,0))))
		elif random.randint(0,3) == 1:
			print(add_indent(unrolls, loop_string.format(var_fact, '<', random.randint(0,100))))
		elif random.randint(0,3) == 2:
			print(add_indent(unrolls, loop_string.format(var_fact, '<=', random.randint(0,100))))
		else:
			print(add_indent(unrolls, loop_string.format(var_fact, '>=', random.randint(0,100))))
		
		if random.randint(0,1) == 0:
			if random.randint(0,3) == 0:
			    print(add_indent(unrolls+1, "    {} = {} {} {} ; ".format(var_i, var_i, '+', var_fact)))
			elif random.randint(0,3) == 1:
				print(add_indent(unrolls+1, "    {} = {} {} {} ; ".format(var_i, var_i, '-', var_fact)))
			elif random.randint(0,3) == 2:
				print(add_indent(unrolls+1, "    {} = {} {} {} ; ".format(var_i, var_i, '/', var_fact)))
		else:
			if random.randint(0,3) == 0:
				print(add_indent(unrolls+1, "    {} {}= {} ; ".format(var_i, '+', var_fact)))
			elif random.randint(0,3) == 1:
			    print(add_indent(unrolls+1, "    {} {}= {} ; ".format(var_i, '-', var_fact)))
			elif random.randint(0,3) == 2:
			    print(add_indent(unrolls+1, "    {} {}= {} ; ".format(var_i, '/', var_fact)))
			
		if random.randint(0,1) == 0:
			if random.randint(0,1) == 0:
			    print(add_indent(unrolls+1, "    {} ++ ; ".format(var_fact)))
		else:
			if random.randint(0,3) == 0:
			    print(add_indent(unrolls+1, "    {} = {} {} 1 ; ".format(var_fact, var_fact, '+')))
			elif random.randint(0,3) == 1:
			    print(add_indent(unrolls+1, "    {} = {} {} 1 ; ".format(var_fact, var_fact, '*')))
			elif random.randint(0,3) == 2:
				print(add_indent(unrolls+1, "    {} = {} {} 1 ; ".format(var_fact, var_fact, '/')))

		print(add_indent(unrolls + 1, close_braces))
	
		# Print close braces for unrolls
		for i in range(unrolls):
			print(add_indent(unrolls - i, close_braces))
	
		f.close()

sys.stdout = orig_stdout
