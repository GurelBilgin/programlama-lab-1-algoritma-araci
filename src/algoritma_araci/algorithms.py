"""Temel algoritma fonksiyonları.

Bu modüldeki fonksiyonlar kullanıcıdan veri almaz ve ekrana çıktı basmaz.
Bu sayede fonksiyonlar hem CLI menüsünde hem de testlerde rahatça kullanılabilir.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from pathlib import Path
from typing import Iterable, Sequence


_WORD_PATTERN = re.compile(r"[0-9A-Za-zÇĞİÖŞÜçğıöşü]+", re.UNICODE)


def kth_smallest_unique(numbers: Sequence[int | float], k: int) -> int | float:
    """Listedeki benzersiz değerler arasından k'ncı en küçük elemanı döndürür.

    Args:
        numbers: Sayılardan oluşan liste/tuple.
        k: 1'den başlayan sıra numarası.

    Raises:
        ValueError: Liste boşsa veya k geçersizse.
    """
    if not numbers:
        raise ValueError("Liste boş olamaz.")
    if k < 1:
        raise ValueError("k değeri 1 veya daha büyük olmalıdır.")

    unique_sorted = sorted(set(numbers))
    if k > len(unique_sorted):
        raise ValueError(
            f"k değeri benzersiz eleman sayısından büyük olamaz. "
            f"Benzersiz eleman sayısı: {len(unique_sorted)}"
        )

    return unique_sorted[k - 1]


def closest_pair_to_target(numbers: Sequence[int | float], target: int | float) -> tuple[int | float, int | float]:
    """Toplamı hedef sayıya en yakın olan sayı çiftini döndürür.

    İki işaretçili yöntem kullanılır. Bu nedenle önce liste sıralanır.
    Zaman karmaşıklığı: O(n log n)
    """
    if len(numbers) < 2:
        raise ValueError("En yakın çift için listede en az iki sayı olmalıdır.")

    sorted_numbers = sorted(numbers)
    left = 0
    right = len(sorted_numbers) - 1
    best_pair = (sorted_numbers[left], sorted_numbers[right])
    best_difference = math.inf

    while left < right:
        current_sum = sorted_numbers[left] + sorted_numbers[right]
        current_difference = abs(target - current_sum)

        if current_difference < best_difference:
            best_difference = current_difference
            best_pair = (sorted_numbers[left], sorted_numbers[right])

        if current_sum == target:
            return best_pair
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return best_pair


def repeated_elements(items: Sequence[object]) -> list[object]:
    """Listede birden fazla geçen elemanları ilk görülme sırasına göre döndürür."""
    counts = Counter(items)
    repeated: list[object] = []
    seen: set[object] = set()

    for item in items:
        if counts[item] > 1 and item not in seen:
            repeated.append(item)
            seen.add(item)

    return repeated


def validate_matrix(matrix: Sequence[Sequence[int | float]], name: str = "matris") -> None:
    """Matrisin boş olmayan, dikdörtgen yapıda olduğunu kontrol eder."""
    if not matrix:
        raise ValueError(f"{name} boş olamaz.")
    if not matrix[0]:
        raise ValueError(f"{name} satırları boş olamaz.")

    column_count = len(matrix[0])
    for row in matrix:
        if len(row) != column_count:
            raise ValueError(f"{name} dikdörtgen yapıda olmalıdır.")


def matrix_multiply(
    matrix_a: Sequence[Sequence[int | float]],
    matrix_b: Sequence[Sequence[int | float]],
) -> list[list[int | float]]:
    """İki matrisi çarpar.

    A matrisi m x n, B matrisi n x p boyutunda olmalıdır.
    Sonuç matrisi m x p boyutundadır.
    """
    validate_matrix(matrix_a, "Birinci matris")
    validate_matrix(matrix_b, "İkinci matris")

    a_columns = len(matrix_a[0])
    b_rows = len(matrix_b)
    if a_columns != b_rows:
        raise ValueError(
            "Matrisler çarpılamaz. Birinci matrisin sütun sayısı, "
            "ikinci matrisin satır sayısına eşit olmalıdır."
        )

    b_columns = len(matrix_b[0])
    result: list[list[int | float]] = []

    for i in range(len(matrix_a)):
        result_row: list[int | float] = []
        for j in range(b_columns):
            value = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(a_columns))
            result_row.append(value)
        result.append(result_row)

    return result


def word_frequency_from_text(text: str) -> dict[str, int]:
    """Metindeki kelimelerin frekansını döndürür.

    Büyük/küçük harf farkını kaldırır ve noktalama işaretlerini ayıklar.
    Türkçe karakterleri destekler.
    """
    words = _WORD_PATTERN.findall(text.casefold())
    return dict(Counter(words))


def word_frequency_from_file(file_path: str | Path) -> dict[str, int]:
    """Bir metin dosyasındaki kelime frekanslarını döndürür."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Dosya bulunamadı: {path}")
    if not path.is_file():
        raise ValueError(f"Verilen yol bir dosya değil: {path}")

    return word_frequency_from_text(path.read_text(encoding="utf-8"))


def min_value(numbers: Sequence[int | float]) -> int | float:
    """Listedeki en küçük değeri döndürür."""
    if not numbers:
        raise ValueError("Liste boş olamaz.")

    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest


def sqrt_newton(
    number: float,
    initial_guess: float | None = None,
    tolerance: float = 1e-10,
    max_iterations: int = 100,
) -> float:
    """Newton-Raphson yöntemiyle karekök hesaplar."""
    if number < 0:
        raise ValueError("Negatif sayıların gerçek karekökü hesaplanamaz.")
    if number == 0:
        return 0.0
    if tolerance <= 0:
        raise ValueError("Tolerans değeri pozitif olmalıdır.")
    if max_iterations <= 0:
        raise ValueError("Maksimum iterasyon sayısı pozitif olmalıdır.")

    x = initial_guess if initial_guess is not None else number / 2
    if x <= 0:
        raise ValueError("İlk tahmin değeri pozitif olmalıdır.")

    for _ in range(max_iterations):
        next_x = 0.5 * (x + number / x)
        if abs(next_x - x) < tolerance:
            return next_x
        x = next_x

    return x


def gcd(number_a: int, number_b: int) -> int:
    """Öklid algoritması ile iki sayının EBOB değerini döndürür."""
    a = abs(number_a)
    b = abs(number_b)

    while b != 0:
        a, b = b, a % b
    return a


def is_prime(number: int) -> bool:
    """Bir sayının asal olup olmadığını kontrol eder."""
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    limit = int(math.sqrt(number)) + 1
    for divisor in range(3, limit, 2):
        if number % divisor == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """n'inci Fibonacci sayısını iteratif olarak hesaplar.

    fib(0) = 0, fib(1) = 1 kabul edilir.
    """
    if n < 0:
        raise ValueError("Fibonacci için n negatif olamaz.")

    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


def parse_number_list(raw_value: str) -> list[float]:
    """Virgülle ayrılmış kullanıcı girişini sayı listesine çevirir."""
    if not raw_value.strip():
        raise ValueError("Liste girişi boş olamaz.")

    numbers: list[float] = []
    for part in raw_value.split(","):
        part = part.strip()
        if not part:
            continue
        numbers.append(float(part))

    if not numbers:
        raise ValueError("Geçerli sayı bulunamadı.")
    return numbers
