# _*_ utf-8 _*_
# @uthor : Aman Raj
# Filename : local (predictor.py)
# File Modified : 09/01/2023

import sys
import subprocess
import importlib
import platform
import time
import urllib.request as request


class Installer:
    def OS(self):
        if str(platform.system()).lower() == 'linux':
            return 'linux'
        elif str(platform.system()).lower() == 'windows':
            return 'windows'
        else:
            return 'other'

    def internet(self):
        try:
            request.urlopen("https://google.com/")
            return True
        except Exception:
            return False

    def package_checker(self, pkg:str, OS:str):
        if self.internet() != True:
            sys.stdout.write("Internet Connection Failed\n")
        else:
            if str(OS).lower() == 'linux':
                if str(subprocess.getoutput("whoami")).lower() != 'root':
                    sys.stdout.write("\033[1;33m**WARNING** You need to Root\n")
                else:
                    if bool(subprocess.getstatusoutput(str(pkg))[0]) != False:
                        sys.stdout.write(f"\033[1;37m[ \033[0;31mNot Found\033[1;37m ] {str(pkg)}\n")
                        subprocess.getoutput(f'xterm -T "Installing" -geometry 100x30 -e "sudo apt install -y {str(pkg)}"')
                        sys.stdout.write(f"\033[1;37m[ \033[1;32mInstalled\033[1;37m ] {str(pkg)}\n")
                    else:
                        sys.stdout.write(f"\033[1;37m[ \033[1;32mFound\033[1;37m ] {str(pkg)}\n")

            elif str(OS) == 'windows':
                if bool(subprocess.getstatusoutput(str(pkg))[0]) != False:
                    sys.stdout.write(f"\033[1;37m[ \033[0;31mNot Found\033[1;37m ] {str(pkg)}\n")
                    sys.stdout.write(f"\033[1;37m[ \033[1;33mNot Found\033[1;37m ] You Need To install this {str(pkg)}\n")
                else:
                    sys.stdout.write(f"\033[1;37m[ \033[1;32mFound\033[1;37m ] {str(pkg)}\n")
            else:
                sys.stdout.write("\033[1;31mOperating System Not Support !!\033[0m")

    def check_module(self, module:str):
        try:
            _ = importlib.import_module(str(module))
            return True
        except Exception and ModuleNotFoundError:
            return False

    def module(self, module:str, OS:str):
        if self.internet() != True:
            sys.stdout.write("Internet Connection Failed\n")
        else:
            if str(OS).lower() == 'linux':
                if self.check_module(module):
                    sys.stdout.write(f"\033[1;37m[\033[0;32m Module Found\033[1;37m ] {module}\n")
                else:
                    sys.stdout.write(f"\033[1;37m[\033[0;31m Module Not Found\033[1;37m ] {module}\n")
                    subprocess.getoutput(f'xterm -T "Installing" -geometry 100x30 -e "pip3 install {str(module)}"')
                    sys.stdout.write(f"\033[1;37m[\033[1;32m Module Installed\033[1;37m ] {module}\n")
            elif str(OS).lower() == 'windows':
                if self.check_module(module):
                    sys.stdout.write(f"\033[1;37m[\033[0;32m Module Found\033[1;37m ] {module}\n")
                else:
                    sys.stdout.write(f"\033[1;37m[\033[0;31m Module Not Found\033[1;37m ] {module}\n")
                    subprocess.getoutput(f'pip install {str(module)}')
                    sys.stdout.write(f"\033[1;37m[\033[1;32m Module Installed\033[1;37m ] {module}\n")
            else:
                sys.stdout.write("\033[1;31mOperating System Not Support !!\033[0m")

    def setup(self):
        OS = self.OS()
        sys.stdout.write("\t\033[1;34m[ Version : 0.1 ]\033[0m\n")
        sys.stdout.write("\t\033[1;33m[ Author : Aman Raj ]\033[0m\n\n")
        pkg = ['python3', 'python3-pip', 'gcc']
        if OS == 'linux':
            subprocess.getoutput('sudo apt install figlet -y')
            subprocess.getoutput('sudo apt install xterm -y')
            subprocess.call('clear', shell=True)
            sys.stdout.write("\033[1;31m")
            subprocess.getoutput('figlet Predictor')
            for i in pkg:
                self.package_checker(pkg=str(i), OS=OS)

        module = ['joblib', 'opencv-python', 'numpy',
                    'PyQt6', 'beautifulsoup4', 'requests',
                    'tensorflow']


        for j in module:
            self.module(module=str(j), OS=OS)

        sys.stdout.write(f"\033[1;33mInstallation Has been Completed since \033[1;34m{time.asctime()}\033[0m\n")

if __name__ == '__main__':
    selfs = Installer()
    selfs.setup()
