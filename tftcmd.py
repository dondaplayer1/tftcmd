import os, serial, time
from json import load, loads

def coolPrint(content, line=True):
    if line:
        content = content+'\n======================================================\n'
    for char in content:
        print(char, end='')
        time.sleep(.01)

def clsc():
    os.system('cls' if os.name == 'nt' else 'clear')

clsc()

print("""
████████╗███████╗████████╗░█████╗░███╗░░░███╗██████╗░
╚══██╔══╝██╔════╝╚══██╔══╝██╔══██╗████╗░████║██╔══██╗
░░░██║░░░█████╗░░░░░██║░░░██║░░╚═╝██╔████╔██║██║░░██║
░░░██║░░░██╔══╝░░░░░██║░░░██║░░██╗██║╚██╔╝██║██║░░██║
░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝██║░╚═╝░██║██████╔╝
░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░
""")
coolPrint("======================================================\n",False)
coolPrint("Developed by dondaplayer. Thanks to MoSiren for research/testing.\n",False)
coolPrint("Version 1.0.0 - Release Build\n",False)
coolPrint("Please wait, loading config...\n",False)
coolPrint("======================================================\n",False)

with open('config.json', 'r') as f:
    conf = load(f)

with open('TFTData.json', 'r') as f:
    tftdata = load(f)
port = conf['serial']
baud = conf['baud']
pin = conf['password']

ser = serial.Serial(port=port, baudrate = baud, bytesize=8, stopbits=1)

time.sleep(3)
clsc()

