def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result

def main():
    print("=== Caesar Cipher Tool ===")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (0-25): "))
        if not 0 <= shift <= 25:
            raise ValueError
    except ValueError:
        print("Invalid shift value. Please enter a number between 0 and 25.")
        return

    result = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode}ed): {result}")

if __name__ == "__main__":
    main()
