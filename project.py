

def create_ascii_art():
    text=input("enter the text you want to style : ")
    
   
        
    form = int(input("enter the number of the style you want to apply : 1-slant | 2-block | 3-caligraphy | 4-relief | 5-isometric1\n"))
        
        
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

        
        
        
    custom_fig = Figlet(font=form)  # You can choose different fonts, e.g., 'slant', 'block', 'caligraphy', etc.
    ascii_art = custom_fig.renderText(text)
    print(ascii_art)

# Example usage
create_ascii_art()
