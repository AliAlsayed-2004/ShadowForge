import os

from ui.banner import Banner
from ui.wizard import wizard

from core.generator import apply_patterns
from core.leet import leet
from core.numbers import generate_numbers
from core.filter import filter_length


def main():

    banner = Banner()
    banner.show()

    config = wizard()

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