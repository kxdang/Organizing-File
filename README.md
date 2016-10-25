<content>
# File Organizer
My first python script I wrote to clean up Downloads folder after reading "Automate the Boring Stuff with Python" by Al Sweigart
## Installation
Windows OS only.
Requires python and PyInstaller with the line "pyinstaller –onefile OrganizingFiles.py" 
It creates a one-file bundled executable for you to schedule the program via Windows Scheduler
## Usage
You can edit the OrganizingFiles.py code using a text editor

For creating a new desired folder you must define what the folder would be


e.g To make a music folder

new_path_*music* = os.getcwd() + "\Music"

The under the Organizing functions, follow the format

if obj.endswith('*.mp3*','*.mp4*'):
        mover(obj, new_path_*music*)
        
You can specify which file type you want to move, in this case, we have chosen .mp3 and .mp4 file extensions, so the File Organizer script will run looking for any files with these extensions and then move them to the new_path_music we specified which is the folder it makes or if the folder is there it will send it to that folder.

## Bugs
 * Will not move files if the file already exists in there and eventually stops the entire program - Will find a fix soon
## Credits (Debuggers)
 * Tommy Tran
 * Adrian Lee
 * Kelvin Kong
## License
 - Feel free to use and distribute.
]]></content>
  <tabTrigger>readme</tabTrigger>

