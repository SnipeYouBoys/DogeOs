import time
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread, main_thread
from time import sleep
import os
os.system('color 1')
class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        self.stop()
if __name__ == "__main__":
    with Loader("Loading DogeOS"):
        for i in range(2):
            sleep(0.5)
    with Loader("Loading Terminal"):
        for i in range(1):
            sleep(0.5)
    with Loader("Loading UI"):
        for i in range(1):
            sleep(0.5)

    loader = Loader("Loading Welcome Screen", "Done!", 0.05).start()
    for i in range(1):
        sleep(0.25)
    loader.stop()

os.system('cls' if os.name == 'nt' else 'clear')
os.system('color 5')
print("DDDDDDDDDDDDD                   Welcome To                                         OOOOOOOOO")
time.sleep(0.01)
print("D::::::::::::DDD                                                                 OO:::::::::OO")                    
time.sleep(0.01)
print("D:::::::::::::::DD                                                             OO:::::::::::::OO")                  
time.sleep(0.01)
print("DDD:::::DDDDD:::::D                                                           O:::::::OOO:::::::O")                 
time.sleep(0.01)
print("  D:::::D    D:::::D    ooooooooooo      ggggggggg   ggggg    eeeeeeeeeeee    O::::::O   O::::::O    ssssssssss")   
time.sleep(0.01)
print("  D:::::D     D:::::D oo:::::::::::oo   g:::::::::ggg::::g  ee::::::::::::ee  O:::::O     O:::::O  ss::::::::::s")  
time.sleep(0.01)
print("  D:::::D     D:::::Do:::::::::::::::o g:::::::::::::::::g e::::::eeeee:::::eeO:::::O     O:::::Oss:::::::::::::s") 
time.sleep(0.01)
print("  D:::::D     D:::::Do:::::ooooo:::::og::::::ggggg::::::gge::::::e     e:::::eO:::::O     O:::::Os::::::ssss:::::s")
time.sleep(0.01)
print("  D:::::D     D:::::Do::::o     o::::og:::::g     g:::::g e:::::::eeeee::::::eO:::::O     O:::::O s:::::s  ssssss ")
time.sleep(0.01)
print("  D:::::D     D:::::Do::::o     o::::og:::::g     g:::::g e:::::::::::::::::e O:::::O     O:::::O   s::::::s      ")
time.sleep(0.01)
print("  D:::::D     D:::::Do::::o     o::::og:::::g     g:::::g e::::::eeeeeeeeeee  O:::::O     O:::::O      s::::::s   ")
time.sleep(0.01)
print("  D:::::D    D:::::D o::::o     o::::og::::::g    g:::::g e:::::::e           O::::::O   O::::::Ossssss   s:::::s ")
time.sleep(0.01)
print("DDD:::::DDDDD:::::D  o:::::ooooo:::::og:::::::ggggg:::::g e::::::::e          O:::::::OOO:::::::Os:::::ssss::::::s")
time.sleep(0.01)
print("D:::::::::::::::DD   o:::::::::::::::o g::::::::::::::::g  e::::::::eeeeeeee   OO:::::::::::::OO s::::::::::::::s ")
time.sleep(0.01)
print("D::::::::::::DDD      oo:::::::::::oo   gg::::::::::::::g   ee:::::::::::::e     OO:::::::::OO    s:::::::::::ss  ")
time.sleep(0.01)
print("DDDDDDDDDDDDD           ooooooooooo       gggggggg::::::g     eeeeeeeeeeeeee       OOOOOOOOO       sssssssssss    ")
time.sleep(0.01)
print("                                                  g:::::g                                                         ")
time.sleep(0.01)
print("                                      gggggg      g:::::g                                                         ")
time.sleep(0.01)
print("                                      g:::::gg   gg:::::g                                                         ")
time.sleep(0.01)
print("                                       g::::::ggg:::::::g                 v1.5")
time.sleep(0.01)
print("                                        gg:::::::::::::g                                                          ")
time.sleep(0.01)
print("                                          ggg::::::ggg                                                            ")
time.sleep(0.01)
print("                                             gggggg                  ")
time.sleep(1.5)
os.system('cls||clear')
os.system('color 2')
doge = "dogeos@"
symbol = ">"
path = os.path.expanduser('~')
path = f'{doge}{path}{symbol}'
cmd = input (path)
if cmd == ("quit"):
    import main;
else:
    os.system(f'cmd /k "{cmd}"');

