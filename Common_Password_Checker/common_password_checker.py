
def check_password(password: str):
    with open("passwords.txt", "r") as file:
        common_passwords: list[str] = file.read().splitlines()
    
    for i in common_passwords in enumerate(common_passwords, start=1):
        if password == common_passwords:
            print(f"{password}: 😬 (#{i})")
            return
    
    print(f"{password}: ✔ (Unique)")


def main():
    user_password: str = input(" Enter a password: ")
    check_password(user_password)


if __name__ == "__main__":
    main()


