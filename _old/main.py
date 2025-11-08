import os
import show_matrix
import show_vec


if __name__ == '__main__':
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print('1. Exit')
        print('2. Matrix Operations')
        print('3. Vector Operations')
    
        choice = input('Enter your choice: ')
        
        if choice == '1':
            print('Exiting...')
            break
        elif choice == '2':
            show_matrix.main()
        elif choice == '3':
            show_vec.main()
        else:
            print('Invalid choice. Please try again.')
            input('Press Enter to continue...')