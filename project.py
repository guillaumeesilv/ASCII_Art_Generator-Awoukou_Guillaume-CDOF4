
from pyfiglet import Figlet
from colorama import init, Fore, Back, Style

def create_ascii_art():
    init(autoreset=True)

    text=input("enter the text you want to style : ")
   
        
    form = int(input("enter the number of the style you want to apply : 1-slant | 2-block | 3-caligraphy | 4-relief | 5-isometric1 | 6-acrobatic\n"))
    
    color_choice = input("Enter the text color (e.g., 'red', 'green', 'blue'): ")
        
    if form==1:
        form="slant"
        
    elif form==2:
        form="block"
            
    elif form==3:
        form="caligraphy"
            
    elif form==4:
        form="relief"
            
    elif form==5:
        form="isometric1"
    elif form==6:
        form="acrobatic"
        
    custom_fig = Figlet(font=form)  # You can choose different fonts, e.g., 'slant', 'block', 'caligraphy', etc.
    ascii_art = custom_fig.renderText(text)
    
    color_codes = {
        'black': Fore.BLACK,
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE
    }
    
    if color_choice in color_codes:
        colored_text = color_codes[color_choice] + ascii_art
        print(colored_text)
    else:
        print("Invalid color choice. Displaying in default color.")
        print(ascii_art)

# Example usage
create_ascii_art()
input()