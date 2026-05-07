import os

def main():
    # Зчитуємо системну змінну (OLIINYK_VAR)
    env_value = os.getenv("OLIINYK_VAR")
    
    if env_value:
        print(f"Зчитане значення системної змінної OLIINYK_VAR: {env_value}")
    else:
        print("Повідомлення: Системна змінна OLIINYK_VAR відсутня або не задана!")

if __name__ == "__main__":
    main()