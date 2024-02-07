# main.py
from led_control import LEDControl
from voice_interaction import speak, listen

def main():
    led_control = LEDControl()
    led_control.set_all_leds(Color(0, 255, 0))  # Example: set LEDs to green
    
    while True:
        command = listen()
        print(f"Heard: {command}")
        if "turn off" in command.lower():
            led_control.set_all_leds(Color(0, 0, 0))  # Turn LEDs off
            speak("Turning off the lights.")
            break  # Exit the loop to end the program

if __name__ == "__main__":
    main()
