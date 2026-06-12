import re
import random
import sys
from pathlib import Path


OPTION_LETTER = re.compile(r'^([A-Z])\) (.+)$')


def parse_option_block(lines):
    """Parse consecutive option lines into [(letter, text), ...]. Returns None on failure."""
    options = []
    for line in lines:
        m = OPTION_LETTER.match(line)
        if not m:
            return None
        options.append((m.group(1), m.group(2)))
    return options


def shuffle_file(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')

    # Split on the ## Answers section header
    split_m = re.search(r'^## Answers[ \t]*$', text, re.MULTILINE)
    if not split_m:
        print(f"LINT {path}: missing '## Answers' section")
        return False

    questions_text = text[:split_m.start()]
    answers_text = text[split_m.start():]

    # --- Parse question blocks ---
    # Each block: #### N. heading line, then option lines until blank/non-option line
    q_block_re = re.compile(
        r'^(#### \d+\..+\n)((?:[A-Z]\) .+\n)+)',
        re.MULTILINE
    )
    # --- Parse answer blocks ---
    # Each block: #### N. heading, option lines with ✓/✗, blank line, **Correct:** line
    a_block_re = re.compile(
        r'^(#### \d+\..+\n)((?:[A-Z]\) .+\n)+)\n(\*\*Correct:\*\*.+)',
        re.MULTILINE
    )

    q_matches = list(q_block_re.finditer(questions_text))
    a_matches = list(a_block_re.finditer(answers_text))

    if not q_matches:
        print(f"LINT {path}: no question option blocks found")
        return False
    if not a_matches:
        print(f"LINT {path}: no answer blocks found")
        return False
    if len(q_matches) != len(a_matches):
        print(f"LINT {path}: {len(q_matches)} question blocks but {len(a_matches)} answer blocks")
        return False

    # Collect replacements (applied in reverse so offsets stay valid)
    q_replacements = []  # (start, end, new_text)
    a_replacements = []  # list of (start, end, new_text) sorted descending by start

    for i, (qm, am) in enumerate(zip(q_matches, a_matches), 1):
        q_opts_raw = qm.group(2).splitlines(keepends=True)
        a_opts_raw = am.group(2).splitlines(keepends=True)

        q_opts = parse_option_block([l.rstrip('\n') for l in q_opts_raw])
        a_opts = parse_option_block([l.rstrip('\n') for l in a_opts_raw])

        if q_opts is None or a_opts is None:
            print(f"LINT {path}: Q{i} option lines don't match expected format")
            return False
        if len(q_opts) != len(a_opts):
            print(f"LINT {path}: Q{i} has {len(q_opts)} question options but {len(a_opts)} answer options")
            return False

        # Verify letters align
        q_letters = [o[0] for o in q_opts]
        a_letters = [o[0] for o in a_opts]
        if q_letters != a_letters:
            print(f"LINT {path}: Q{i} option letters don't match between sections: {q_letters} vs {a_letters}")
            return False

        correct_line = am.group(3)  # e.g. "**Correct:** B, D"
        correct_m = re.search(r'\*\*Correct:\*\*\s*(.+)', correct_line)
        if not correct_m:
            print(f"LINT {path}: Q{i} can't parse **Correct:** line")
            return False
        correct_letters = set(re.findall(r'[A-Z]', correct_m.group(1)))

        # Shuffle
        n = len(q_opts)
        perm = list(range(n))
        random.shuffle(perm)

        new_q_opts = ''
        new_a_opts = ''
        new_correct = []

        for new_pos, old_pos in enumerate(perm):
            new_letter = q_letters[new_pos]  # keep A/B/C/D labels in order
            old_letter = q_letters[old_pos]

            # Preserve original line endings
            new_q_opts += f"{new_letter}) {q_opts[old_pos][1].rstrip()}  \n"
            new_a_opts += f"{new_letter}) {a_opts[old_pos][1].rstrip()}  \n"

            if old_letter in correct_letters:
                new_correct.append(new_letter)

        new_correct.sort()
        new_correct_str = f"**Correct:** {', '.join(new_correct)}"

        q_replacements.append((qm.start(2), qm.end(2), new_q_opts))
        # Two replacements in answers: options block and correct line (correct line has higher offset)
        a_replacements.append((am.start(3), am.end(3), new_correct_str))
        a_replacements.append((am.start(2), am.end(2), new_a_opts))

    # Apply all replacements in descending offset order so earlier offsets stay valid
    new_questions_text = _apply_replacements(questions_text, sorted(q_replacements, key=lambda x: x[0], reverse=True))
    new_answers_text = _apply_replacements(answers_text, sorted(a_replacements, key=lambda x: x[0], reverse=True))

    path.write_text(new_questions_text + new_answers_text, encoding='utf-8')
    return True


def _apply_replacements(text, replacements):
    for start, end, new_text in replacements:
        text = text[:start] + new_text + text[end:]
    return text


def main():
    if len(sys.argv) < 2:
        # Default: all quiz files in repo
        roots = [Path('.')]
        files = []
        for root in roots:
            files.extend(root.rglob('quiz*/*.md'))
    else:
        files = [Path(p) for p in sys.argv[1:]]

    ok = 0
    fail = 0
    for f in sorted(files):
        if shuffle_file(f):
            # print(f"OK  {f}") # don't print to surface errors cleanly
            ok += 1
        else:
            fail += 1

    print(f"\n{ok} shuffled, {fail} skipped due to lint errors.")


if __name__ == '__main__':
    main()
