#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &>/dev/null; then
    # Install Python 3
    sudo pacman -S python
fi

# Check if GTK+ 3 is installed
if ! pkg-config --exists gtk+-3.0; then
    # Install GTK+ 3
    sudo pacman -S gtk3
fi
