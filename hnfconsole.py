import argparse
import json
import os
import random
import sys
import threading
import time

import requests
from flask import Flask, request, jsonify, app
from termcolor import colored as ctc

global webclientcode
parser = argparse.ArgumentParser(description="HyperNetwork Framework HELP"); parser.add_argument("--no-dns-server-proxy", help="Will using DNS Server Proxy for website?", default="true"); parser.add_argument("--no-name-checker", help="Check the filename?", default="true")
kwarg = parser.parse_args()

class FlASK_SERVICE:
    # Proxy of hypernetworkframework.carbondoxdfuckedwerewolfwolfyxd.su
    class repeatnsLookup:
        global thread;

    def run(self):
        if kwarg.no_dns_server_proxy == "false" or kwarg.no_dns_server_proxy == "0":
            if (sys.platform == "linux") or ("linux2" == sys.platform):
                hosts_file = open("/etc/hosts", "a+")
                hosts_file.write("\n127.0.0.1 hypernetworkframework.carbondoxdfuckedwerewolfwolfyxd.su\n")
                hosts_file.flush()
                hosts_file.close()
            elif (sys.platform == "win32"):
                hosts_file = open("C:\Windows\System32\drivers\etc\hosts", "a+")
                hosts_file.write("\n127.0.0.1 hypernetworkframework.carbondoxdfuckedwerewolfwolfyxd.su\n")
                hosts_file.flush()
                hosts_file.close()

        urlport = 80
        webclientcode = random.randint(100000, 99999999)
        print(ctc("Your AuthCode ", "grey", "on_red", ["underline", "blink"])+": "+ctc(webclientcode.__str__(), "grey", "on_green", ["underline", "blink"]))
        print("http://hypernetworkframework.carbondoxdfuckedwerewolfwolfyxd.su/")
        app = Flask("HNF")

        @app.route("/post/cwgauth/auth2.0/oauth/", methods=["GET", "POST"])
        def getauthhere():
            data = request.get_data()
            urlstrip = request.url.replace("http://", "").replace("https://", "").split("/")
            substrip = urlstrip[5].split("&")
            authid = substrip[0].replace("?", "")
            if authid.__str__() == webclientcode.__str__():
                return '<script>window.location.replace("../../../../../../../../../../../fuckyourassholeaw");</script>'
            else:
                return '<!DOCTYPE html><html><head><meta charset="utf-8"><title></title></head><body><h6><font color="red">ERROR: Your codes was mistaken and it will make you retry at: </font></h6><h2><font color="red"><p id="counter"></p></font></h2><script type="text/javascript">let fun = () => document.getElementById("counter").innerHTML = "<a>"+i+"s</a>";let sleep2= (time)=> new Promise((resolve)=>{setTimeout(resolve,time)})async function wait(time){await sleep2(time);}var i=10000;while (i > 0){	wait(1000);fun();i = i - 1;}if (i == 0) {window.location.replace("../../../../../../../../../../");}</script></body></html>'
            return '<!DOCTYPE html><html><head><meta charset="utf-8"><title></title></head><body><h6><font color="red">ERROR: Your codes was mistaken and it will make you retry at: </font></h6><h2><font color="red"><p id="counter"></p></font></h2><script type="text/javascript">let fun = () => document.getElementById("counter").innerHTML = "<a>"+i+"s</a>";let sleep2= (time)=> new Promise((resolve)=>{setTimeout(resolve,time)})async function wait(time){await sleep2(time);}var i=10000;while (i > 0){	wait(1000);fun();i = i - 1;}if (i == 0) {window.location.replace("../../../../../../../../../../");}</script></body></html>'

        @app.route("/", methods=["GET", "POST"])
        def getIndex():
            return '<!DOCTYPE html><html><head><meta charset="utf-8" /><title></title><script>var h = "CLIENT-RPT-ID";var idc = prompt(h+":");if (idc != null) {window.location.replace("./post/cwgauth/auth2.0/oauth/?"+idc)} else {alert(h+" IS VAILD.")}</script></head><body></body></html>'

        @app.route("/fuckyourassholeaw/", methods=["GET", "POST"])
        def getfyas():
            return 'back<script>window.location.replace("hnfnp://"+'+webclientcode.__str__()+');</script>'

        @app.route("/doc/", methods=["GET", "POST"])
        def getDocumentRoute():
            return "No Document Now, We're Sorry. QWQ"
        app.run(host="127.0.0.1", port=urlport)

