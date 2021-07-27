import audio_metadata
import shutil
import os
from termcolor import colored

print("\n" + colored('''   mm              #    "                   mmmm                  m   
   ##   m   m   mmm#  mmm     mmm          #"   "  mmm    m mm  mm#mm 
  #  #  #   #  #" "#    #    #" "#         "#mmm  #" "#   #"  "   #   
  #mm#  #   #  #   #    #    #   #             "# #   #   #       #   
 #    # "mm"#  "#m##  mm#mm  "#m#"         "mmm#" "#m#"   #       "mm ''', 'blue'))

print(colored("\n Made by MaxOmenes \n", "blue"))



def meta(song_name, source):                                        #Uses for read metadata from track
    metadata = audio_metadata.load(source +'\\'+ song_name)

    artist_name = str(metadata.tags.artist)
    album_name = str(metadata.tags.album)
    date = str(metadata.tags.date)

    artist_name = artist_name.replace('\'', '')
    artist_name = artist_name.replace('[', '')
    artist_name = artist_name.replace(']', '')

    album_name = album_name.replace('[', '')
    album_name = album_name.replace(']', '')
    album_name = album_name.replace('\'', '')

    date = date.replace('\'', '')

    return artist_name, album_name, date

def replicant(song_name, source, destination):              #Copy file from one destination, to another
    artist_name, album, date = meta(song_name, source)

    album = album + ' ' + date

    source = source +'\\'+ song_name
    
    destination = destination + "\\" + artist_name + "\\" + album
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)
        shutil.copy(source, destination)
        print(artist_name, '-', song_name, 'copied successfully!')
    except:
        print(artist_name, '-', song_name, colored('denied!', 'red'))

from_source = str(input('Select source: '))
to_source = str(input('Select destination: '))

file_list = os.listdir(from_source)

for song_name in file_list:
    replicant(song_name, from_source, to_source)


