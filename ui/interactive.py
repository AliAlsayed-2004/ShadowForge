"""Interactive CLI helpers (placeholder)."""

def prompt_loop():
    try:
        while True:
            cmd = input('> ')
            if cmd in ('q', 'quit', 'exit'):
                break
            print(f"You typed: {cmd}")
    except (KeyboardInterrupt, EOFError):
        print('\nExiting')
