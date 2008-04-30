import random
import cStringIO

file_handle = open("./ex_grm.dat")
grammar_lines = file_handle.readlines()


nonTerminalSymbols = {}
terminalSymbols = {}
target = nonTerminalSymbols
startSym = None
totalOutput = None

for line in grammar_lines:
	if "TERMINALS" in line:
		target = terminalSymbols
		continue

	elif "TERMINAL" in line or line == '\n':
		continue


	prod_def = line.split(" -> ")
	target[prod_def[0]] = []

	if startSym == None:
		startSym = prod_def[0]
	
	for production in prod_def[1].split(" | "):
		target[prod_def[0]].append(production.strip())

'''
print "Start Symbol: " + startSym

print "Terminal Symbols:"
for key in terminalSymbols.keys():
	print str(key) + " , " + str(terminalSymbols[key])

print "Non-Terminal Symbols:"
for key in nonTerminalSymbols.keys():
        print str(key) + " , " + str(nonTerminalSymbols[key])
'''

def produce(sym):
	terminal = terminalSymbols.get(sym)

	if not terminal:
		productions = nonTerminalSymbols[sym]
		production = random.choice(productions)
		for symbol in production.split():
			produce(symbol)
	
	elif terminal[0] == '\\n':
		output('\n')
	
	else:
		output(terminal[0] + ' ')

	return

def output(symbol):
	global totalOutput
	totalOutput.write(str(symbol))
	return

def getFuzzInput(spec, seed):
	global totalOutput
	totalOutput = cStringIO.StringIO()
	produce(startSym)
	if spec=='postscript':
		return totalOutput.getvalue()

'''
print "\nNow producing..."
print getFuzzInput('postscript')
'''
