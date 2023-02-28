import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

playlistLeo = "spotify:playlist:5Y5kiYaST9xJvOBi67kfbC"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="dd6c0415a2fc43778cdccf91a82de87a",client_secret="5c46b6d01fb64ad7a41209d9f025a292",redirect_uri="http://127.0.0.1:9090",scope="user-library-read playlist-read-private user-modify-playback-state user-read-playback-state"))



def getAvailableDevice():
    devices = sp.devices()["devices"]
    if len(devices) > 0:
        return devices[0]["id"]
    else:
        return None

device_id = getAvailableDevice()

def playPlaylist(playlist):
    if device_id is not None:
        sp.volume(100, device_id=device_id)
        sp.start_playback(context_uri=playlist, device_id=device_id)
    else:
        print("No active devices found.")

def stopMusic():
    sp.pause_playback()

def resumeMusic():
    sp.start_playback()

def changeVolume(volume):
    if device_id is not None:
        sp.volume(volume, device_id=device_id)
    else:
        print("No active devices found.")
