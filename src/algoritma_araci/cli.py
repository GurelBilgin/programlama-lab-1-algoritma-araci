"""Komut satırı menüsü."""

from __future__ import annotations

from pathlib import Path

from .algorithms import (
    closest_pair_to_target,
    fibonacci,
    gcd,
    is_prime,
    kth_smallest_unique,
    matrix_multiply,
    min_value,
    parse_number_list,
    repeated_elements,
    sqrt_newton,
    word_frequency_from_file,
)


MENU = """
================ ALGORİTMA ARACI ================
1. k'ncı en küçük benzersiz elemanı bul
2. Hedef sayıya en yakın çifti bul
3. Tekrar eden elemanları bul
4. Matris çarpımı yap
5. Kelime frekanslarını hesapla
6. En küçük değeri bul
7. Newton yöntemiyle karekök hesapla
8. EBOB hesapla
9. Asal sayı kontrolü yap
10. Fibonacci sayısı hesapla
11. Çıkış
==================================================
"""


def read_numbers() -> list[float]:
    raw_value = input("Sayıları virgülle ayırarak girin: ")
    return parse_number_list(raw_value)


def read_int(prompt: str) -> int:
    return int(input(prompt))


def read_float(prompt: str) -> float:
    return float(input(prompt))


def read_matrix(matrix_name: str) -> list[list[float]]:
    print(f"\n{matrix_name}")
    row_count = read_int("Satır sayısı: ")
    column_count = read_int("Sütun sayısı: ")

    if row_count <= 0 or column_count <= 0:
        raise ValueError("Satır ve sütun sayıları pozitif olmalıdır.")

    matrix: list[list[float]] = []
    for row_index in range(row_count):
        while True:
            raw_row = input(
                f"{row_index + 1}. satırı {column_count} sayı olacak şekilde virgülle girin: "
            )
            row = parse_number_list(raw_row)
            if len(row) == column_count:
                matrix.append(row)
                break
            print(f"Bu satırda {column_count} sayı olmalıdır. Tekrar deneyin.")

    return matrix


def print_matrix(matrix: list[list[int | float]]) -> None:
    for row in matrix:
        print("  ".join(f"{value:g}" for value in row))


def run_menu() -> None:
    while True:
        print(MENU)
        choice = input("Seçiminiz: ").strip()

        try:
            if choice == "1":
                numbers = read_numbers()
                k = read_int("k değerini girin: ")
                print(f"Sonuç: {kth_smallest_unique(numbers, k):g}")

            elif choice == "2":
                numbers = read_numbers()
                target = read_float("Hedef sayıyı girin: ")
                number_a, number_b = closest_pair_to_target(numbers, target)
                print(f"En yakın çift: {number_a:g}, {number_b:g}")
                print(f"Çiftin toplamı: {number_a + number_b:g}")

            elif choice == "3":
                numbers = read_numbers()
                print(f"Tekrar eden elemanlar: {repeated_elements(numbers)}")

            elif choice == "4":
                matrix_a = read_matrix("Birinci matris")
                matrix_b = read_matrix("İkinci matris")
                result = matrix_multiply(matrix_a, matrix_b)
                print("\nÇarpım sonucu:")
                print_matrix(result)

            elif choice == "5":
                file_path = Path(input("Metin dosyası yolunu girin: ").strip())
                frequencies = word_frequency_from_file(file_path)
                print("\nKelime frekansları:")
                for word, count in sorted(frequencies.items()):
                    print(f"{word}: {count}")

            elif choice == "6":
                numbers = read_numbers()
                print(f"En küçük değer: {min_value(numbers):g}")

            elif choice == "7":
                number = read_float("Karekökü alınacak sayıyı girin: ")
                initial_raw = input("İlk tahmin değeri; boş bırakılırsa otomatik seçilir: ").strip()
                initial_guess = float(initial_raw) if initial_raw else None
                result = sqrt_newton(number, initial_guess=initial_guess)
                print(f"Sonuç: {result}")

            elif choice == "8":
                number_a = read_int("Birinci tam sayıyı girin: ")
                number_b = read_int("İkinci tam sayıyı girin: ")
                print(f"EBOB: {gcd(number_a, number_b)}")

            elif choice == "9":
                number = read_int("Bir tam sayı girin: ")
                if is_prime(number):
                    print(f"{number} asal sayıdır.")
                else:
                    print(f"{number} asal sayı değildir.")

            elif choice == "10":
                n = read_int("Fibonacci dizisindeki sıra değerini girin: ")
                print(f"fib({n}) = {fibonacci(n)}")

            elif choice == "11":
                print("Programdan çıkılıyor.")
                break

            else:
                print("Geçersiz seçim. Lütfen 1-11 arasında bir değer girin.")

        except (ValueError, FileNotFoundError) as error:
            print(f"Hata: {error}")

        input("\nDevam etmek için Enter'a basın...")


def main() -> None:
    run_menu()


if __name__ == "__main__":
    main()
