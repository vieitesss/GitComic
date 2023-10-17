#!/bin/bash

SCRIPT_DIRNAME=$(dirname $(realpath "$0"))

icons_file="$SCRIPT_DIRNAME/icons.txt"
session="$(tmux list-sessions | grep attached | sed 's/:.*//')"
window="$(tmux list-windows | grep active | sed 's/:.*//')"
pane="$(tmux list-panes | grep active | sed 's/:.*//')"
current_pane=${session}:${window}.${pane}

if [[ -z $1 ]]; then
    tmux neww "cat $icons_file | fzf\
        --bind 'enter:become(tmux send-keys -t $current_pane {s1})'"
fi

