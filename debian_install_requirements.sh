#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &>/dev/null; then
    # Install Python 3
    sudo apt-get install python3
fi

# Check if pip is installed
if ! command -v pip &>/dev/null; then
    # Install pip
    sudo apt-get install python3-pip
fi

# Install the ffmpeg-python package
pip install ffmpeg-python

# Check if ffmpeg is installed
if ! command -v ffmpeg &>/dev/null; then
    # Install ffmpeg
    sudo apt-get install ffmpeg
fi
