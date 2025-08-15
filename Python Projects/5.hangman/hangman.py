#!/usr/bin/env python3
# ================================================================
# Hangman — Color + Sound + BIG Animated Win/Lose (Block-Font Intro)
# Fully commented and stable in VS Code / Windows Terminal / macOS
# ================================================================

# ----------------- Imports -----------------
import os                  # clear screen & detect OS
import sys                 # cursor show/hide, stdout writes
import time                # tiny animation delays
import random              # choosing words & hints
import shutil              # get terminal width (for fitting banners)
from dataclasses import dataclass  # small typed container

# Try Windows beeps; other OSs will use '\a' (terminal bell)
try:
    import winsound        # only exists on Windows
except Exception:
    winsound = None


# ----------------- Enable ANSI color on Windows -----------------
def _enable_ansi_on_windows():
    """Turn on ANSI color support on Windows 10+; safe no-op elsewhere."""
    if os.name != "nt":
        return
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)              # STD_OUTPUT_HANDLE
        mode = ctypes.c_uint32()
        kernel32.GetConsoleMode(handle, ctypes.byref(mode))
        kernel32.SetConsoleMode(handle, mode.value | 0x0004)  # ENABLE_VIRTUAL_TERMINAL_PROCESSING
    except Exception:
        pass                                              # if it fails, game still works

_enable_ansi_on_windows()


# ----------------- Color constants -----------------
class C:
    RESET   = "\033[0m"    # reset styles
    BOLD    = "\033[1m"    # bold
    DIM     = "\033[2m"    # dim

    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"
    GRAY    = "\033[90m"


def colorize(text: str, color: str) -> str:
    """Wrap text with a color and reset."""
    return f"{color}{text}{C.RESET}"


# ----------------- Rainbow helpers -----------------
def rainbow(text: str) -> str:
    """Static rainbow (per-character cycling)."""
    palette = [C.RED, C.YELLOW, C.GREEN, C.CYAN, C.BLUE, C.MAGENTA]
    return "".join(palette[i % len(palette)] + ch + C.RESET for i, ch in enumerate(text))


def rainbow_wave(text: str, phase: int = 0) -> str:
    """Moving rainbow (shifted by 'phase')."""
    palette = [C.RED, C.YELLOW, C.GREEN, C.CYAN, C.BLUE, C.MAGENTA]
    return "".join(palette[(i + phase) % len(palette)] + ch + C.RESET for i, ch in enumerate(text))


def animate_rainbow_banner(lines, cycles: int = 18, delay: float = 0.05):
    """
    Animate a multi-line banner with a rainbow wave by redrawing the same N lines.
    """
    if not lines:
        return
    sys.stdout.write("\033[?25l"); sys.stdout.flush()           # hide cursor
    try:
        for line in lines:                                      # first frame
            print(rainbow_wave(line, 0))
        time.sleep(delay)
        for phase in range(1, cycles + 1):                      # subsequent frames
            sys.stdout.write(f"\033[{len(lines)}A"); sys.stdout.flush()
            for line in lines:
                print(rainbow_wave(line, phase))
            time.sleep(delay)
    finally:
        sys.stdout.write("\033[?25h"); sys.stdout.flush()       # show cursor


# ----------------- Single-color wave (for WIN=green / LOSE=red) -----------------
def _mono_wave(text: str, base_color: str, phase: int, span: int = 8) -> str:
    """
    Apply a shimmer using BOLD → normal → DIM bands across the text.
    Looks like a wave traveling left→right.
    """
    out = []
    for i, ch in enumerate(text):
        if ch == " ":
            out.append(" ")
            continue
        band = (i + phase) % span
        if band in (0, 1):
            c = C.BOLD + base_color      # bright band
        elif band in (2, 3, 4):
            c = base_color               # mid band
        else:
            c = C.DIM + base_color       # trailing dim band
        out.append(f"{c}{ch}{C.RESET}")
    return "".join(out)


