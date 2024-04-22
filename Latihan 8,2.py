def load_soal(file_path):
    with open(file_path, 'r') as file:
        return [tuple(map(str.strip, line.split("||"))) for line in file]

def main():
    nama_file = "soal.txt"
    soal = load_soal(nama_file)
    
    for idx, (pertanyaan, jawaban_benar) in enumerate(soal, start=1):
        print(pertanyaan)
        jawaban = input("Jawab: ").strip().lower()
        if jawaban == jawaban_benar.lower():
            print("Jawaban benar!")
        else:
            print("Jawaban salah!")
        print()

if __name__ == "__main__":
    main()