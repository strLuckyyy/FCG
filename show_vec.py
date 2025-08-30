import os
from Math.vector import Vec2, Vec3, Vec4
from typing import Any, Union

def show_vector(vector: Union[Vec2, Vec3, Vec4]) -> None:  
    ''' Code made by myself, with some help from ChatGPT 5 mini to format the output '''
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('Vector', len(vector), ':', vector)
    print(f'Magnitude: {vector.magnitude():.3f}')
    print('Normalized:', vector.normalize())
    print('Length:', len(vector))

    other: Any = Vec2.from_values(3, 4) if len(vector) == 2 else Vec3.from_values(3, 4, 5) if len(vector) == 3 else Vec4.from_values(3, 4, 5, 6)
    print('\nAddition:', vector, '+', other)
    print('\t', vector + other)

    sub: Any = Vec2.from_values(1, 1) if len(vector) == 2 else Vec3.from_values(1, 1, 1) if len(vector) == 3 else Vec4.from_values(1, 1, 1, 1)
    print('\nSubtraction:', vector, '-', sub)
    print('\t', vector - sub)

    print('\nMultiplication:', vector, '* 2')
    print('\t', vector * 2)

    print('\nDivision:', vector, '/ 2')
    print('\t', vector / 2)

    sp: Any = Vec2.from_values(3, 4) if len(vector) == 2 else Vec3.from_values(3, 4, 5) if len(vector) == 3 else Vec4.from_values(3, 4, 5, 6)
    print('\nScalar Product:', vector, sp)
    print(f'\t {vector.scalar_product(sp):.3f}')

    print('\nCopy:', vector, 'copied')
    new_vec: Union[Vec2, Vec3, Vec4] = vector.copy()
    print('\t', vector, '==', new_vec)

    print('\nTo Float:', vector, 'to float')
    print('\t', [f"{v:.3f}" for v in vector.to_float()]) 
    
    print('\nContinue? (y/n)')
    input()



def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        vector2 = Vec2.from_values(1, 2)
        vector3 = Vec3.from_values(1, 2, 3)
        vector4 = Vec4.from_values(1, 2, 3, 4)
    
        print('Vector Operations')
        print('------------------')
        print('\n', vector2)    
        print('\n', vector3)    
        print('\n', vector4)
        
        print('\n Which vector do you want to see?')
        print('\n1: EXIT\n2: Vec2\n3: Vec3\n4: Vec4')
        choice = input('Enter your choice (1/2/3/4): ')
        
        if choice == '1':
            print('Exiting...')
            break
        elif choice == '2':
            show_vector(vector2)
        elif choice == '3':
            show_vector(vector3)
        elif choice == '4':
            show_vector(vector4)
        else:
            print('Invalid choice. Please enter 1, 2, 3 or 4.')


if __name__ == "__main__":
    main()