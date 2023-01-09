import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
import os

class AddAudioGUI:
    def __init__(self):
        # Create the main window
        self.window = Gtk.Window(title="Add Audio to Image")
        self.window.set_border_width(10)
        self.window.set_default_size(400, 200)

        # Create a vertical box to hold the image and audio widgets
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # Create a horizontal box to hold the image label and image file chooser button
        hbox_image = Gtk.Box(spacing=6)
        image_label = Gtk.Label("Image:")
        self.image_button = Gtk.FileChooserButton()
        self.image_button.set_title("Choose an image file")
        hbox_image.pack_start(image_label, False, False, 0)
        hbox_image.pack_start(self.image_button, True, True, 0)

        # Create a horizontal box to hold the audio label and audio file chooser button
        hbox_audio = Gtk.Box(spacing=6)
        audio_label = Gtk.Label("Audio:")
        self.audio_button = Gtk.FileChooserButton()
        self.audio_button.set_title("Choose an audio file")
        hbox_audio.pack_start(audio_label, False, False, 0)
        hbox_audio.pack_start(self.audio_button, True, True, 0)

        # Create a horizontal box to hold the output label and output file chooser button
        hbox_output = Gtk.Box(spacing=6)
        output_label = Gtk.Label("Output:")
        self.output_button = Gtk.FileChooserButton()
        self.output_button.set_title("Choose an output file")
		
		# Create a horizontal box to hold the audio label and audio file chooser button
        hbox_audio = Gtk.Box(spacing=6)
        audio_label = Gtk.Label("Audio:")
        self.audio_button = Gtk.FileChooserButton()
        self.audio_button.set_title("Choose an audio file")
        hbox_audio.pack_start(audio_label, False, False, 0)
        hbox_audio.pack_start(self.audio_button, True, True, 0)

        # Create a horizontal box to hold the output label and output file chooser button
        hbox_output = Gtk.Box(spacing=6)
        output_label = Gtk.Label("Output:")
        self.output_button = Gtk.FileChooserButton()
        self.output_button.set_title("Choose an output file")
        self.output_button.set_current_name("output.mp4")
        hbox_output.pack_start(output_label, False, False, 0)
        hbox_output.pack_start(self.output_button, True, True, 0)

        # Create a horizontal box to hold the create video button
        hbox_create = Gtk.Box(spacing=6)
        create_button = Gtk.Button.new_with_label("Create Video")
        create_button.connect("clicked", self.on_create_clicked)
        hbox_create.pack_start(create_button, True, True, 0)

        # Create a horizontal box to hold the progress bar
        hbox_progress = Gtk.Box(spacing=6)
        self.progress_bar = Gtk.ProgressBar()
        hbox_progress.pack_start(self.progress_bar, True, True, 0)

        # Add the image, audio, and output boxes to the main vertical box
        vbox.pack_start(hbox_image, True, True, 0)
        vbox.pack_start(hbox_audio, True, True, 0)
        vbox.pack_start(hbox_output, True, True, 0)
        vbox.pack_start(hbox_create, True, True, 0)
        vbox.pack_start(hbox_progress, True, True, 0)

        # Add the vertical box to the main window
        self.window.add(vbox)

    def on_create_clicked(self, widget):
        # Get the image and audio file names from the file chooser buttons
        image_file = self.image_button.get_filename()
        audio_file = self.audio_button.get_filename()
        output_file = self.output_button.get_filename()

        # Check if the input files exist
        if not os.path.exists(image_file):
            self.show_error_message("Image file not found")
            return
        if not os.path.exists(audio_file):
            self.show_error_message("Audio file not found")
            return

        # Check if the output file can be written
        try:
            open(output_file, "w").close()
        except:
            self.show_error_message("Unable to write to output file")
            return

        # Use ffmpeg to combine the image and audio into a video
        command = (f"ffmpeg -loop 1 -i {image_file} -i {audio_file} "
                   f"-c:v libx264 -tune stillimage -c:a aac -b:a 192k "
                   f"-pix_fmt yuv420p -shortest {output_file}")
        self.run_ffmpeg(command)

    def run_ffmpeg(self, command):
        # Run the ffmpeg command and update the progress bar
        self.progress
        # Run the ffmpeg command and update the progress bar
        self.progress_bar.set_fraction(0.0)
        self.window.set_sensitive(False)
        self.ffmpeg_command = os.popen(command)
        self.timeout_id = GObject.timeout_add(100, self.update_progress_bar)

    def update_progress_bar(self):
        # Update the progress bar based on the output of the ffmpeg command
        try:
            line = self.ffmpeg_command.readline()
        except:
            # ffmpeg has finished
            self.window.set_sensitive(True)
            self.ffmpeg_command = None
            self.timeout_id = None
            self.progress_bar.set_fraction(1.0)
            self.show_message_dialog("Video Created", "The video has been created and saved to the specified file.")
            return False

        if not line:
            # ffmpeg is still running
            return True

        # Parse the output of ffmpeg to get the progress
        if "time=" in line:
            try:
                time = line.split("time=")[1].split(" ")[0]
                hours, minutes, seconds = map(float, time.split(":"))
                                duration = 3600 * hours + 60 * minutes + seconds
                self.progress_bar.set_fraction(duration / 100.0)
            except:
                pass

        return True

    def show_error_message(self, message):
        # Display an error message dialog
        message_dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Error")
        message_dialog.format_secondary_text(message)
        message_dialog.run()
        message_dialog.destroy()

    def show_message_dialog(self, title, message):
        # Display a message dialog
        message_dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, title)
        message_dialog.format_secondary_text(message)
        message_dialog.run()
        message_dialog.destroy()

def main():
    AddAudioGUI()
    Gtk.main()

if __name__ == "__main__":
    main()

