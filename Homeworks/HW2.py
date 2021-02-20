'''
Homework 2:
	Write a program that includes information about the grades of 5 students in 
	a school.
	- Keep these students' grades in a list. (Midterm, final, homework)
	- Keep students' names in a list. (Name, surname)
	- Create a dictionary named info and put all the information of students in 
	a dictionary.
	- Sort and list the students' grades here in descending order and 
	congratulate the students' grades here in descending order and congratulate 
	the student with the highest score. 
'''

def main():
	student_names = []
	student_grades = []
	
	# Kullanıcıdan 5 tane öğrencinin adı, soyadı, vize, final ve ödev notu girilir.
	for i in range(5):
		name = input("Öğrenci Adı: ")
		surname = input("Öğrenci Soyadı: ")
		student_names.append((name, surname))
		midterm = int(input("Vize Puanı: "))
		final = int(input("Final Puanı: "))
		homework = int(input("Ödev Puanı: "))
		student_grades.append((midterm, final, homework))
		print("------------------------------------")
	# Öğrencilerin adı, soyadı, vize, final ve ödev notu bilgileri bir dictionaryde toplanır.
	information_dict = {f'Student {i}': {'Name': student_names[i], 'Grade': student_grades[i]} for i in range(5)}
	
	print("====================================")
	print("| Ad | Soyad | Vize | Final | Ödev |")
	print("====================================")
	for info in information_dict.items():
		print("| {} | {} | {} | {} | {} |".format(info[1]['Name'][0],
										info[1]['Name'][1],
										info[1]['Grade'][0],
										info[1]['Grade'][1],
										info[1]['Grade'][2]))
		# Öğrencinin vize final ve ödev notunun ortalaması alınıp öğrencinin puanı hesaplanır.
		info[1]['Score'] = round((info[1]['Grade'][0] + 
								info[1]['Grade'][1] +
								info[1]['Grade'][2])/3, 2)
		print("------------------------------------")
	
	# Öğrenciler puan bilgisi kullanılarak büyükten küçüğe sıralanır.
	des_dict = dict(sorted(information_dict.items(), key=lambda kv: kv[1]['Score'], reverse=True))
	
	print("=====================")
	print("| Ad | Soyad | Puan |")
	print("=====================")
	for info in des_dict.items():
		print("| {} | {} | {} |".format(info[1]['Name'][0],
					info[1]['Name'][1],
					info[1]['Score']))
		print("-----------------------------")
	
	des_list = list(des_dict.items())
	# En yüksek puana sahip öğrenci listenin en üstündedir, dolayısıyla tebrik edilecek öğrenci seçilmiş olur.
	print("Tebrikler, {} {}! Skorunuz: {}".format(des_list[0][1]['Name'][0],
													des_list[0][1]['Name'][1], 
													des_list[0][1]['Score']))
if __name__ == "__main__":
	main()