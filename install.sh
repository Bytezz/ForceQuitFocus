#!/bin/bash

filename="forcequitfocus.py"
name="forcequitfocus"
rootpath="/usr/local/bin/"
userpath="$HOME/.local/bin/"

if [ "$UID" == "0" ]; then
	ipath="$rootpath"
else
	ipath="$userpath"
fi

if [ "$1" == "-u" ]; then
	set -x
	rm -f "$ipath$name"
else
	set -x
	mkdir -p "$ipath"
	cp "$filename" "$ipath$name"
fi
