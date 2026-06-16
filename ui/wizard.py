from ui.colors import Colors
from core.numbers import generate_numbers
from core.leet import leet

def wizard():
    print(f"\n{Colors.CYAN}[+] ShadowForge Interactive Wizard\n")

    profile = input(f"{Colors.YELLOW}[?] Base names (space separated): ").split()
    keywords = input(f"{Colors.YELLOW}[?] Keywords (optional): ").split()

    print()

    min_len = int(input(f"{Colors.YELLOW}[?] Min length [6]: ") or 6)
    max_len = int(input(f"{Colors.YELLOW}[?] Max length [12]: ") or 12)

    print()

    leet_choice = input(f"{Colors.YELLOW}[?] Enable leetspeak? (y/n): ").lower() == "y"

    symbols_choice = input(f"{Colors.YELLOW}[?] Use symbols? (y/n): ").lower() == "y"
    symbols = "!@#$%^&*"

    if symbols_choice:
        custom = input(f"{Colors.MAGENTA}[$] Custom symbols (default !@#$%^&*): ")
        if custom.strip():
            symbols = custom.strip()

    print()

    digits = None
    digits_input = input(f"{Colors.YELLOW}[$] Digits range (min max) or 0 0: ").split()
    if len(digits_input) == 2:
        if digits_input[0] != "0" or digits_input[1] != "0":
            digits = (int(digits_input[0]), int(digits_input[1]))

    numbers_mode = input(f"{Colors.YELLOW}[?] Numbers mode (random/sequence) [random]: ") or "random"

    limit = int(input(f"{Colors.YELLOW}[?] Limit [100000]: ") or 100000)

    print(f"\n{Colors.GREEN}[+] Configuration locked. Generating...\n")

    return {
        "profile": profile,
        "keywords": keywords,
        "min": min_len,
        "max": max_len,
        "leet": leet_choice,
        "symbols": symbols,
        "use_symbols": symbols_choice,
        "digits": digits,
        "numbers_mode": numbers_mode,
        "limit": limit
    }