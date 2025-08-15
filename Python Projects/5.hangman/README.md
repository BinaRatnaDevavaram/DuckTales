# Hangman — Color + Sound + Animated Banners (Terminal)

A playful terminal Hangman with:

- 🌈 Rainbow intro (animated wave)
- 🟩 Big **YOU WIN!** (green shimmer) / 🟥 **YOU LOSE** (red shimmer)
- 🎶 Sound effects (Windows `winsound` or terminal bell elsewhere)
- 🎨 Colored gallows, alphabet guide, and heart‑based lives
- 🧠 Categories, difficulty levels, and a one‑time hint

---

## ✨ Features

- **Cross‑platform color:** ANSI sequences auto‑enabled on Windows 10+.
- **Clean animations:** Uses in‑place redraw for smooth waves.
- **Readable everywhere:** Banners use a Unicode block font (no slashes to get mangled by fonts).
- **Beginner‑friendly:** Clear structure and functions with comments.

---

## 📦 Requirements

- **Python 3.9+** (works on 3.8+ in most cases; 3.9+ recommended)
- No third‑party packages required.
- Windows only: `winsound` is part of the standard library; other platforms will use the terminal bell (`\a`).
- No `requirements.txt` — it’s intentionally left out.

---

## 🚀 Run

```bash
python hangman_fun.py

If you have multiple Python versions:
python3 hangman_fun.py
```

---

## 🕹️ How to Play

- Pick a category and difficulty (lives).
- Guess letters a–z.
- Type hint once per game to reveal a letter.
- Win by revealing the whole word before running out of lives.

---

## 🔧 Customization

- Open hangman_fun.py and tweak:
- Words: edit the WORDS dict.
- Lives per difficulty: edit DIFFICULTY.
- Animation speed: adjust delay/cycles in:
        animate_rainbow_banner(...)
        animate_mono_wave(...)
- Colors: change color constants in class C.
- Gallows stages: edit the ASCII in STAGES.

---

## 🔊 Sound Notes

- Windows: uses winsound.Beep() for tones.
- If you don’t hear anything, your terminal may have the bell disabled.

---

## 🖥️ Terminal Tips / Troubleshooting

- If the intro banner wraps (letters break or look squashed):
- Widen your terminal window.
- The game auto‑checks width and will fall back to a compact title if needed.
- Windows colors not showing:
        > You must be on Windows 10+ and using Windows Terminal or a modern PowerShell/Command Prompt.
        > The code calls _enable_ansi_on_windows() automatically; most setups need nothing else.
- Font issues:
        > Use a monospaced font that renders Unicode block characters cleanly (e.g., Cascadia Mono, Consolas, Menlo, JetBrains Mono).

---

## 🧩 Code Map (What does what?)

- Color & ANSI setup: C, _enable_ansi_on_windows(), colorize()
- Rainbow text: rainbow(), rainbow_wave(), animate_rainbow_banner()
- Single‑color shimmer: _mono_wave(), animate_mono_wave()
- Screen & width: clear_screen(), term_width()
- Sounds: beep_ok(), beep_bad(), fanfare_win(), dirge_lose()
- ASCII gallows: STAGES, draw_gallows()
- Block‑font banners: _FONT, big_text_lines()
- Game I/O: choose_category(), choose_difficulty(), get_letter(), reveal_hint()
- Rendering state: alphabet_line(), show_state()
- Win/Lose sequences: win_sequence(), lose_sequence()
- Intro: intro_banner()
- Game flow: play_one(), main()

---

## ✅ Tested On

- Windows 11 + Windows Terminal

---

## 📄 License

MIT. Do whatever you like; attribution appreciated.

---
