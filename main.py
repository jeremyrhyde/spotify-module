# main.py

import yaml
import time
from spotify_player.spotify import Spotify

playlist_id = "2bpNUD5gCPCoYd0Spo3GGB"
volume = 70

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    spotify_cfg = config["spotify"]

    print("Starting connection to spotify...")
    sp = Spotify(
        client_id=spotify_cfg["client_id"],
        client_secret=spotify_cfg["client_secret"],
        redirect_uri=spotify_cfg["redirect_uri"],
        device_id=spotify_cfg["device_id"]
    )
    
    sp.set_volume(50)
    
    print("Getting track URIs...")
    uris = sp.get_track_uris(playlist_id)
    sp.list_devices()
    sp.play_on_device(uris)
    
    try:
        sp.gradually_increase_volume(increment=1, delay=10)
    except KeyboardInterrupt:
        sp.stop_playback_on_exit()  # Handle ctrl+C gracefully
    
if __name__ == "__main__":
    main()
