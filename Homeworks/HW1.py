'''
Homework 1:
	Generating a 3x3 matrix with 9 random prime numbers.
	(You have to do it using the for loop)
'''

from random import randint
                                                 
def main():
	# Boş matris oluştulur
	rows, cols = (3, 3)
	prime_matrix = [[0 for i in range(cols)] for j in range(rows)]

	# Matrisin içi asal sayılarla doldurulur
	for row in range(rows):
		for col in range(cols):	
			not_prime = True
			# Yeni bir asal sayı bulunana kadar devam edecek olan while döngüsü
			while not_prime:
				# 1 ile 100 arasında rasgele bir sayı üretilir.
				rand_num = randint(1, 100)
				if rand_num > 1:
					for i in range(2, rand_num):
						# Eğer 1 ve kendisinden farklı bir böleni varsa üretilen sayı asal değildir.
						if (rand_num % i) == 0:
							break
					else: 
						# Eğer 1 ve kendisinden farklı bir böleni yoksa üretilen sayı asaldır.
						if any(rand_num in sub for sub in prime_matrix) is False:
							# Üretilen asal sayı matristeki sayılardan farklı ise matrise eklenir.
							prime_matrix[row][col] = rand_num
							not_prime = False
					
	for i in range(rows):
		for j in range(cols):
			print(prime_matrix[i][j], end=" ")
		print()

if __name__ == "__main__":
	main()