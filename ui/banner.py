import os
import platform
import datetime

from ui.colors import Colors


class Banner:

    def __init__(self):
        self.title = '''
███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗    ███████╗ ██████╗ ██████╗  ██████╗ ███████╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║    ██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║    █████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║    ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝    ██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝     ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
'''

        self.subtitle = "Wordlist Generation Framework"

        self.themes = {
            "default": Colors.CYAN,
            "neon": Colors.MAGENTA,
            "matrix": Colors.GREEN,
            "fire": Colors.RED,
        }

        self.theme = self.themes["default"]

    # ----------------------------
    def _width(self):
        try:
            return min(os.get_terminal_size().columns, 110)
        except:
            return 100

    def _clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # ----------------------------
    def _line(self, text, width, color=None):
        if color is None:
            color = self.theme
        return color + "║ " + text.ljust(width - 4) + " ║"

    def _kv(self, key, value):
        return f"{Colors.CYAN}{key:<10}{Colors.RESET}: {Colors.GREEN}{value}"

    def set_theme(self, name):
        if name in self.themes:
            self.theme = self.themes[name]

    # ----------------------------
    def show(self):
        self._clear()
        width = self._width()

        top = self.theme + "╔" + "═" * (width - 2) + "╗"
        mid = self.theme + "╠" + "═" * (width - 2) + "╣"
        bot = self.theme + "╚" + "═" * (width - 2) + "╝"

        print(top)

        # -------- STATIC LOGO --------
        for line in self.title.strip("\n").splitlines():
            print(self._line(line[:width - 2], width, self.themes["fire"]))

        print(mid)

        # -------- SUBTITLE --------
        print(self._line(self.subtitle.center(width - 4), width))
        print(self._line(
            "Red Team Utility | Pattern Engine | Shadow Ops".center(width - 4),
            width,
            self.themes["neon"]
        ))

        print(mid)

        # -------- SYSTEM INFO --------
        info = [
            self._kv("Developer", "Aloosh"),
            self._kv("Version", "2.1"),
            self._kv("OS", f"{platform.system()} {platform.release()}"),
            self._kv("Python", platform.python_version()),
            self._kv("Time", datetime.datetime.now().strftime('%H:%M:%S')),
        ]

        for line in info:
            print(self._line(line, width+22, self.themes["matrix"]))

        print(bot)
        print(Colors.RESET)

    # ----------------------------
    def show_minimal(self):
        print(f"{Colors.GREEN}[+] {self.subtitle} | v2.1{Colors.RESET}")