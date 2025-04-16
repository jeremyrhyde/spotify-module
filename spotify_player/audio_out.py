import subprocess

class AudioOut:
    def __init__(self, volume=50):
        self.volume = volume

    def play_uri(self, uri):
        # Use Spotify URI with mpv and spotify-dl or stream preview_url
        cmd = ["mpv", f"spotify:{uri}", f"--volume={self.volume}"]
        subprocess.run(cmd)
