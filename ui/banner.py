import os
import re
import platform
import datetime
import random
import pyfiglet

from ui.colors import Colors


class Banner:

    def __init__(self, name="ShadowForge", subtitle="Advanced Wordlist Generator",
                 developer="mrV", version="1.0"):

        self.name = name
        self.subtitle = subtitle
        self.developer = developer
        self.version = version

    def _width(self):
        try:
            return os.get_terminal_size().columns
        except OSError:
            return 100

    def _strip(self, text):
        return re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', text)

    def _line(self, text, width):
        clean = len(self._strip(text))
        pad = max(0, (width - 2) - clean)
        return f"{Colors.CYAN}║{text}{' ' * pad}{Colors.CYAN}║"

    def show(self):

        width = self._width()

        top = Colors.CYAN + "╔" + "═" * (width - 2) + "╗"
        mid = Colors.CYAN + "╠" + "═" * (width - 2) + "╣"
        bot = Colors.CYAN + "╚" + "═" * (width - 2) + "╝"

        print(top)

        logo = pyfiglet.figlet_format(
            self.name,
            font="slant",
            width=width - 2
        )

        for line in logo.splitlines():
            print(self._line(Colors.RED + line, width))

        print(mid)

        print(self._line(Colors.MAGENTA + self.subtitle, width))
        print(mid)

        info = [
            f"[+] Developer : {self.developer}",
            f"[+] Version   : {self.version}",
            f"[+] OS        : {platform.system()} {platform.release()}",
            f"[+] Python    : {platform.python_version()}",
            f"[+] Time      : {datetime.datetime.now().strftime('%H:%M:%S')}",
        ]

        for i in info:
            print(self._line(Colors.GREEN + i, width))

        print(bot)
        print(Colors.RESET)