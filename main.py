# main.py

import yaml
from spotify_player.spotify import Spotify
from spotify_player.audio import Audio

playlist_id = ""

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    spotify_cfg = config["spotify"]
    audio_cfg = config["audio"]

    sp = Spotify(
        client_id=spotify_cfg["client_id"],
        client_secret=spotify_cfg["client_secret"],
        redirect_uri=spotify_cfg["redirect_uri"]
    )

    audio = Audio(volume=audio_cfg.get("volume", 50))

    uris = sp.get_track_uris(playlist_id)
    for uri in uris:
        audio.play_uri(uri)

if __name__ == "__main__":
    main()
