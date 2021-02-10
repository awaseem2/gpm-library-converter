# Google Play Music Library Converter

![icon](icon.png)

## Description

This is a tool that can be used to convert your Google Play Music library into 1 Spotify playlist.

## What is a Google Play Music library, and how can I download mine?

The Google Play Music (GPM) library was an awesome feature that let you add songs individually to your personal collection, without needing to be saved to playlists. 

[You can download your GPM library through Google Takout by using this link](https://takeout.google.com/settings/takeout/custom/play_music?gar=1). (This link should also be in your email from Google.)

**Important: You can only download your GPM library until February 24, 2021.
After that, your GPM Library will be deleted, and you will be unable to download it.**

## Prerequisites

In order to run this program, you must have:
- [Python 3.4+](https://www.python.org/downloads/)
- [Spotipy](https://spotipy.readthedocs.io/en/2.16.1/?highlight=spotify#installation) (Run `pip install spotipy --upgrade` to install)

## Instructions

1. Clone this repository and cd into the directory
    `git clone https://github.com/awaseem2/gpm-library-converter.git`
    `cd gpm-library-converter`

1. Download and unzip [your GPM library](https://takeout.google.com/settings/takeout/custom/play_music?gar=1)

2. Navigate to the [Spotify Developers Dashboard](https://developer.spotify.com/dashboard/applications)
    - click `Create an App`
    - Provide a name and description, and check the boxes
    - click `Show Client Secret`

3. Set your environment variables
    On the Spotify app page, you will see a Client ID hash and a Client Secret hash.
    - On Windows Powershell:
        `$env:SPOTIPY_CLIENT_ID='your_client_id_hash'`
        `$env:SPOTIPY_CLIENT_SECRET='your_client_secret_hash'`

    - On Mac:
        `export SPOTIPY_CLIENT_ID='your_client_id_hash'`
        `export SPOTIPY_CLIENT_SECRET='your_client_secret_hash'`

4. Run main.py
    `python main.py`

5. Enter 1 to consolidate your GPM Library files into 1 CSV

6. Enter the path to the directory the files are in
    - For me, this looked something like 
    `C:\Users\username\Downloads\takeout-20210209T095055Z-001\Takeout\Google Play Music\Tracks`

7. Once this is complete, I recommend noting any songs that failed to work.
Next, enter 2

8. Type "default"

9. Wait until it finishes. Note any songs that failed. ctrl-c or type "Quit" to exit the program.

## Disclaimer

This program will probably not be helpful if you have a lot of songs that contain non-English letters.

## I didn't use Google Play Music, can I still use your program?

Sure, it can be used more generally as well. The program has two components:
1. Combining many Google Play Music CSV files into 1 CSV file
2. Converting a CSV file into a spotify playlist

Option (2) can be used for any CSV file that has Title, Artist, and Album columns (in any order).
If you would like to convert a CSV file of any size into a Spotify playlist, you can definitely
accomplish that using this program.