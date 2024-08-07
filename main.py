from string import ascii_lowercase, ascii_uppercase


def main():
    current_action = None
    current_shift = None
    while True:
        if current_action is None:
            print('Please choose an action:',
                  '1. Encrypt',
                  '2. Decrypt\n',
                  sep='\n')
            
            choice = input('Enter your choice (or type "exit" to quit): ').strip().lower()
            if choice == 'exit':
                break
            
            action = actions.get(choice)
            if action:
                current_action = action
            else:
                print('Invalid choice. Please try again.')
                continue

        if current_shift is None:
            shift = input('Enter the shift amount (an integer): ')
            if shift.isdigit():
                current_shift = int(shift)
            else:
                print('Invalid input for shift amount. Please enter a valid integer.')
                continue
        
        text = input('Enter the text you want to process: ')
        if not text:
            print('Invalid input. Please enter valid text to process')
            continue

        result = current_action(text, current_shift)
        print(f'\nThe result is: {result}\n')

        copy_responce = input('Do you want to copy this text to the clipboard? (pyperclip required; type "yes" or "no"): ')
        if copy_responce == 'yes':
            try:
                from pyperclip import copy
                copy(result)
                print('The text has been copied to the clipboard.')
            except ImportError:
                print('Pyperclip is not installed. Clipboard functionality is unavailable.')

        again = input('Do you want to repeat the same action? (yes/no): ').strip().lower()
        if again == 'no':
            current_action = None
            reset = input('Do you want to choose another action? (yes/no): ').strip().lower()
            if reset == 'yes':
                current_action = None
            else:
                break

        again_shift = input('Do you want to use the same shift amount? (yes/no): ').strip().lower()
        if again_shift == 'no':
            current_shift = None

        print()


def encrypt(text:str, shift:int):
    encrypted_text = ''
    for symbol in text:
        if symbol.isalpha():
            if symbol.islower():
                encrypted_text += ascii_lowercase[ascii_lowercase.index(symbol) + shift]
            else:
                encrypted_text += ascii_uppercase[ascii_uppercase.index(symbol) + shift]
        else:
            encrypted_text += symbol

    return encrypted_text


def decrypt(text:str, shift:int):
    decrypted_text = ''
    for symbol in text:
        if symbol.isalpha():
            if symbol.islower():
                decrypted_text += ascii_lowercase[ascii_lowercase.index(symbol) - shift]
            else:
                decrypted_text += ascii_uppercase[ascii_uppercase.index(symbol) - shift]
        else:
            encrypted_text += symbol

    return decrypted_text


actions = {
    '1': encrypt,
    '2': decrypt
}


if __name__ == '__main__':
    main()