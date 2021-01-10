import pyfiglet 
fonts = pyfiglet.FigletFont.getFonts()
print(fonts)
for font in fonts:
    
    print(pyfiglet.figlet_format("\n Nick ",font=f'{font}'))