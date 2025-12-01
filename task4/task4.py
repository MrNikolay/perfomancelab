import sys

def main(numbers):
    m = numbers[len(numbers) // 2]
    total_moves = sum(abs(n - m) for n in numbers)

    if total_moves > 20:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
    else:
        print(total_moves)


if __name__ == "__main__":
    assert len(sys.argv) >= 2, "Программа ожидает один обязательный аргумент!"

    with open(sys.argv[1], 'r') as file:
        numbers = sorted(map(int, file.readlines()))
    
    main(numbers)