def main():
    while True:
        coolPrint("""
Available Commands:
    1 - Record Voice Message
    2 - Play Voice Message
    3 - Live Patch
    4 - Record Announcement
    5 - Play Announcement
    6 - Weekly Test
    7 - Originate Alert
    8 - Send EOM
    9 - Reboot Unit
    0 - Help
    Q - Exit
        """)
        selection = input('\nSelection: ')
        
        if selection == '1':
            clsc()
            coolPrint('''
    Voice Record:
        Records a voice message through Monitor 1.
        Usage: Y/N
    ''')
            yno = input('Record voice? ')
            if yno.lower() == 'y':
                ser.write(f'*{pin}09#'.encode('utf-8'))
                coolPrint('Recording voice! Press enter when finished.')
                input()
                ser.write('#'.encode('utf-8'))
                clsc(); continue
            else:
                clsc(); continue

        elif selection == '2':
            clsc()
            coolPrint('''
    Voice Playback:
        Plays back recorded voice message
        Usage: Y/N
    ''')
            yno = input('Play? ')
            if yno.lower() == 'y':
                ser.write(f'*{pin}11#'.encode('utf-8'))
                coolPrint('Press enter when finished.')
                input()
                ser.write('#'.encode('utf-8'))
                clsc(); continue
            else:
                clsc(); continue

        elif selection == '3':
            clsc()
            coolPrint('''
    Live Patch:
        Patches live audio through main audio output and triggers
        on-air relay.
        Usage: Y/N
    ''')
            yno = input('Patch live audio? ')
            if yno.lower() == 'y':
                ser.write(f'*{pin}20#'.encode('utf-8'))
                coolPrint('Patching live audio. Press enter when finished.')
                input()
                ser.write('#'.encode('utf-8'))
                clsc(); continue
            else:
                clsc(); continue

        elif selection == '4':
            clsc()
            coolPrint('''
    Announcement Record:
        Records an announcement through Monitor 1.
        Usage: Y/N
    ''')
            yno = input('Record? ')
            if yno.lower() == 'y':
                ser.write(f'*{pin}21#'.encode('utf-8'))
                coolPrint('Recording announcement! Press enter when finished.')
                input()
                ser.write('#'.encode('utf-8'))
                clsc(); continue
            else:
                clsc(); continue

        elif selection == '5':
            clsc()
            coolPrint('''
    Announcement Playback:
        Plays back announcement.
        Usage: Y/N
    ''')
            yno = input('Play? ')
            if yno.lower() == 'y':
                ser.write(f'*{pin}22#'.encode('utf-8'))
                coolPrint('Playing! Press enter when finished.')
                input()
                ser.write('#'.encode('utf-8'))
                clsc(); continue
            else:
                clsc(); continue

        elif selection == '6':
            clsc()
            coolPrint('''
    Weekly Test:
        Sends a weekly test..
        Usage: Y/N
    ''')
            yno = input('Send weekly? ')
            if yno.lower() == 'y':
                tone = input('Attention tone? (Y/N) ')
                if tone.lower() == 'y':
                    ser.write(f'*{pin}31#'.encode('utf-8'))
                    coolPrint('Sending RWT with Attention Tone. Press enter to return to menu.')
                    input()
                    clsc(); continue
                elif tone.lower() == 'n':
                    ser.write(f'*{pin}30#'.encode('utf-8'))
                    coolPrint('Sending RWT without Attention Tone. Press enter to return to menu.')
                    input()
                    clsc(); continue
                else:
                    # Invalid input for tone
                    clsc(); continue
            else:
                clsc(); continue

        elif selection == '7':
            clsc()
            coolPrint('''
    Originate Alert:
        Originates an alert with a variety of audio options.
        When asked for counties, this refers to front panel
        location keys. 1 would be the key noted by "1". For
        multiple, type consecutively. Ex. 1269. When prompted 
        for duration, lead with 0 for minutes.
        Ex. 01 is 15 minutes.
        Usage: (N) No Audio | (P) Pre-Recorded Audio | (L) Live Audio
               Y/N
    ''')
            yno = input('Audio? (N/P/L) ')
            
            if yno.lower() not in ['n', 'p', 'l']:
                # If user typed something else, just go back to menu
                clsc(); continue
            
            try:
                event = input('Event Code? ').upper()
                code = tftdata[event][1]
                code1 = tftdata[event][0]
            except:
                clsc()
                coolPrint('Try again...')
                time.sleep(1)
                clsc(); continue  # Return to menu if event code not found
            
            loc = input('Locations? ')
            dur = input('Duration? ')
            
            if yno.lower() == 'n':
                ser.write(f'*{pin}40#'.encode('utf-8'))
                ser.write(f'*{code}#'.encode('utf-8'))
                ser.write(f'*{loc}#'.encode('utf-8'))
                ser.write(f'*{dur}#'.encode('utf-8'))
                coolPrint(f'Sending {code1}! Press enter to return to menu.')
                input()
                clsc(); continue

            elif yno.lower() == 'p':
                ser.write(f'*{pin}41#'.encode('utf-8'))
                ser.write(f'*{code}#'.encode('utf-8'))
                ser.write(f'*{loc}#'.encode('utf-8'))
                ser.write(f'*{dur}#'.encode('utf-8'))
                coolPrint(f'Sending {code1} with Pre-Recorded audio! Press enter to return to menu.')
                input()
                clsc(); continue

            elif yno.lower() == 'l':
                ser.write(f'*{pin}40#'.encode('utf-8'))
                ser.write(f'*{code}#'.encode('utf-8'))
                ser.write(f'*{loc}#'.encode('utf-8'))
                ser.write(f'*{dur}#'.encode('utf-8'))
                coolPrint(f'Sending {code1} with LIVE audio! Press enter to end alert and return to menu.')
                input()
                ser.write('#'.encode('utf-8'))
                clsc(); continue

        elif selection == '8':
            clsc()
            coolPrint('''
    EOM:
        Gorman EOM button moment.
        Usage: Y/N
    ''')
            yno = input('Send EOM? ')
            if yno.lower() == 'y':
                ser.write(f'*{pin}43#'.encode('utf-8'))
                coolPrint('Sent EOM. Press enter to go to menu.')
                input()
                clsc(); continue
            else:
                clsc(); continue

        elif selection == '9':
            clsc()
            coolPrint('''
    Reboot:
        Reboots the unit.
        Usage: Y/N
    ''')
            yno = input('Are you sure you want to reboot? ')
            if yno.lower() == 'y':
                ser.write(f'*{pin}91#'.encode('utf-8'))
                coolPrint('Rebooting unit! Press enter to return to menu.')
                input()
                clsc(); continue
            else:
                clsc(); continue

        elif selection == '0':
            clsc()
            coolPrint('''
    Help:
        Coming soon.
    ''')
            input()
            clsc(); continue

        elif selection.lower == 'q':
            coolPrint('Goodbye!',False)
            time.sleep(.5)
            exit()

        else:
            # Invalid menu selection
            clsc()
            coolPrint("Invalid selection, please try again.\n", False)
            clsc(); continue

main()
0