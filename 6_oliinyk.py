def main():
    # Жорстко заданий масив із 13 елементів (відповідно до прикладу)
    arr = [1, 3, 5, 9, 11, 0, 12, 1, 12, 21, 22, 16, 17]
    n = len(arr)
    
    # Виводимо початковий масив із зірочкою біля першого елемента
    print(f"Масив {n} елементів:")
    print_arr = [f"*{arr[0]}"] + [str(x) for x in arr[1:]]
    print(" ".join(print_arr))
    
    try:
        k = int(input("Введіть ціле число k: "))
        if k <= 0:
            print("Помилка: k має бути більше 0")
            return
    except ValueError:
        print("Помилка: потрібно ввести ціле число.")
        return

    # Якщо k > 13, беремо по модулю 13
    shift = k % n
    print(f"Зсув вправо на {shift} елементи")
    
    # Здійснюємо циклічний зсув вправо
    if shift > 0:
        shifted_arr = arr[-shift:] + arr[:-shift]
    else:
        shifted_arr = arr[:]
        
    # Формуємо вивід для зсунутого масиву. 
    # Оригінальний перший елемент (який треба виділити *) тепер на індексі `shift`
    shifted_print = []
    for i in range(n):
        if i == shift:
            shifted_print.append(f"*{shifted_arr[i]}")
        else:
            shifted_print.append(str(shifted_arr[i]))
            
    print(" ".join(shifted_print))

if __name__ == "__main__":
    main()