from time import *
from tracemalloc import start

start_time = time()
phrase = input(' Escribe una reseña : ')
end_time = time()

total_time = end_time - start_time
symbols = len(phrase)
print(' Velocidad de tipeo:', symbols/total_time*60)