class NO:
    NOTIFICATION_QUESTION = ctc("[?]", "grey")
    NOTIFICATION_WARN = ctc("[!]", "red")
    NOTIFICATION_YES = ctc("[✓]", "green")
    NOTIFICATION_NO = ctc("[×]", "red")
    NOTIFICATION_ADD = ctc("[+]", "green")
    NOTIFICATION_CON = ctc("[-]", "red")


class INSIDER_TOOLS:
    class SQL_INJECTOR:
        def SQL_INJECTOR(self, URL, PORT, MESSAGEHERE):
            url = URL.__str__()
            port = PORT.__str__()
            message = MESSAGEHERE.__str__()
            requests.Response(url, port, message)


class NE:
    def register(Key, Something):
        print


def _hnf_header_usemodule(setting, a):
    global _hnf_header_usemodule_a
    if setting == "set":
        _hnf_header_usemodule_a = a
    return _hnf_header_usemodule_a


def getbackheader(_a, _b):
    gbh_rtr = ""
    if _a: gbh_rtr = _b
    if not _a: return gbh_rtr


def init():
    if kwarg.no_name_checker== "false" and os.path.basename(__file__) != "hnfconsole.py": (ctc("You Are Running in WARN-NAME-STATUS, Reject Start.", "grey", "on_red", ["underline", "blink"])); exit("Do not use other name to run this script if you turned that mode!")
    global _hnf_path, _hnf_firstload, _hnf_exploitsfile, _hnf_auxiliaryfile, hnf_exploits_json, _hnf_initanimate, _hnf_commandlists, _hnf_everydaytips_one, _hnf_commandlist_json, _hnf_commandlist, _hnf_header_usemodule, _cmdtemp_use_in, _hnf_data_defaultBrowser, _hnf_data_DB
    _cmdtemp_use_in = ""
    _hnf_path = "_hnf"
    _hnf_firstload = "fl.status"
    _hnf_exploitsfile = "exploits.rc"
    _hnf_auxiliaryfile = "auxiliary.rc"
    _hnf_initanimate = "init_animate.an"
    _hnf_commandlist = "cmdlist.json"
    _hnf_header_usemodule = ""
    _hnf_header_usemodule_a = ""
    cmd_in_header = ""
    _hnf_data_defaultBrowser = """os.system(r"{browser} {url}")"""
    _hnf_data_DB = ""
    _hnf_initanimate_json = '{"animate": ["[*] Starting the Hypernetwork Framework Console.../","[*] StArting the Hypernetwork Framework Console...-","[*] StaRting the Hypernetwork Framework Console...\\\\","[*] StarTing the Hypernetwork Framework Console...|","[*] StartIng the Hypernetwork Framework Console.../","[*] StartiNg the Hypernetwork Framework Console...-","[*] StartinG the Hypernetwork Framework Console...\\\\","[*] Starting the Hypernetwork Framework Console...|","[*] Starting The Hypernetwork Framework Console.../","[*] Starting tHe Hypernetwork Framework Console...-","[*] Starting thE Hypernetwork Framework Console...\\\\","[*] Starting the Hypernetwork Framework Console...|","[*] Starting the HYpernetwork Framework Console.../","[*] Starting the HyPernetwork Framework Console...-","[*] Starting the HypErnetwork Framework Console...\\\\","[*] Starting the HypeRnetwork Framework Console...|","[*] Starting the HyperNetwork Framework Console.../","[*] Starting the HypernEtwork Framework Console...-","[*] Starting the HyperneTwork Framework Console...\\\\","[*] Starting the HypernetWork Framework Console...|","[*] Starting the HypernetwOrk Framework Console.../","[*] Starting the HypernetwoRk Framework Console...-","[*] Starting the HypernetworK Framework Console...\\\\","[*] Starting the Hypernetwork Framework Console...|","[*] Starting the Hypernetwork FRamework Console.../","[*] Starting the Hypernetwork FrAmework Console...-","[*] Starting the Hypernetwork FraMework Console...\\\\","[*] Starting the Hypernetwork FramEwork Console...|","[*] Starting the Hypernetwork FrameWork Console.../","[*] Starting the Hypernetwork FramewOrk Console...-","[*] Starting the Hypernetwork FramewoRk Console...\\\\","[*] Starting the Hypernetwork FrameworK Console...|","[*] Starting the Hypernetwork Framework Console.../","[*] Starting the Hypernetwork Framework Console...-","[*] Starting the Hypernetwork Framework COnsole...\\\\","[*] Starting the Hypernetwork Framework CoNsole...|","[*] Starting the Hypernetwork Framework ConSole.../","[*] Starting the Hypernetwork Framework ConsOle...-","[*] Starting the Hypernetwork Framework ConsoLe...\\\\","[*] Starting the Hypernetwork Framework ConsolE...|", "   "]}'
    _hnf_everydaytips = [
        "No Tips",
        "Writing a custom module? After editing your\nmodule, why not try the reload command\nHypernetwork Framework Documentation:\nhttp://hypernetworkframework.carbondoxdfuckedwerewolfwolfyxd.su/doc",
        ":(",
        "Fuck you CarbondoXD!"
    ]
    _hnf_commandlists = """{"help": {"cmd": "print('HELP:')", "single": 1},
                            "exit": {"cmd": "print('Exiting '+ctc('HyperNetwork Framework', 'red'));exit(0)", "single": 1},
                            "echo": {"cmd": ["print(cmd_in_array[0][1])"], "single": 0},
                            "search": {"cmd": ["_cmdtemp_search_in = input('> ')", "if _cmdtemp_search_in=='hnf_exploits': print(hnf_exploits_json)", "if _cmdtemp_search_in=='hnf_auxiliary': print(hnf_auxiliary_json)", "if _cmdtemp_search_in=='hnf_command': print(hnf_commandlist_json)"], "single":  0},
                            "use": {"cmd": ["global _cmdtemp_use_in","_cmdtemp_use_in = input('USE MODULE > ')", "_hnf_header_usemodule = _cmdtemp_use_in", "getbackheader(True, _cmdtemp_use_in)"], "single": 0},
                            "execute": {"cmd": "exec(input('> '))" , "single": 1},
                            "del_res": {"cmd": ["os.system('cd /d '+os.getcwd())", "os.system('cd '+os.getcwd())", "os.system('del /s/q _hnf", "os.system('rm -rf _hnf')", "os.system('python3 hnfconsole.py')"], "single": 0},
                            "script_py": {"cmd": ["import os", "_cmdtemp_scriptpy_in = input('> ')", "os.system(r'python3 '+_cmdtemp_scriptpy_in)"], "single": 0},
                            "exploit ddos": {"cmd": ["_cmdtemp_exploit_in_maxconn = input('MAXCONN > ')", "_cmdtemp_exploit_in_port = input('PORT > ')", "_cmdtemp_exploit_in_host = input('HOST > ')", "_cmdtemp_exploit_in_page = input('PAGE > ')", "_cmdtemp_exploit_in_packsize = input('PACKSIZE > ')", "_cmdtemp_exploit_in_cookie = input('COOKIE > ')", "_cmdtemp_exploit_in_thread = input('THREAD > ')", "INSIDER_TOOLS.DDOS(_cmdtemp_exploit_in_maxconn, _cmdtemp_exploit_in_port, _cmdtemp_exploit_in_host, _cmdtemp_exploit_in_page, _cmdtemp_exploit_in_packsize, _cmdtemp_exploit_in_cookie, _cmdtemp_exploit_in_thread)"], "single": 0},
                            "u": {"cmd": ["cmd_in_header = cmd_in_array[0][1]", "print(cmd_in_header+'  |  '+cmd_in_array[0][1])"], "single": 0},
                            "whatusing": {"cmd": "print(cmd_in_header)", "single": 1},
                            "webclient": {"cmd": ["if cmd_in_array[0][1]=='set': _hnf_data_DB=_hnf_data_DB=cmd_in_array[0][2];print('Your Default Browser Is: '+_hnf_data_DB+' | check out!')", "if cmd_in_array[0][1]=='test': exec(_hnf_data_defaultBrowser.format(browser=_hnf_data_DB, url=cmd_in_array[0][2]));print('RUNNING IN '+ctc(_hnf_data_DB, 'green')+' | '+ctc(cmd_in_array[0][1], 'red')+' PR YN.')", "if cmd_in_array[0][1]=='run': FlASK_SERVICE.run('');"], "single": 0},
                            "shodan": {"cmd": ["if cmd_in_array[0][1]=='init': os.system('shodan init {shodan_ak}'.format(shodan_ak=cmd_in_array[0][2]))", "if cmd_in_array[0][1]=='setup' or 'install': os.system('start pip install shodan');os.system('pip install shodan');print(NO.NOTIFICATION_ADD+' Shodan Initilaztion.')", "if cmd_in_array[0][1]=='search': os.system('shodan search '+cmd_in_array[0][2])"], "single": 0}
                            }"""

    _hnf_everydaytips_one = _hnf_everydaytips[random.randint(0, len(_hnf_everydaytips) - 1)]
    if kwarg.no_dns_server_proxy == "false" or kwarg.no_dns_server_proxy == "0":
        if (sys.platform == "linux") or ("linux2" == sys.platform):
            print(ctc("You Are Running in Linux / Unix Environment, Try to Root for the server services.", "grey", "on_red", ["underline", "blink"]))
            hosts_file = open("/etc/hosts", "r+")
            hosts_file_a = hosts_file.read().__str__().replace(
                "127.0.0.1 hypernetworkframework.carbondoxdfuckedwerewolfwolfyxd.su", "")
            hosts_file_b = open("/etc/hosts", "w+")
            hosts_file_b.write(hosts_file_a)
            hosts_file_b.flush()
            hosts_file_b.close()
            hosts_file.close()
        elif (sys.platform == "win32"):
            print(ctc("You Are Running in Windows / OS2 Environment, Try to run with usr Administrator(UAC) for the server services.", "grey", "on_red", ["underline", "blink"]))
            hosts_file = open("C:\Windows\System32\drivers\etc\hosts", "r+")
            hosts_file_a = hosts_file.read().__str__().replace("127.0.0.1 hypernetworkframework.carbondoxdfuckedwerewolfwolfyxd.su", "")
            hosts_file_b = open("C:\Windows\System32\drivers\etc\hosts", "w+")
            hosts_file_b.write(hosts_file_a)
            hosts_file_b.flush()
            hosts_file_b.close()
            hosts_file.close()
    if os.path.exists(_hnf_path):
        _hnf_exploitsfile_data = open(_hnf_path + "/" + _hnf_exploitsfile, "r+")
        _hnf_auxiliaryfile_data = open(_hnf_path + "/" + _hnf_auxiliaryfile, "r+")
        _hnf_initanimate_data = open(_hnf_path + "/" + _hnf_initanimate, "r+")
        _hnf_commandlist_data = open(_hnf_path + "/" + _hnf_commandlist, "r+")
        if not os.path.exists(_hnf_path + "/" + _hnf_exploitsfile):
            _hnf_exploitsfile_data.write("[\n]")
            _hnf_exploitsfile_data.flush()
        if not os.path.exists(_hnf_path + "/" + _hnf_auxiliaryfile):
            _hnf_auxiliaryfile_data.write("[\n]")
            _hnf_auxiliaryfile_data.flush()
        if not os.path.exists(_hnf_path + "/" + _hnf_auxiliaryfile):
            _hnf_commandlist_data.write(_hnf_commandlists)
            _hnf_commandlist_data.flush()
        if not os.path.exists(_hnf_path + "/" + _hnf_initanimate):
            _hnf_initanimate_data.write(_hnf_initanimate_json)
            _hnf_initanimate_data.flush()
        if not os.path.exists(_hnf_path + "/" + _hnf_firstload):
            draw_init_setup()
        _hnf_commandlist_data.close()
        draw_main()
    else:
        os.mkdir(_hnf_path)
        _hnf_exploitsfile_data = open(_hnf_path + "/" + _hnf_exploitsfile, "w+")
        _hnf_auxiliaryfile_data = open(_hnf_path + "/" + _hnf_auxiliaryfile, "w+")
        _hnf_initanimate_data = open(_hnf_path + "/" + _hnf_initanimate, "w+")
        _hnf_commandlist_data = open(_hnf_path + "/" + _hnf_commandlist, "w+")
        if not os.path.exists(_hnf_path + "/" + _hnf_exploitsfile):
            _hnf_exploitsfile_data.write("[\n]")
            _hnf_exploitsfile_data.flush()
        if len(_hnf_exploitsfile_data.read().__str__()) <= 3:
            _hnf_exploitsfile_data.write("[\n]")
            _hnf_exploitsfile_data.flush()
        if not os.path.exists(_hnf_path + "/" + _hnf_auxiliaryfile):
            _hnf_auxiliaryfile_data.write("[\n]")
            _hnf_auxiliaryfile_data.flush()
        if len(_hnf_auxiliaryfile_data.read().__str__()) <= 3:
            _hnf_auxiliaryfile_data.write("[\n]")
            _hnf_auxiliaryfile_data.flush()
        if not os.path.exists(_hnf_path + "/" + _hnf_auxiliaryfile):
            _hnf_commandlist_data.write(_hnf_commandlists)
            _hnf_commandlist_data.flush()
        if len(_hnf_commandlist_data.read().__str__()) <= 3:
            _hnf_commandlist_data.write(_hnf_commandlists)
            _hnf_commandlist_data.flush()
        if not os.path.exists(_hnf_path + "/" + _hnf_initanimate):
            _hnf_initanimate_data.write(_hnf_initanimate_json)
            _hnf_initanimate_data.flush()
        if _hnf_initanimate_data.read().__str__() == "" or None or " ":
            _hnf_initanimate_data.write(_hnf_initanimate_json)
            _hnf_initanimate_data.flush()
        if not os.path.exists(_hnf_path + "/" + _hnf_firstload):
            draw_init_setup()
        _hnf_commandlist_data.close()
        init()


