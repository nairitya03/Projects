import pyfiglet 

def print_text():

    text = input ("\nEnter text to Convert to Figlet >>> ")
    
                  
    while True:

        font = input ("\nEnter Font to use for Figlet or See help for all the available Fonts >>> ")

        if font == 'help' or font == 'Help' or font == 'HELP' :

            fonts = list(pyfiglet.FigletFont.getFonts())

            index=1

            for _ in fonts:
                print(f"{index} > {_}")
                index+=1
            
        else:

            print( pyfiglet.figlet_format(f"{text}", font) )
            break

if __name__=='__main__':

    print(pyfiglet.figlet_format("Fancy Text", font = "bulbhead" ).center(30))
    print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
    print("-"*70,"\n")

    print_text()
