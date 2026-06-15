import os
import sys
import argparse

from ui.banner import Banner
from ui.wizard import wizard

from core.generator import apply_patterns
from core.leet import leet
from core.numbers import generate_numbers
from core.filter import filter_length


def main():
    parser = argparse.ArgumentParser(
        prog="ShadowForge",
        description="Advanced Wordlist Generation Framework"
    )

    parser.add_argument("-p", "--profile", nargs="+")
    parser.add_argument("-k", "--keywords", nargs="*", default=[])
    parser.add_argument("--min", type=int, default=6)
    parser.add_argument("--max", type=int, default=12)

    parser.add_argument("--leet", action="store_true")
    parser.add_argument("--use-symbols", action="store_true")
    parser.add_argument("--symbols", default="!@#$%^&*")

    parser.add_argument("--digits", nargs=2, type=int)
    parser.add_argument("--numbers-mode", choices=["random", "sequence"], default="random")
    parser.add_argument("--limit", type=int, default=100000)

    parser.add_argument("--interactive", action="store_true")

    args = parser.parse_args()

    banner = Banner()
    banner.show()

    if len(sys.argv) == 1 or args.interactive:
        config = wizard()
    else:
        if not args.profile:
            parser.error("the following arguments are required: -p/--profile when not using --interactive")

        config = {
            "profile": args.profile,
            "keywords": args.keywords,
            "min": args.min,
            "max": args.max,
            "leet": args.leet,
            "symbols": args.symbols,
            "use_symbols": args.use_symbols,
            "digits": tuple(args.digits) if args.digits else None,
            "numbers_mode": args.numbers_mode,
            "limit": args.limit,
        }

    base_words = list(set(config["profile"] + config["keywords"]))

    numbers = []
    if config["digits"]:
        numbers = generate_numbers(
            config["digits"][0],
            config["digits"][1],
            config["numbers_mode"]
        )

    words = apply_patterns(base_words, numbers, config["symbols"], config["use_symbols"])

    if config["leet"]:
        extra = []
        for w in words:
            extra.extend(leet(w))
        words += extra

    words = list(set(words))
    words = filter_length(words, config["min"], config["max"])
    words = words[:config["limit"]]

    os.makedirs("wordlists", exist_ok=True)

    out_file = config["profile"][0]
    path = f"wordlists/{out_file}_wordlist.txt"

    with open(path, "w") as f:
        for w in words:
            f.write(w + "\n")

    print(f"\n[✔] Saved → {path}\n")


if __name__ == "__main__":
    main()