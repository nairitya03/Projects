#Fancy ASCII text ...
import pyfiglet

print(pyfiglet.figlet_format("Zipper ", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*70,"\n")

# importing required modules 
import tarfile
from tqdm import tqdm
import time
# define a compressing function

def compress( tar_file , members ):
    
    #open file for zip compressed writting
    tar = tarfile.open(tar_file , mode="x")
    
    ## create a progress bar 
    progress =tqdm(members)
    for members in progress:
        
        #add file to compress
        tar.add(members)
        #progress description
        progress.set_description(f"Compressing {members}")
    
    print("-> Compression Succefull... ")
    time.sleep(10)
    #close file
    tar.close()


#define a deccompressing funtion
def decompress( tar_file , path , members = None ):
    tar=tarfile.open( tar_file , mode="r" )
    
    if members is None:
        members = tar.getmembers()
    
     ## create a progress bar 
    progress = tqdm (members)
    for members in progress:
        
        #add file to compress
        tar.extract( members ,path= path )
         #progress description
        progress.set_description(f"Extracting {members.name}")
    
   
    print("-> Extraction Succefull... ")
    time.sleep(10)
       
   #close file
    tar.close()
    

#enter the files to compress
def files():
    files_list = list(map(str,input("Enter the files to compress (Sepreated by ',') >>> ").strip().split(',')))
    return files_list

#enter location for Decommpressing
def path():
    
    path = input("Enter Path to Extract files >>>")
    return path
    
    
    
#Switch funtion for Compression and Decompression

def zipper(i):
    if i==1:
        compress(name , files())
        
    
    elif i==2:
        decompress(name, path())

    else:
        print("Invalid Selection !! " )
        time.sleep(8)


num=0
while num != '1' or num != '2':
    num = input ("Enter your Choice !"
              "\n 1: Archive"
              "\n 2: Extract"
              "\n >>>"
              )
    if num.isnumeric():
        if int(num) == 1 or int(num) == 2:
            break

        else :
            print("\nInvalid Selection !! \n" )

    else:
        print("\nInvalid Selection !! \n")
    
# give name to compressed file
name = str(input("Give file name for Compression/Extraction ( Without Extension !! )\n>>>")+'.rar')

#call switch funti0n
zipper(int(num))



