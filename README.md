# mic-mute-status/mic-mute-status/README.md

# Mic Mute Status Overlay

This project provides a simple overlay application for monitoring and displaying the mute status of your microphone on Linux systems. It uses GTK for the graphical interface and interacts with the PulseAudio sound server to listen for changes in microphone status.

## Features

- Displays the current mute status of the microphone.
- Allows users to drag the overlay around the screen.
- Automatically updates when the microphone status changes.

## Installation

To install the application, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/mic-mute-status.git
   cd mic-mute-status
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   ./bin/mic-mute-status
   ```

## Usage

Once the application is running, it will display an overlay indicating the current mute status of your microphone. You can drag the overlay to your desired position on the screen.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.