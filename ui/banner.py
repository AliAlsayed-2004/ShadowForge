import os
import sys
import time
import platform
import datetime
import pyfiglet

from ui.colors import Colors


class Banner:

    def __init__(self):
        self.name = "Shadow  Forge"
        self.subtitle = "Wordlist Generation Framework"

        # Theme system (plugin-ready)
        self.themes = {
            "default": Colors.CYAN,
            "neon": Colors.MAGENTA,
            "matrixless": Colors.GREEN,
            "fire": Colors.RED,
        }

        self.theme = self.themes["default"]

    # ----------------------------
    # TERMINAL WIDTH
    # ----------------------------
    def _width(self):
        try:
            return min(os.get_terminal_size().columns, 110)
        except:
            return 100
        
    def _clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    # ----------------------------
    # CLEAN PRINT (smooth, no flicker)
    # ----------------------------
    def _slow_print(self, text, delay=0.01):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    # ----------------------------
    # TYPEWRITER EFFECT
    # ----------------------------
    def _type(self, text, speed=0.03):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(speed)
        print()

    # ----------------------------
    # BEEP SIMULATION (safe UX)
    # ----------------------------
    def _beep(self):
        sys.stdout.write("\a")
        sys.stdout.flush()

    # ----------------------------
    # BORDER PULSE ANIMATION
    # ----------------------------
    def _pulse_border(self, width, cycles=3):
        for i in range(cycles):
            char = "═" if i % 2 == 0 else "─"
            top = self.theme + "╔" + char * (width - 2) + "╗"
            print(top)
            time.sleep(0.1)
            self._clear_line()

    def _clear_line(self):
        sys.stdout.write("\033[F")

    # ----------------------------
    # TAKEOVER INTRO SEQUENCE
    # ----------------------------
    def _intro(self):
        sequence = [
            "[*] Booting ShadowForge core...",
            "[*] Loading cryptographic modules...",
            "[*] Establishing secure runtime...",
            "[*] Injecting pattern engine...",
            "[*] Environment ready."
        ]

        for line in sequence:
            self._beep()
            self._type(line, speed=0.02)
            time.sleep(0.15)

    # ----------------------------
    # PLUGIN THEME SYSTEM
    # ----------------------------
    def set_theme(self, name):
        if name in self.themes:
            self.theme = self.themes[name]

    # ----------------------------
    # MAIN BANNER
    # ----------------------------
    def show(self):
        self._clear()
        width = self._width()

        # intro sequence (system takeover feel)
        self._intro()
        self._clear()


        # border pulse effect
        self._pulse_border(width)

        top = self.theme + "╔" + "═" * (width - 2) + "╗"
        mid = self.theme + "╠" + "═" * (width - 2) + "╣"
        bot = self.theme + "╚" + "═" * (width - 2) + "╝"

        print(top)

        # ASCII logo (smooth, no glitch)
        logo = pyfiglet.figlet_format(
            self.name,
            font="doom",
            width=width - 2
        )

        for line in logo.splitlines():
            self._slow_print(self.theme + line, delay=0.002)

        print(mid)

        # cinematic typing subtitle
        self._type(self.subtitle, speed=0.04)
        self._type(f"{self.themes['neon']}Red Team Utility | Pattern Engine | Shadow Operations", speed=0.03)

        print(mid)

        # system info block (stable clean style)
        info = [
            f"Developer   : Aloosh",
            f"Version    : 2.1",
            f"System     : {platform.system()} {platform.release()}",
            f"Python     : {platform.python_version()}",
            f"Time       : {datetime.datetime.now().strftime('%H:%M:%S')}",
            f"Status     : ACTIVE"
        ]

        for i in info:
            self._slow_print(self.themes['matrixless'] + i, delay=0.01)

        print(bot)
        print(Colors.RESET)