def animate_mono_wave(lines, base_color: str, cycles: int = 24, delay: float = 0.05, span: int = 8):
    """Animate the single-color wave across multiple lines."""
    if not lines:
        return
    sys.stdout.write("\033[?25l"); sys.stdout.flush()
    try:
        for phase in range(0, cycles + 1):
            if phase:
                sys.stdout.write(f"\033[{len(lines)}A"); sys.stdout.flush()
            for line in lines:
                print(_mono_wave(line, base_color, phase, span))
            time.sleep(delay)
    finally:
        sys.stdout.write("\033[?25h"); sys.stdout.flush()


# ----------------- Utilities -----------------
def clear_screen():
    """CLS/clear wrapper."""
    os.system("cls" if os.name == "nt" else "clear")


def term_width(default: int = 80) -> int:
    """Get current terminal width, with a safe fallback."""
    try:
        return shutil.get_terminal_size(fallback=(default, 24)).columns
    except Exception:
        return default


# ----------------- Sounds -----------------
def beep_ok():
    if winsound and os.name == "nt": winsound.Beep(880, 120)
    else: sys.stdout.write("\a"); sys.stdout.flush()

def beep_bad():
    if winsound and os.name == "nt": winsound.Beep(220, 180)
    else:
        sys.stdout.write("\a"); sys.stdout.flush()
        time.sleep(0.08)
        sys.stdout.write("\a"); sys.stdout.flush()

def fanfare_win():
    if winsound and os.name == "nt":
        for f, d in [(880,120),(988,120),(1046,200),(1318,250)]:
            winsound.Beep(f,d); time.sleep(0.03)
    else:
        for _ in range(3):
            sys.stdout.write("\a"); sys.stdout.flush(); time.sleep(0.12)

def dirge_lose():
    if winsound and os.name == "nt":
        for f, d in [(440,250),(392,250),(349,350)]:
            winsound.Beep(f,d); time.sleep(0.04)
    else:
        for _ in range(2):
            sys.stdout.write("\a"); sys.stdout.flush(); time.sleep(0.2)


# ----------------- ASCII gallows -----------------
STAGES = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
   =========""",
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
   =========""",
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
   =========""",
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
   =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
   =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
   =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
   ========="""
]


# ----------------- Block font (Unicode █) for banners -----------------
# We include letters needed for: YOU WIN! / YOU LOSE / HANGMAN.
_FONT = {
    "A": [" █████ ", "██   ██", "███████", "██   ██", "██   ██"],
    "E": ["██████ ", "██     ", "█████  ", "██     ", "██████ "],
    "G": [" █████ ", "██     ", "██  ███", "██   ██", " █████ "],
    "H": ["██   ██", "██   ██", "███████", "██   ██", "██   ██"],
    "I": [" █████ ", "   ██  ", "   ██  ", "   ██  ", " █████ "],
    "L": ["██     ", "██     ", "██     ", "██     ", "██████ "],
    "M": ["███ ███", "██ █ ██", "██   ██", "██   ██", "██   ██"],
    "N": ["██   ██", "███  ██", "██ █ ██", "██  ███", "██   ██"],
    "O": [" █████ ", "██   ██", "██   ██", "██   ██", " █████ "],
    "S": [" █████ ", "██     ", " █████ ", "     ██", " █████ "],
    "U": ["██   ██", "██   ██", "██   ██", "██   ██", " █████ "],
    "W": ["██     ██", "██  █  ██", "██  █  ██", "██ ███ ██", " ███ ███ "],  # (not used in title, but used in "YOU WIN!")
    "Y": ["██   ██", " ██ ██ ", "  ███  ", "  ███  ", "  ███  "],
    "!": ["  ██  ", "  ██  ", "  ██  ", "      ", "  ██  "],
    " ": ["  ", "  ", "  ", "  ", "  "],
}

def big_text_lines(message: str):
    """Render 5-line big text using the block font above."""
    msg = message.upper()
    out = ["", "", "", "", ""]
    for ch in msg:
        glyph = _FONT.get(ch, _FONT[" "])        # unknown -> space
        for r in range(5):
            out[r] += glyph[r] + "  "            # gap between letters
    return out


# Clear boxes shown beneath the waves (readable in any font)
WIN_BOX  = "+--------------------------------+\n|            YOU WIN!            |\n+--------------------------------+"
LOSE_BOX = "+--------------------------------+\n|            YOU LOSE            |\n+--------------------------------+"


