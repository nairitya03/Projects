#import libraries...
import speedtest
import time   

#fancy ASCII text...
import pyfiglet

print(pyfiglet.figlet_format("Speed Test", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*70,"\n")

#funtion to perform test...
def test():
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        return res["download"], res["upload"], res["ping"]
    
#funtion to call test and save to file...
def main():
        
#pretty write to txt file...
        with open('Speed Test.txt', 'w') as f:
            for i in range(3):
                print('Making test #{}'.format(i+1))
                d, u, p = test()
                f.write('Test #{}\n'.format(i+1))
                f.write('Download: {:.2f} MB/s\n'.format(d/(1024*1024*8)))
                f.write('Upload: {:.2f} MB/s\n'.format(u/(1024*1024*8)))
                f.write('Ping: {}\n'.format(p))
                f.write('')
#pretty Read from txt file...
        print('')
        with open ('Speed Test.txt', 'r') as f:
                for i in f:
                        print(i)
        time.sleep(8)

# Constrctor Call...       
if __name__ == '__main__':
        main()

