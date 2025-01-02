![TFTCMD](https://github.com/dondaplayer1/tftcmd/blob/main/assets/tftcmd.png)
## TFT EAS 911 Remote Control software

## What can it do?

> - Record a voice message for later playback
> - Playback the recorded voice message
> - Live patch on-air
> - Record an announcement for later playback
> - Playback the recorded announcement
> - Send a weekly test
> - Send a monthly test
> - Originate alerts with a variety of different options (Pre-recorded audio, live patch audio)
> - Gorman EOM button
> - Remotely reboot the unit

## Requirements

- TFT EAS 911, TFT EAS 911+, or TFT EAS 911D with modified ROM*
- J303 (COM3) serial port on the EAS unit
- Python 3 and the "pyserial" library

*TFT EAS 911D requires soldering to make use of this program. The hardware exists on the motherboard to support the J303 header, however there is no COM port soldered to the board. For complete functionality, you only need GND, RX, and TX soldered to the motherboard. Additionally, you are required to flash your TFT EAS 911D unit with the TFT EAS 911 ROM to enable the DTMF interface.

## Usage

Configure an access pin through menu 19 on the EAS unit. Configure the program through config.json and select the correct COM port, baud rate, and pin.
Run the program with `python3 tftcmd.py` on Linux, or `python tftcmd.py` on Windows. Follow onscreen prompts to use the software and interface with your unit.

When originating:
- When asked for locations, the numbers coorelate to the location keys on the front of the unit. With the first being "1" and the last being "0"
- When asked for duration, you must lead with "0" for minutes. For example, "01" is 15 minutes.

When recording audio or doing a live patch, the audio is recorded through Monitor 1.