# ----------------- Words & difficulty -----------------
WORDS = {
    "animals": ["elephant","giraffe","hippopotamus","kangaroo","dolphin","rhinoceros",
                "alligator","chimpanzee","penguin","flamingo","salamander","butterfly"],
    "countries": ["canada","brazil","portugal","germany","australia","singapore",
                  "argentina","jamaica","iceland","ethiopia","thailand","hungary"],
    "tech": ["algorithm","encryption","database","variable","function","exception",
             "compiler","framework","protocol","bandwidth","container","python"],
    "random": ["avalanche","strawberry","moonlight","harmony","pneumonia","microscope",
               "telescope","pharaoh","boulevard","xylophone","psyche","oxygen"]
}

DIFFICULTY = {"easy": 8, "normal": 6, "hard": 5, "insane": 4}


# ----------------- Optional config container -----------------
@dataclass
class GameConfig:
    category: str
    lives: int
    word: str


# ----------------- Input helpers -----------------
def choose_category() -> str:
    """Ask the player for a category; Enter = random."""
    cats = list(WORDS.keys())
    print(colorize("\nCategories: ", C.CYAN) + ", ".join(cats))
    while True:
        c = input(colorize("Pick a category (or press Enter for random): ", C.CYAN)).strip().lower()
        if c == "":
            return random.choice(cats)
        if c in WORDS:
            return c
        print(colorize("Invalid category. Try again.", C.YELLOW))

def choose_difficulty() -> int:
    """Ask the player for difficulty; Enter = normal."""
    diff_str = ", ".join(f"{k}({v} lives)" for k, v in DIFFICULTY.items())
    print(colorize(f"\nDifficulty: {diff_str}", C.MAGENTA))
    while True:
        d = input(colorize("Pick difficulty [easy/normal/hard/insane] (Enter=normal): ", C.MAGENTA)).strip().lower()
        if d == "":
            return DIFFICULTY["normal"]
        if d in DIFFICULTY:
            return DIFFICULTY[d]
        print(colorize("Invalid difficulty. Try again.", C.YELLOW))

def pick_word(category: str) -> str:
    """Return a random word from the chosen category."""
    return random.choice(WORDS[category]).lower()

def get_letter(already: set) -> str:
    """Read a guess; return 'hint' or a single letter."""
    while True:
        s = input(colorize("Guess a letter (or type 'hint' once): ", C.BLUE)).strip().lower()
        if s == "hint":
            return "hint"
        if len(s) != 1 or not s.isalpha():
            print(colorize("Please enter a single A–Z letter.", C.YELLOW)); beep_bad(); continue
        if s in already:
            print(colorize("You already guessed that. Try another.", C.YELLOW)); beep_bad(); continue
        return s

def reveal_hint(secret: str, guessed: set):
    """Pick one unrevealed letter at random; None if all revealed."""
    hidden = [c for c in set(secret) if c not in guessed]
    return random.choice(hidden) if hidden else None


# ----------------- Rendering -----------------
def draw_gallows(mistakes: int) -> str:
    """Return the current stage of the gallows, color-coded by danger."""
    art = STAGES[min(mistakes, len(STAGES)-1)]
    color = C.GREEN if mistakes <= 2 else C.YELLOW if mistakes <= 4 else C.RED
    return colorize(art, color)

def alphabet_line(secret: str, guessed: set) -> str:
    """Return A–Z with colors: green=correct, red=wrong, gray=unused."""
    out = []
    for code in range(ord('a'), ord('z')+1):
        ch = chr(code)
        if ch in guessed and ch in secret: out.append(colorize(ch.upper(), C.GREEN))
        elif ch in guessed:                out.append(colorize(ch.upper(), C.RED))
        else:                              out.append(colorize(ch.upper(), C.GRAY))
    return " ".join(out)

def show_state(secret: str, guessed: set, total_lives: int, lives_left: int):
    """Clear the screen and display gallows, word, alphabet, and lives."""
    clear_screen()
    mistakes = total_lives - lives_left
    print(draw_gallows(mistakes))
    masked = " ".join([ch if ch in guessed else "_" for ch in secret])
    print("\n" + colorize("Word: ", C.BOLD) + colorize(masked, C.CYAN))
    print(colorize("Letters: ", C.BOLD) + alphabet_line(secret, guessed))
    heart_full, heart_empty = colorize("♥", C.RED), colorize("♡", C.GRAY)
    life_bar = heart_full * lives_left + heart_empty * (total_lives - lives_left)
    print(colorize(f"Lives: {lives_left}/{total_lives} ", C.BOLD) + life_bar + "\n")


