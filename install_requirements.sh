#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &>/dev/null; then
    # Install Python 3
    sudo apt-get install python3
fi

# Check if GTK+ 3 is installed
if ! pkg-config --exists gtk+-3.0; then
    # Install GTK+ 3
    sudo apt-get install python3-gi gir1.2-gtk-3.0
fi
