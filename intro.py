import multiprocessing as mp
import random
import string

# Define an output queue
output = mp.Queue()

# define a example function
def rand_string(length, output, x):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    print 'process happening ' + str(x)
    rand_str = ''.join(random.choice(
                    string.ascii_lowercase
                    + string.ascii_uppercase
                    + string.digits)
               for i in range(length))
    print rand_str + str(x)
    #output.put(rand_str + str(x))

# Setup a list of processes that we want to run
processes = [mp.Process(target=rand_string, args=(5, output, x)) for x in range(14)]
"""
pool = mp.Pool(processes=4)
results = [pool.apply_async(cube, args=(x,)) for x in range(1,7)]
output = [p.get() for p in results]
print(output)
"""
# Run processes
for p in processes:
	print 'process starting'
	p.start()

# Exit the completed processes
for p in processes:
	print 'process quiting'
	p.join()

# Get process results from the output queue
#results = [output.get() for p in processes]

#print(results)