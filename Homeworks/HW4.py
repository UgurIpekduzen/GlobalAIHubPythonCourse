import random as rnd
import os

# Ekranı temizler.
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Word:
    # Eğer girilen bir kelime yoksa daha önce oluşturulan Word nesnesindeki kelime değeri gönderilmelidir.
    def __init__(self, word = " ", length = 0):
        self.size = length if word == " " and length != 0 else len(word)
        self.chars = ["_" for i in range(length)] if word == " " and length != 0 else list(word.upper())

    def get_chars(self):
        return self.chars
    
    def get_size(self):
        return self.size
    
    def set_word(self, new_word):
        self.chars = new_word

    # Harf liste şeklinde parçalanan kelimeyi string değere çevirir.
    def list_to_str(self):
        string = ""
        for ch in self.chars:
            string += ch
        return string

class Hangman:
    
    def __init__(self, word):
        self.secret = Word(word) # Tutulan kelime
        self.result = Word(length=self.secret.get_size()) # Oyuncunun harf tahminleriyle doldurulacak boşluklar
        self.num_of_unknown_chars = self.secret.get_size() # Oyun sırasında bulunamamış harf sayısı
    
    def guess(self):
        cls()
        guess = ""
         # Oyuncu 10 doğru harf tahmin etme hakkı vardır.
        for turn in range(10, 0, -1):
            # Harf tahmin süreci, oyuncu tüm harfleri erken bulursa tamamlanır ve kelime tahminine geçilir.
            if self.num_of_unknown_chars != 0:
                while True:
                    print(f"Harf tahmin hakkı: {turn}")
                    print(f"Bilinmeyen harf sayısı: {self.num_of_unknown_chars}")
                    print(self.result.get_chars())
                    guess = input("Bir harf tahmin edin: ")
                    guess = guess.upper()
                    # Yapılan tahmin bir kelime ise tekrar denenir.
                    if len(guess) == 1:
                        break
                    else:
                        cls()
                        print("Yaptığınız tahmin bir harf değil, lütfen tekrar deneyin!")
                
                secret_chars = self.secret.get_chars()
                result_chars = self.result.get_chars()
                indexes = get_index_positions(secret_chars, guess)
                # Eğer tahmin edilen harf, tutulan kelimede mevcutsa ekrandaki boşluklara yazdırılır, 
                # mevcut değilse doğru harf tahmin sayısından düşülüp yeni bir tahmin alınır.
                if len(indexes) != 0: 
                    cls()
                    result_chars = replace_chars(result_chars, guess, indexes)
                    self.result.set_word(result_chars)
                    self.num_of_unknown_chars -= len(indexes)
                else: 
                    cls()
                    print("Yaptığınız harf tahmini kelimede mevcut değildir!")
            else:
                break
        
        while True:
                guess = input("Lütfen kelimeyi girin: ")
                if len(guess) > 1:
                    break
                else:
                    print("Yaptığınız tahmin bir kelime değil, lütfen tekrar deneyin!")
        
        secret_str = self.secret.list_to_str()

        if guess.upper() == secret_str:
            print(f"Tebrikler doğru bildiniz, kelimeniz: {secret_str}")
        else:
            print(f"Maleesef, tahmininiz doğru değil. Oyun Bitti! Kelimeniz: {secret_str}")

# Oyuncu tarafında görünen boşlukların doğru harf tahminleriyle doldurulmasında kullanılır.
def replace_chars(list_of_chars, char, indexes):
    for i in indexes:
        list_of_chars[i] = char
    return list_of_chars

# Yapılan harf tahminin tutulan kelimedeki indislerini bulmakta kullanılır. 
def get_index_positions(list_of_chars, char):
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # İstenen harf kelimede baştan aşağı aranır.
            index_pos = list_of_chars.index(char, index_pos)
            # Harfin kelimedeki konumu listeye eklenir. 
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError:
            break
    
    return index_pos_list

def main():
    words = ['rainbow', 'computer', 'science', 'programming', 
         'python', 'mathematics', 'player', 'condition', 
         'reverse', 'water', 'board', 'geeks'] 
    # Kelime listinden rasgele bir kelime seçilir ve oyun başlatılır.
    game = Hangman(rnd.choice(words))
    game.guess()
    
    return 0

if __name__ == "__main__":
    main()