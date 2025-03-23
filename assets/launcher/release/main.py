import assets.assetGetter as assetGetter
import hashlib
import os
import subprocess

def content(path):
    with open(path, "r") as f:
        return f.read()

asset = assetGetter.getter("https://raw.githubusercontent.com/RRDDMC/YOG/main/assets/", manifest ="versions.txt", localPath="assets/")

class launcher():
    def __init__(self):
        self.running = False
    def f_help(self, *args):
        """Show all commands"""
        commands = [elt for elt in dir(self) if elt[:2] == "f_"]
        for command in commands:
            print("{}: {}".format(command[2:], getattr(self, command).__doc__))
    def f_offline(self, *args):
        """Show installed version"""
        if os.path.exists("assets/launcher/versions.txt"):
            print(content("assets/launcher/versions.txt"))
        else:
            print("No offline versions")
    def f_launch(self, *args):
        """Launch version in arg VER
        VER -> Version: release, beta, [VERSION]"""
        try:
            if args[0] == "dev":
                raise KeyError
            asset.getAssets(args[0])
            subprocess.Popen([os.getcwd() + "/yog", "assets/{}/main.py".format(args[0])], env={"PYTHONPATH": os.getcwd() + "/lib"})
        except IndexError:
            print("Missing VER argument")
        except KeyError:
            print("Unknown version: {}".format(args[0]))
    def f_dev(self, *args):
        """Launch dev version"""
        token = input("Token: ")
        if hashlib.sha256(token.replace("\n", "").encode("utf-8")).hexdigest() == '0ea0af45c5824d9f5e578f3717680ea6583ec933355a313f63c8d87f07e7ec9f':
            try:
                asset.getAssets("dev", forceUpdate=True)
                subprocess.Popen([os.getcwd() + "/yog", "assets/dev/main.py".format(args[0])], env={"PATH": os.getcwd() + "/lib"})
            except KeyError:
                print("'dev' version is not available")
    def f_quit(self, *args):
        """Exit launcher"""
        print("Exit...")
        self.running = False
    def run(self):
        print("Welcome in YOG launcher.\nAsk 'help' for more informations.")
        self.running = True
        while self.running:
            try:
                entry = input("> ").split()
                getattr(self, f"f_{entry.pop(0)}")(*entry)
            except AttributeError:
                print("Unknown command")
            except Exception as error:
                errorType = str(error.__class__)
                print("{}: {}".format(errorType[errorType.find("'")+1:errorType.find("'>")], error))
            except KeyboardInterrupt:
                self.f_quit()

launcher().run()