# ----------------- Win / Lose sequences -----------------
def win_sequence(secret: str) -> bool:
    """Show a BIG 'YOU WIN!' green wave + box + fanfare."""
    banner = big_text_lines("YOU WIN!")
    animate_mono_wave(banner, base_color=C.GREEN, cycles=28, delay=0.045, span=10)
    print(colorize(WIN_BOX, C.GREEN))
    fanfare_win()
    time.sleep(0.25)
    return True

def lose_sequence(secret: str):
    """Show a BIG 'YOU LOSE' red wave + box + reveal the word + dirge."""
    banner = big_text_lines("YOU LOSE")
    animate_mono_wave(banner, base_color=C.RED, cycles=24, delay=0.060, span=10)
    print(colorize(LOSE_BOX, C.RED))
    print(colorize(f"The word was: {secret.upper()}", C.YELLOW))
    dirge_lose()
    time.sleep(0.25)


# ----------------- Intro that ALWAYS spells HANGMAN correctly -----------------
def intro_banner():
    """Render HANGMAN in the block font and animate it with a rainbow wave."""
    lines = big_text_lines("HANGMAN")              # build the big title with our safe block font
    width = term_width(80)                         # get terminal width
    if max(len(x) for x in lines) > width - 2:     # if it wouldn't fit, fall back to compact text
        animate_rainbow_banner(["HANGMAN"], cycles=10, delay=0.05)
    else:
        animate_rainbow_banner(lines, cycles=16, delay=0.04)


# ----------------- One full round -----------------
def play_one() -> bool:
    clear_screen()
    print(rainbow("WELCOME TO"))                   # compact rainbow (never wraps)
    intro_banner()                                  # big HANGMAN title (block font = no more HANIU)

    category = choose_category()
    total_lives = choose_difficulty()
    secret = pick_word(category)

    print(colorize(f"\nCategory: {category.title()} | Letters: {len(secret)}", C.CYAN))
    time.sleep(0.5)

    guessed, used_hint = set(), False
    lives_left = total_lives
    show_state(secret, guessed, total_lives, lives_left)

    while lives_left > 0:
        g = get_letter(guessed)

        if g == "hint":
            if used_hint:
                print(colorize("You already used your hint this game.", C.YELLOW)); beep_bad()
            else:
                letter = reveal_hint(secret, guessed)
                if letter:
                    guessed.add(letter); used_hint = True
                    print(colorize(f"Hint reveals: '{letter.upper()}'", C.MAGENTA)); beep_ok()
                else:
                    print(colorize("No hint available — all letters already revealed.", C.YELLOW)); beep_bad()
            time.sleep(0.6)
            show_state(secret, guessed, total_lives, lives_left)
            if all(ch in guessed for ch in secret):
                return win_sequence(secret)
            continue

        guessed.add(g)
        if g in secret:
            print(colorize(f"Nice! '{g.upper()}' is in the word.", C.GREEN)); beep_ok()
        else:
            lives_left -= 1
            print(colorize(f"Sorry — '{g.upper()}' is not in the word. Lives left: {lives_left}", C.RED)); beep_bad()

        time.sleep(0.5)
        show_state(secret, guessed, total_lives, lives_left)

        if all(ch in guessed for ch in secret):
            return win_sequence(secret)

    lose_sequence(secret)
    return False


# ----------------- Program entry (score + replay) -----------------
def main():
    score = 0
    games = 0
    while True:
        win = play_one()
        games += 1
        if win: score += 1
        print(colorize(f"\nScore: {score}/{games}", C.BOLD))
        again = input(colorize("\nPlay again? [Y/n]: ", C.CYAN)).strip().lower()
        if again == "n":
            break
    print(colorize("\nThanks for playing! Bye.", C.MAGENTA))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colorize("\nExiting. Goodbye!", C.YELLOW))