def draw_init_setup():
    print("\n" + " ** Welcome to Hypernetwork Framework Inital Setup ** ")
    print("    Please answer a few questions to get started.    ")
    print("\n" + "Would you like buy us a coffee? (1=yes/0=no)")
    _temp_condifident = int(input(": ").__str__())
    if _temp_condifident == 1:
        print("\ntry donate us? https://hypernetworkframework.carbondoxdfuckedwerewolfwolfyxd.su/donate/zh-cn\n")
    open(_hnf_path + "/" + _hnf_firstload, "w").close()
    print(NO.NOTIFICATION_WARN + "This is your first time to load, you can try to using help at first!")
    draw_main()


def draw_main():
    global cmd_in_header
    cmd_in_header = ""
    if cmd_in_header == None or "" or " ":
        cmd_in_header = ""
    _hnf_initanimate_data = open(_hnf_path + "/" + _hnf_initanimate, "r+")
    if len(_hnf_initanimate_data.read().__str__()) <= 10:
        _hnf_initanimate_data.write('{\n"animate": ["[*] Starting the Hypernetwork Framework Console.../",'
                                    '"[*] StArting the Hypernetwork Framework Console...-","[*] StaRting the '
                                    'Hypernetwork Framework Console...\\\\","[*] StarTing the Hypernetwork Framework '
                                    'Console...|","[*] StartIng the Hypernetwork Framework Console.../","[*] StartiNg '
                                    'the Hypernetwork Framework Console...-","[*] StartinG the Hypernetwork Framework '
                                    'Console...\\\\","[*] Starting the Hypernetwork Framework Console...|",'
                                    '"[*] Starting The Hypernetwork Framework Console.../","[*] Starting tHe '
                                    'Hypernetwork Framework Console...-","[*] Starting thE Hypernetwork Framework '
                                    'Console...\\\\","[*] Starting the Hypernetwork Framework Console...|",'
                                    '"[*] Starting the HYpernetwork Framework Console.../","[*] Starting the '
                                    'HyPernetwork Framework Console...-","[*] Starting the HypErnetwork Framework '
                                    'Console...\\\\","[*] Starting the HypeRnetwork Framework Console...|",'
                                    '"[*] Starting the HyperNetwork Framework Console.../","[*] Starting the '
                                    'HypernEtwork Framework Console...-","[*] Starting the HyperneTwork Framework '
                                    'Console...\\\\","[*] Starting the HypernetWork Framework Console...|",'
                                    '"[*] Starting the HypernetwOrk Framework Console.../","[*] Starting the '
                                    'HypernetwoRk Framework Console...-","[*] Starting the HypernetworK Framework '
                                    'Console...\\\\","[*] Starting the Hypernetwork Framework Console...|",'
                                    '"[*] Starting the Hypernetwork FRamework Console.../","[*] Starting the '
                                    'Hypernetwork FrAmework Console...-","[*] Starting the Hypernetwork FraMework '
                                    'Console...\\\\","[*] Starting the Hypernetwork FramEwork Console...|",'
                                    '"[*] Starting the Hypernetwork FrameWork Console.../","[*] Starting the '
                                    'Hypernetwork FramewOrk Console...-","[*] Starting the Hypernetwork FramewoRk '
                                    'Console...\\\\","[*] Starting the Hypernetwork FrameworK Console...|",'
                                    '"[*] Starting the Hypernetwork Framework Console.../","[*] Starting the '
                                    'Hypernetwork Framework Console...-","[*] Starting the Hypernetwork Framework '
                                    'COnsole...\\\\","[*] Starting the Hypernetwork Framework CoNsole...|",'
                                    '"[*] Starting the Hypernetwork Framework ConSole.../","[*] Starting the '
                                    'Hypernetwork Framework ConsOle...-","[*] Starting the Hypernetwork Framework '
                                    'ConsoLe...\\\\","[*] Starting the Hypernetwork Framework ConsolE...|", "    "]\n}')
        _hnf_initanimate_data.flush()
    _a = open(_hnf_path + "/" + _hnf_initanimate, "r+").read().__str__()
    _hnf_initanimate_json = json.loads(_a)

    def progress_bar():
        for i in range(0, len(_hnf_initanimate_json["animate"])):
            print("\r", end="")
            print(_hnf_initanimate_json["animate"][i], end="")
            sys.stdout.flush()
            time.sleep(0.08)

    pb_num = random.randint(1, 5)
    for i in range(1, pb_num):
        progress_bar()
    print("\n")
    hnf_exploits_json = json.loads(open(_hnf_path + "/" + _hnf_exploitsfile, "r+").read().__str__())
    hnf_auxiliary_json = json.loads(open(_hnf_path + "/" + _hnf_auxiliaryfile, "r+").read().__str__())
    hnf_commandlist_json = json.loads(open(_hnf_path + "/" + _hnf_commandlist, "r+").read().__str__())
    if not os.path.exists(_hnf_path + "/" + _hnf_exploitsfile):
        print(NO.NOTIFICATION_WARN + " NO EXPLOITS FILE, CREATING.")
    if not os.path.exists(_hnf_path + "/" + _hnf_firstload): draw_init_setup()
    print("        =[ " + ctc(data_d("P") + " v" + data_d("V") + "-dev-", "cyan") + "    ]")
    print("+ --  --=[ " + len(hnf_exploits_json).__str__() + " exploits - " + len(
        hnf_auxiliary_json).__str__() + " auxiliary    ]")
    print("+ --  --=[ " + len(hnf_commandlist_json).__str__() + " commands - " + len(
        hnf_auxiliary_json).__str__() + " auxiliary    ]")
    print("\n" + "Hypernetwork tips: " + _hnf_everydaytips_one + "\n")
    badtry = False
    while 1:
        cmd_in = input(
            data_d("H") + " " + ctc(getbackheader(False, "") + _cmdtemp_use_in + cmd_in_header, "grey", "on_red",
                                    ["underline", "blink"]) + "" + ctc("> ", "white"))
        cmd_in_array = [cmd_in.split(" ")]
        cmd_in_array_ph = ""
        for i in range(0, len(cmd_in_array)):
            cmd_in_array_ph += cmd_in_array[0][i]
        for i in hnf_commandlist_json:
            if cmd_in_array[0][0] == i:
                if hnf_commandlist_json[i]["single"] == 1:
                    exec(hnf_commandlist_json[i]["cmd"])
                    badtry = False
                    break
                else:
                    if hnf_commandlist_json[i]["single"] == 0:
                        for n in range(0, len(hnf_commandlist_json[i]["cmd"])):
                            exec(hnf_commandlist_json[i]["cmd"][n])
                            badtry = False
                        break
                    else:
                        print(ctc("[DEBUGGER OF COMMAND]: WRONG 'single' TYPE: " + hnf_commandlist_json[i], "red",
                                  "white", ["underline"]))
            else:
                badtry = True
        if badtry: print(ctc("BAD COMMAND HERE: " + cmd_in_array.__str__(), "red", None, ["underline"]))


def data_d(info):
    ver = "1.0 alpha"
    prg = "Hypernetwork Framework Console"
    hed = ctc("hnf", None, None, ["underline"])
    hum = ctc(_hnf_header_usemodule, "white", "on_red", ["underline"])
    rgt = ctc("> ", "white")
    if info == "VERSION" or info == "VER" or info == "V":
        return ver
    elif info == "PROGRAM" or info == "PRG" or info == "P":
        return prg
    elif info == "LOCATION" or info == "LOCA" or info == "LS" or info == "DIR":
        return os.getcwd()
    elif info == "GET_HEAD" or info == "HEAD" or "H":
        return hed
    elif info == "HEADER_USEMODULE" or info == "HU":
        return hum
    elif info == "RIGHT_RT" or "RT":
        return rgt


if __name__ == "__main__":
    init()
