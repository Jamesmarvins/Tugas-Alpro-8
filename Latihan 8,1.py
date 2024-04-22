def bandingkan_file(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for i, (line1, line2) in enumerate(zip(f1, f2), start=1):
            if line1 != line2:
                print(f"Perbedaan pada baris {i}:")
                print(f"File 1: {line1.strip()}")
                print(f"File 2: {line2.strip()}")

    print("Tidak ada perbedaan antara kedua file." if i == 0 else "")

bandingkan_file('file1.txt', 'file2.txt')