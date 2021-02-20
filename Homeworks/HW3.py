'''
Homework 3:
	Write two functions. The name of the first function is prime_first. The name of the 
    second function is prime_second. You must use these two functions inside the for loop. 
    Ensure that the for loop takes values between 0 - 1000. Press the prime numbers between 
    0 - 500 on the screen with the prime_first function. Press the prime numbers between 
    500 - 1000 on the screen with the prime_second function.
'''
def prime_first(num):
    if 0 <= num <= 500:
        if num == 0:
            print("-------------------------------------------------")
            print("0 ve 500 arasındaki asal sayılar: ")
            print("-------------------------------------------------")
        if num > 1:
            # Her 60 sayıda bir alt satıra geçilsin.
            if num % 60 == 0: print()
            for i in range(2, num):
                # Eğer 1 ve kendisinden farklı bir böleni varsa üretilen sayı asal değildir.
                if (num % i) == 0:
                    break
            else: 
                # Eğer 1 ve kendisinden farklı bir böleni yoksa üretilen sayı asaldır.
                print(num, end= ",")
        if num == 500:
            print()
            print("-------------------------------------------------")
            
    else: 
        return 0

def prime_second(num):
    if 500 <= num <= 1000:
        if num == 500:
            print("-------------------------------------------------")
            print("500 ve 1000 arasındaki asal sayılar: ")
            print("-------------------------------------------------")
        if num > 1:
            # Her 70 sayıda bir alt satıra geçilsin.
            if num % 70 == 0: print()
            for i in range(2, num):
                # Eğer 1 ve kendisinden farklı bir böleni varsa üretilen sayı asal değildir.
                if (num % i) == 0:
                    break
            else: 
                # Eğer 1 ve kendisinden farklı bir böleni yoksa üretilen sayı asaldır.
                print(num, end = ",")
        if num == 1000:
            print()
            print("-------------------------------------------------")
            
    else: 
        return 0

def main():
    for i in range(0, 1001):
        prime_first(i)
        prime_second(i) 
    return 0

if __name__ == "__main__":
    main()