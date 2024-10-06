import speech_recognition as sr
import RPi.GPIO as GPIO
import time

# GPIO Setup
LED_PIN = 18
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(LED_PIN, GPIO.OUT)

# Initialize Speech Recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Function to process the voice command
def process_command(command):
    command = command.lower()
    if "on" in command:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED turned ON")
    elif "off" in command:
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED turned OFF")
    else:
        print("Unknown command:", command)

# Main loop to listen and act on voice commands
def listen_and_control_led():
    with microphone as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for commands...")

        while True:
            try:
                print("Say something...")
                audio = recognizer.listen(source)


                # Using Google Speech Recognition to convert speech to text
                command = recognizer.recognize_google(audio)
                print("You said:", command)
                
                process_command(command)

            except sr.UnknownValueError:
                print("Could not understand the audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
            time.sleep(1)

# Start listening
try:
    listen_and_control_led()
except KeyboardInterrupt:
    print("Program stopped by user")
finally:
    GPIO.cleanup()

