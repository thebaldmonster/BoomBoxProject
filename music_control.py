import pygame
import os
from time import sleep
# Import the required library for WS2812 LEDs
from rpi_ws281x import PixelStrip, Color

try:
    import RPi.GPIO as GPIO
    on_raspberry_pi = True
except (ImportError, ModuleNotFoundError):
    on_raspberry_pi = False
    print("RPi.GPIO library not found. GPIO functionality will be disabled.")

# LED strip configuration:
LED_COUNT = 3        # Number of LED pixels.
LED_PIN = 10         # GPIO pin connected to the pixels (10, 12, 18, 21 on Pi).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10         # DMA channel to use for generating signal
LED_BRIGHTNESS = 255 # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal

# Initialize LED strip
if on_raspberry_pi:
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    strip.begin()

def set_led_color(led_index, color):
    """Set color of a single LED"""
    if on_raspberry_pi:
        strip.setPixelColor(led_index, color)
        strip.show()

def clear_leds():
    """Turn off all LEDs."""
    if on_raspberry_pi:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

# Define GPIO pins for buttons
button_pins = [5, 6, 13]  # Adjust as necessary

# Define music folders for each button
music_folders = [
    "/path/to/music/folder1",
    "/path/to/music/folder2",
    "/path/to/music/folder3"
]

# Initialize pygame mixer
pygame.mixer.init()

# GPIO setup
if on_raspberry_pi:
    GPIO.setmode(GPIO.BCM)
    for pin in button_pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

current_folder = [None]  # Keep track of the currently playing folder

# Add your existing music control functions here, adjusting LED control as needed...

# Example of integrating LED control into a button press callback
def button_callback(channel):
    # Your existing button callback logic here
    # Include calls to set_led_color() or clear_leds() based on playback state

if on_raspberry_pi:
    # Setup event detection for each button
    for pin in button_pins:
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=button_callback, bouncetime=300)

# Main loop or other initialization code...

# Remember to call clear_leds() on exit to turn off LEDs
try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    clear_leds()
    if on_raspberry_pi:
        GPIO.cleanup()
