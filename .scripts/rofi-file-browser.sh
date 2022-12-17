#!/bin/bash
alacritty -e nvim "$(rg --no-messages --files ~/Zettelkasten \
    | rofi -threads 0 \
    -dmenu -sort -sorting-method fzf -i -p "find")"
