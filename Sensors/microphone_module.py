# microphone_module.py

import pyaudio
import numpy as np

def get_decibel_level():
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open stream
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)

    try:
        while True:
            # Read audio data from the stream
            data = np.frombuffer(stream.read(1024), dtype=np.int16)
            
            # Calculate RMS value
            rms = np.sqrt(np.mean(np.square(data)))
            
            # Convert RMS to decibels
            decibel_level = 20 * np.log10(rms)
            
            print(f"Decibel Level: {decibel_level:.2f} dB")
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    get_decibel_level()