import matplotlib.pyplot as plt
from sorting import sorting

array_length = 50
array = sorting.make_randomly_shuffled_list( array_length )
[arrays,times] = sorting.piksrt(array, debug=True)

output_directory='./piksrt/'
sorting.animate_debug_results([arrays,times], output_directory )

print "Total elapsed time is " + str(sum(times)) + " seconds"

