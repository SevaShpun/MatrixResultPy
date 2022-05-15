import colorama
from os import system
from colorama import Fore, Back, Style
colorama.init()

def display(txt:str='test', col:str='green'):
    color_list = {
        'LBLACK': Fore.LIGHTBLACK_EX,
        'LBLUE': Fore.LIGHTBLUE_EX,
        'LCYAN': Fore.LIGHTCYAN_EX,
        'LGREEN': Fore.LIGHTGREEN_EX,
        'LMAGENTA': Fore.LIGHTMAGENTA_EX,
        'LRED': Fore.LIGHTRED_EX,
        'LWHITE': Fore.LIGHTWHITE_EX,
        'LYELLOW': Fore.LIGHTYELLOW_EX,
        'BLUE': Fore.BLUE,
        'CYAN': Fore.CYAN,
        'GREEN': Fore.GREEN,
        'MAGENTA': Fore.MAGENTA,
        'RED': Fore.RED,
        'WHITE': Fore.WHITE,
        'RESET': Fore.RESET,
        'YELLOW': Fore.YELLOW
    }

    color = color_list.get(col.upper(), color_list['GREEN'])
    print(f'{color}{txt}{Style.RESET_ALL}')

cell = {}
r = 0
i = 0

def template_text():
    display("\t\t\t\t=================", "yellow")
    display("\t\t\t\t   Template 3x3", "yellow")
    display("\t\t\t\t=================", "yellow")
    display("\t\t\t\t    1 | 2 | 3", "yellow")
    display("\t\t\t\t    4 | 5 | 6", "yellow")
    display("\t\t\t\t    7 | 8 | 9", "yellow")
    display("\t\t\t\t=================", "yellow")

def matrix_filling_text():
    display("\t\t\t\tFill in the cells", "green")
    display("\t\t\t\t=================", "green")
    display(f"\t\t\t\t{cell.get(0, 0)}\t{cell.get(1, 0)}\t{cell.get(2, 0)}", "magenta")
    display(f"\t\t\t\t{cell.get(3, 0)}\t{cell.get(4, 0)}\t{cell.get(5, 0)}", "magenta")
    display(f"\t\t\t\t{cell.get(6, 0)}\t{cell.get(7, 0)}\t{cell.get(8, 0)}", "magenta")
    display("\t\t\t\t=================", "green")
    display("", "green")


if __name__ == "__main__":
    try:
        system("title Solving a Matrix by a Simple Method (Python 3)")
        while (i < 9):
            template_text();
            matrix_filling_text();
            
            input_text = input(f"cell {i+1}> ")
            try:
                system("cls")
                cell[i] = int(input_text)
                i += 1
            except:
                pass

        template_text()
        matrix_filling_text()

        r = cell[0] * (cell[4] * cell[8] - cell[5] * cell[7]) - cell[1] * (cell[3] * cell[8] - cell[5] * cell[6]) + cell[2] * (cell[3] * cell[7] - cell[4] * cell[6]);

        if r < 0:
            display(f"\t\t\t\tResult: {r}", "red")
        else:
            display(f"\t\t\t\tResult: {r}", "white")
        
        input("Press any key")
    except (KeyboardInterrupt, SystemExit):
        pass
