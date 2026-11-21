#!/usr/bin/env python3
"""Discover the labs in this repository.

A lab is a folder labs/<id>/ (id like lab5, the same name the server uses for
`check_lab <id>`) containing lab.json:

    {"title": "Lab 5", "description": "Bash automation", "book": "Lab_Book.md"}

It may also contain hooks.py with either of these optional functions:

    prepare(root, ask_roll, config) -> Path   set up local/server files and
                                               return the folder to open
    local_hints(folder, config)               print ungraded Codespace hints
                                               before the server grades

Without hooks.py the lab is server-only: the terminal opens in lab-work/<id>/
and check_lab asks the server to grade ~/lab-work/<id>.
Adding a lab therefore needs no change to this kit.
"""
import importlib.util
import json
import re
import sys
from common import ROOT, plain_path

LABS = ROOT / 'labs'
LAB_RE = re.compile(r'(?:lab|mocktest|test)[0-9]{1,3}')


class Lab:
    def __init__(self, lab_id):
        if not LAB_RE.fullmatch(lab_id or ''):
            raise ValueError(f'Unknown lab {lab_id!r}. Available: {", ".join(available()) or "none"}.')
        self.id = lab_id
        self.path = plain_path(LABS / lab_id)
        meta = self.path / 'lab.json'
        if not meta.is_file():
            raise ValueError(f'Unknown lab {lab_id!r}. Available: {", ".join(available()) or "none"}.')
        data = json.loads(meta.read_text(encoding='utf-8'))
        self.title = data.get('title') or lab_id
        self.description = data.get('description', '')
        self.book = self.path / data.get('book', 'README.md')
        self.hooks = None
        if (self.path / 'hooks.py').is_file():
            spec = importlib.util.spec_from_file_location(f'{lab_id}_hooks', self.path / 'hooks.py')
            # Let a lab's hooks import its own helper modules (for example setup.py).
            sys.path.insert(0, str(self.path))
            self.hooks = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.hooks)

    def hook(self, name):
        return getattr(self.hooks, name, None) if self.hooks else None

    def label(self):
        return f'{self.id}  {self.title}' + (f' — {self.description}' if self.description else '')


def available():
    if not LABS.is_dir():
        return []
    found = [p.name for p in LABS.iterdir() if LAB_RE.fullmatch(p.name) and (p / 'lab.json').is_file()]
    return sorted(found, key=lambda name: (name.startswith('mocktest'), int(name.lstrip('abcdefghijklmnopqrstuvwxyz'))))


def choose(lab_id=None, ask=input):
    """Return the requested Lab, asking with a numbered list when none is given."""
    if lab_id:
        return Lab(lab_id)
    labs = [Lab(name) for name in available()]
    if not labs:
        raise ValueError('No labs found in this repository.')
    if len(labs) == 1:
        return labs[0]
    print('Available labs:')
    for number, lab in enumerate(labs, 1):
        print(f'  {number}. {lab.label()}')
    answer = ask(f'Which lab? (1-{len(labs)} or a name like {labs[-1].id}): ').strip()
    if answer.isdigit() and 1 <= int(answer) <= len(labs):
        return labs[int(answer) - 1]
    return Lab(answer)
