def insert(filename, key, value):
	f = open(filename, 'a')
	f.write(key + '\t' + value + '\n')
	f.close()
	
def select_one(filename, key):
	f = open(filename, 'r')
	for row in f:
		(k, v) = row.split('\t', 1)
		if k == key:
			return v[:-1]
	f.close()

def delete(filename, key):
	f = open(filename, 'r')
	result = open('result.txt', 'w')
	for (row) in f:
		(k, v) = row.split('\t', 1)
		if k != key:
			result.write(row)
	f.close()
	result.close()
	import os
	os.replace('result.txt', filename)

def update(filename, key, value):
    f = open(filename, 'r')
    result = open('result.txt', 'w')
    for (row) in f:
    	(k, v) = row.split('\t', 1)
    	if k == key:
    		result.write(key + '\t' + value + '\n')
    	else:
    		result.write(row)
    f.close()
    result.close()
    import os
    os.replace('result.txt', filename)

