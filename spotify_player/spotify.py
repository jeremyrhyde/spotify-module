# spotify_player/spotify.py
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spotify:
    def __init__(self, client_id, client_secret, redirect_uri, device_id):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri="https://192.168.1.8:8888/callback",
            scope="user-read-playback-state user-modify-playback-state"
        ))

        self.device_id = device_id
        
        # Check if the authentication is successful
        try:
            user_info = self.sp.current_user()
            print("Authenticated as:", user_info['id'])
        except Exception as e:
            print("Error during authentication:", e)

    def get_track_uris(self, playlist_id):
        try:
            # Fetch the playlist tracks
            playlist = self.sp.playlist_tracks(playlist_id)
            
            # Debugging: print the raw playlist response
            #print("Full Playlist Response:", playlist)
            
            # Extract the tracks
            tracks = playlist['items']
            print(f"Found {len(tracks)} tracks in the playlist.")
            
            uris = [item['track']['uri'] for item in tracks if item['track']['uri']]
            print("Track URIs:", uris)
            
            return uris
        
        except Exception as e:
            print("Error fetching playlist:", e)
            return []
        
    def start_playback(self, uris):
        # Get available devices
        devices = self.sp.devices()

        # Check if there are active devices
        if len(devices['devices']) == 0:
            print("No active devices found. Please make sure Spotify is playing on a device.")
            return
        
        self.list_devices()

        # Get the ID of the first active device
        device_id = devices['devices'][0]['id']
        print(f"Using device: {device_id}")

        # Start playback on the device
        try:
            self.sp.start_playback(device_id=device_id, uris=uris)
            print(f"Playing track(s) on device: {device_id}")
        except Exception as e:
            print(f"Error starting playback: {e}")
          
    def list_devices(self):
        """List all active devices."""
        devices = self.sp.devices()
        if devices['devices']:
            print("Available devices:")
            for device in devices['devices']:
                print(f"Device Name: {device['name']}, ID: {device['id']}")
        else:
            print("No active devices found.")          
            
    def play_on_device(self, uris):
        print(self.device_id)
        """Play the given URI on the hardcoded device."""
        try:
            self.sp.start_playback(device_id=self.device_id, uris=uris)
            print(f"Playing track(s) on device: {self.device_id}")
        except Exception as e:
            print(f"Error starting playback: {e}")

    def set_volume(self, volume):
        """Set the volume for the active device."""
        try:
            # Volume must be between 0 and 100
            if 0 <= volume <= 100:
                self.sp.volume(volume, device_id=self.device_id)
                print(f"Volume set to {volume}% on device with ID: {self.device_id}")
            else:
                print("Volume must be between 0 and 100.")
        except Exception as e:
            print(f"Error setting volume: {e}")

    def stop_playback_on_exit(self):
        """Handler to stop playback when the program exits."""
        print("Stopping playback before exit...")
        self.sp.pause_playback()
        
    def gradually_increase_volume(self, min_volume=50, max_volume=100, increment=5, delay=1):
        """Gradually increase the volume while the track is playing."""
        current_volume = min_volume
        while current_volume < max_volume:
            self.set_volume(current_volume)
            current_volume += increment
            time.sleep(delay)  # Adjust delay for how fast the volume increases
            if current_volume > max_volume:
                current_volume = max_volume
            print(f"Increasing volume to {current_volume}%")