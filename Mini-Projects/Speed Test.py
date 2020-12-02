
import speedtest
    
    
def test():
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        return res["download"], res["upload"], res["ping"]
    
def main():
        
        # pretty write to txt file
        with open('Speed Test.txt', 'w') as f:
            for i in range(3):
                print('Making test #{}'.format(i+1))
                d, u, p = test()
                f.write('Test #{}\n'.format(i+1))
                f.write('Download: {:.2f} Mb/s\n'.format(d / 1024))
                f.write('Upload: {:.2f} Mb/s\n'.format(u / 1024))
                f.write('Ping: {}\n'.format(p))
        
    
if __name__ == '__main__':
        main()

