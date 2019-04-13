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

# Store original output stream
orig_stdout = sys.stdout

# Program strings broken down

unroll_string = """
	if ( {} > 0 ) {{ """

mult_string	= """	{} = {} * {} ;"""
mult_alt = """	{} *= {} ;"""

subt_string = """	{} -- ; """
subt_alt = """	{} = {} - 1 ;"""

loop_string = """
	while ( {} > 0 ) {{ """

close_braces = """}"""

# Create Directory
dir_name = 'fact1_loop'
new_dir = os.path.join(os.getcwd(), dir_name)
os.mkdir(new_dir)

for unrolls in range(2):
	for copy in range(20):
	
		# Create file
		f  = open(new_dir + '/'+ 'fact1_loop-copies' + str(copy) + '-unrolls' + str(unrolls) + '.c','w+')
		sys.stdout = f

		# Should not be a keyword (take only compilable examples)
		var_i = random_name(random.randint(1, 21))
		var_fact = random_name(random.randint(1, 21))
	

		# Print unrolls with indentif random.randint(0,1) == 0:
		for i in range(unrolls):
			print(add_indent(i, unroll_string.format(var_fact)))
			
			if random.randint(0,1) == 0:
				print(add_indent(i+1, mult_string.format(var_i, var_i, var_fact)))
			else:
				print(add_indent(i+1, mult_alt.format(var_i, var_fact)))
			
			if random.randint(0,1) == 0:
				print(add_indent(i+1, subt_string.format(var_fact)))
			else:
				print(add_indent(i+1, subt_alt.format(var_fact, var_fact)))

		print(add_indent(unrolls, loop_string.format(var_fact)))
		if random.randint(0,1) == 0:
			print(add_indent(unrolls+1, mult_string.format(var_i, var_i, var_fact)))
		else:
			print(add_indent(unrolls+1, mult_alt.format(var_i, var_fact)))
		if random.randint(0,1) == 0:
			print(add_indent(unrolls+1, subt_string.format(var_fact)))
		else:
			print(add_indent(unrolls+1, subt_alt.format(var_fact, var_fact)))
		print(add_indent(unrolls + 1, close_braces))
	
		# Print close braces for unrolls
		for i in range(unrolls):
			print(add_indent(unrolls - i, close_braces))
	
		f.close()

sys.stdout = orig_stdout
