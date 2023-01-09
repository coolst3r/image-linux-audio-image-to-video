# image-linux-audio-image-to-video
converts images toghter with audio into video


To run this script, you will need to have Python 3 and the GTK+ 3 library installed on your system. You can check if you have these dependencies installed by running the following commands:

python3 --version
pkg-config --modversion gtk+-3.0

If you do not have these dependencies installed, you can install them using your system's package manager. For example, on Arch Linux, you can use the following command to install Python 3 and GTK+ 3:

sudo pacman -S python gtk3

On Debian, you can use the following command:

sudo apt-get install python3 python3-gi gir1.2-gtk-3.0

Once you have the dependencies installed, you can run the script by navigating to the directory where you saved the script and running the following command:

python3 add_audio_gui.py

To use this script, save it to a file (e.g. "install_requirements.sh"), make it executable using the chmod command, and then run it using ./install_requirements.sh.

chmod +x install_requirements.sh
./install_requirements.sh
