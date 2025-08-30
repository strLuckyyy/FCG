import os
from Math.vector import Vec2, Vec3, Vec4
from Math.matrix import Mat2, Mat3, Mat4
from typing import Any, Union, cast

def show_matrix(matrix: Union[Mat2, Mat3, Mat4]) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f'Matrix {len(matrix)}: {matrix}')

    print(f'\nAddition:\n{matrix} + {matrix}')
    print(f'R:\n{matrix + cast(Any, matrix)}')

    print(f'\nSubtraction:\n{matrix} - {matrix}')
    print(f'R:\n{matrix - cast(Any, matrix)}')

    print(f'\nMultiplication:\n{matrix} * 2')
    print(f'R:\n{cast(Any, matrix) * 2}')

    print(f'\nDivision:\n{matrix} / 2')
    print(f'R:\n{cast(Any, matrix) / 2}')

    vec_other: Union[Vec2, Vec3, Vec4] = (
        Vec2.from_values(1, 2) if len(matrix) == 2
        else Vec3.from_values(1, 2, 3) if len(matrix) == 3
        else Vec4.from_values(1, 2, 3, 4)
    )
    print(f'\nMultiplication by vector:\n{matrix} * {vec_other}')
    print(f'R:\n{cast(Any, matrix).multiply_vec2(cast(Vec2, vec_other)) if len(matrix) == 2 else cast(Any, matrix).multiply_vec3(cast(Vec3, vec_other)) if len(matrix) == 3 else cast(Any, matrix).multiply_vec4(cast(Vec4, vec_other))}')

    print(f'\nMultiplication by itself:\n{matrix} * {matrix}')
    print(f'R:\n{cast(Any, matrix).multiply_mat2(cast(Any, matrix)) if len(matrix) == 2 else cast(Any, matrix).multiply_mat3(cast(Any, matrix)) if len(matrix) == 3 else cast(Any, matrix).multiply_mat4(cast(Any, matrix))}')

    print(f'\nTranspose:\n{matrix}')
    print(f'R: {matrix.transpose()}')

    print(f'\nCopy:\n{matrix} copied')
    new_mat: Union[Mat2, Mat3, Mat4] = cast(Any, matrix).copy()
    print(f'R:\n{new_mat}\n==\n{matrix}')

    print(f'\nTo Float:\n{matrix} to float')
    matrix_list: list[list[float]] = cast(Any, matrix).matrix_float()
    
    print('R:')
    for i in matrix_list:
        print(i)
    
    print('\nContinue? (y/n)')
    input()
    
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        matrix2 = Mat2.from_list(Vec2.from_values(1, 2), Vec2.from_values(3, 4))
        matrix3 = Mat3.from_list(Vec3.from_values(1, 2, 3), Vec3.from_values(4, 5, 6), Vec3.from_values(7, 8, 9))
        matrix4 = Mat4.from_list(Vec4.from_values(1, 2, 3, 4), Vec4.from_values(5, 6, 7, 8), Vec4.from_values(9, 10, 11, 12), Vec4.from_values(13, 14, 15, 16))
    
        print('Matrix Operations')
        print('------------------')
        print('\n', matrix2)    
        print('\n', matrix3)    
        print('\n', matrix4)
        
        print('\n Which matrix do you want to see?')
        print('\n1: EXIT\n2: Mat2\n3: Mat3\n4: Mat4')
        
        choice = input('Enter your choice: ')
        
        if choice == '1':
            print('Exiting...')
            break
        elif choice == '2':
            show_matrix(matrix2)
        elif choice == '3':
            show_matrix(matrix3)
        elif choice == '4':
            show_matrix(matrix4)
        else:
            print('Invalid choice. Please try again.')
            input('Press Enter to continue...')

if __name__ == "__main__":
    main()