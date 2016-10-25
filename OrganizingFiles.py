import shutil
import os

# Creating new folders for organizing
new_path_torrent = os.getcwd() + "\Torrent Files"
new_path_pictures = os.getcwd() + "\Downloaded Pictures"
new_path_music = os.getcwd() + "\Music"
new_path_folders_movie = os.getcwd() + "\Movies"
new_path_programs = os.getcwd() + "\Downloaded Programs and Games"
new_path_folders_files = os.getcwd() + "\Files"
new_path_documents = os.getcwd() + "\Downloaded Documents"

# Check if folders exists, if not then make them
if not os.path.exists(new_path_torrent):
    os.makedirs(new_path_torrent)

if not os.path.exists(new_path_pictures):
    os.makedirs(new_path_pictures)

if not os.path.exists(new_path_music):
    os.makedirs(new_path_music)

if not os.path.exists(new_path_folders_movie):
    os.makedirs(new_path_folders_movie)

if not os.path.exists(new_path_programs):
    os.makedirs(new_path_programs)

if not os.path.exists(new_path_folders_files):
    os.makedirs(new_path_folders_files)

if not os.path.exists(new_path_documents):
    os.makedirs(new_path_documents)
# Make list of directories to compare
important_folders = ('Torrent Files',
                     'Downloaded Pictures',
                     'Music',
                     'Movies',
                     'Downloaded Programs and Games',
                     'Files',
                     'Downloaded Documents')

# Check for video files inside video

def mover(obj, path):
    shutil.move((os.path.join(os.getcwd(), obj)), path)
    print("Moving", obj, "to", path)
# Organizing functions
# if file is a torrent file, move to the Torrent Files folder
for obj in os.listdir():
    if obj.endswith('.torrent'):
        mover(obj, new_path_torrent)
    if obj.endswith(('.mp3', '.mp4')):
        mover(obj, new_path_music)
    if obj.endswith(('.jpeg', '.jpg', '.png')):
        mover(obj, new_path_pictures)
    if obj.endswith(('.exe', '.msi')):
        mover(obj, new_path_programs)
    if obj.endswith(('.pdf', '.docx', '.pptx', '.ppt', '.doc')):
        mover(obj, new_path_documents)
    if obj.endswith(('.avi', '.mkv')):
        mover(obj, new_path_documents)
    if obj.endswith(('.rar','.zip')):
    	mover(obj, new_path_folders_files)
    if ((os.path.isdir(obj)) and (not (obj in important_folders))):
        # set flag
        video_inside = False
        # check if we should set flag = true
        for videos in os.listdir(os.path.join(os.getcwd(), obj)):
            if videos.endswith(('.mkv', '.avi', '.mp4', '.mov')):
                video_inside = True
                break
        # actually move
        if video_inside == True:
            mover(obj, new_path_folders_movie)
        else:
            mover(obj, new_path_folders_files)
print('Finished Organizing')


