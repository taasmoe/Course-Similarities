import timeit
import numpy as np

start = timeit.default_timer()

courses = np.load("courses.npy")

print(courses)

end = timeit.default_timer()

print("Completed in", start-end, "seconds")
