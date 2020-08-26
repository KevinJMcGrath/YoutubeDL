import csv
import logging

from pytube import YouTube
import os

rootPath = os.path.abspath("E:\Dropbox\Development\Python\YoutubeDL")

# testURL = 'https://www.youtube.com/watch?v=VV1XWJN3nJo'

# YouTube(testURL).streams.first().download()

_consolelog = logging.getLogger('console')
_consolelog.setLevel(logging.DEBUG)

_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

# Not Needed to log output to console
# Create stream handler to display console output
# _consoleStreamHandler = logging.StreamHandler()
# _consoleStreamHandler.setLevel(logging.DEBUG)
# _consoleStreamHandler.setFormatter(_formatter)

# _consolelog.addHandler(_consoleStreamHandler)


with open('songs.csv') as csvFile:
    reader = csv.DictReader(csvFile)

    for i, row in enumerate(reader):

        if row['Downloaded'] != 'Y':
            url = row['YoutubeURL']
            artist = row['Artist']
            title = row['Title']
            newName = artist + ' - ' + title

            _consolelog.info('Downloading ' + newName + '...')

            yt = YouTube(url)

            _consolelog.info('Grabbing streams...')

            downloadPath = os.path.join(rootPath, 'Audio')

            _consolelog.info(downloadPath)

            if len(yt.streams.filter(only_audio=True, subtype='mp4').all()) > 0:
                firstStream = yt.streams.filter(only_audio=True, subtype='mp4').first()

                defaultName = firstStream.default_filename
                # _consolelog.info(defaultName)

                firstStream.download(downloadPath)

                oldPath = os.path.join(downloadPath, defaultName)
                newPath = os.path.join(downloadPath, newName + '.mp4')

                _consolelog.info(oldPath)
                _consolelog.info(newPath)

                os.rename(oldPath, newPath)

                row['Downloaded'] = 'Y'

            # if i > 2:
                # break

