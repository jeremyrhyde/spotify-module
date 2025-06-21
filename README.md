# Spotify Controller

A cross-platform Spotify automation tool that works on Raspberry Pi, macOS, and Linux. Control Spotify playback with playlist search by name, volume ramping, and interactive terminal interface.

## Features

- 🎵 **Playlist Search by Name** - No more hard-coded playlist IDs
- 🖥️ **Cross-Platform** - Works on Raspberry Pi, macOS, and Linux
- 🎛️ **Interactive CLI** - Real-time control with pause, resume, volume, skip
- 📈 **Volume Ramping** - Gradual volume increase over time
- 🤖 **Background Operation** - Runs headlessly with spotifyd
- 📝 **Comprehensive Logging** - Detailed logs for troubleshooting
- 🔧 **Auto-Installation** - Automatically downloads and configures spotifyd

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd spotify-module

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy the example configuration
cp config.yaml.example config.yaml

# Edit with your Spotify credentials
nano config.yaml
```

You'll need to create a Spotify app at https://developer.spotify.com/dashboard to get your `client_id` and `client_secret`.

### 3. Usage

#### Interactive Mode (Recommended)
```bash
python cli.py
```

Then type a playlist name to search and play:
```
> chill vibes
> pause
> v 80
> resume
```

#### Legacy Mode
```bash
python main.py
```

## Configuration

The `config.yaml` file controls all aspects of the application:

```yaml
spotify:
  client_id: "your_client_id"
  client_secret: "your_client_secret"
  redirect_uri: "http://localhost:8888/callback"

device_name: "SpotifyBot"

automation:
  volume_ramp: true
  start_volume: 10
  end_volume: 80
  ramp_duration: 300  # 5 minutes
```

## Interactive Commands

When using `cli.py`, you have these commands available:

- `[p]ause` - Pause playback
- `[r]esume` - Resume playback  
- `[s]top` - Stop playback
- `[v] <num>` - Set volume (0-100)
- `[n]ext` - Skip to next track
- `[b]ack` - Go to previous track
- `[i]nfo` - Show current track info
- `[st]atus` - Show playback status
- `[h]elp` - Show help
- `[q]uit` - Quit application
- `<playlist name>` - Search and play new playlist

## Architecture

The application is built with a modular architecture:

- **PlatformDetector** - Detects OS, architecture, and audio systems
- **DeviceManager** - Handles spotifyd installation and lifecycle
- **PlaylistManager** - Searches and manages playlists
- **PlaybackController** - Controls playback, volume, and background operations

## Platform Support

### Raspberry Pi
- Automatically detects Pi hardware
- Optimized settings (lower bitrate, specific audio config)
- Compatible with existing Pi setups

### macOS
- Uses CoreAudio backend
- Supports both Intel and Apple Silicon
- Auto-downloads appropriate spotifyd binary

### Linux
- Supports ALSA and PulseAudio
- Works on x86_64 and ARM64
- Headless operation friendly

## Logging

Logs are automatically created in the `logs/` directory:
- `device_manager.log` - spotifyd installation and management
- `playlist_manager.log` - Playlist search and retrieval
- `playback_controller.log` - Playback control and volume management
- `spotify_cli.log` - Interactive CLI operations

## Troubleshooting

### Device Not Found
```bash
# Check if spotifyd is running
ps aux | grep spotifyd

# Restart the device manager
python -c "from spotify_controller import DeviceManager, PlatformDetector; dm = DeviceManager(PlatformDetector()); dm.restart_spotifyd()"
```

### Authentication Issues
- Ensure your Spotify app has the correct redirect URI
- Check that your client_id and client_secret are correct
- Try deleting `.cache` files and re-authenticating

### Audio Issues
- On Linux: Install `alsa-utils` or `pulseaudio`
- On macOS: Ensure system audio is working
- Check logs for audio backend errors

## Migration from v1.x

If you're upgrading from the original version:

1. Your existing `config.yaml` will mostly work
2. The old `main.py` has been refactored but maintains compatibility
3. New features are available through `cli.py`
4. Logs are now in the `logs/` directory instead of console output

## Development

### Project Structure
```
spotify-module/
├── spotify_controller/          # Main package
│   ├── platform_detector.py    # Platform detection
│   ├── device_manager.py        # spotifyd management  
│   ├── playlist_manager.py      # Playlist operations
│   ├── playback_controller.py   # Playback control
│   └── logger.py               # Logging utilities
├── cli.py                      # Interactive interface
├── main.py                     # Legacy interface
└── config.yaml.example        # Configuration template
```

### Adding New Features

The modular architecture makes it easy to extend:

```python
from spotify_controller import PlatformDetector, DeviceManager

# Your custom automation
platform = PlatformDetector()
device_manager = DeviceManager(platform)
# ... your code here
```

## License

[Your License Here]

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

- Check the logs in `logs/` directory for detailed error information
- Ensure your Spotify app permissions are correct
- Verify spotifyd is compatible with your system
