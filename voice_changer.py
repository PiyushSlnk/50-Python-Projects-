import sys
import pyaudio
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QComboBox
import pyo
import wave

class VoiceChangerApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the UI elements
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setWindowTitle('Voice Changer App')
        self.setGeometry(100, 100, 400, 300)

        # Layout
        self.layout = QVBoxLayout()

        # Add label
        self.label = QLabel("Choose Voice Effect:", self)
        self.layout.addWidget(self.label)

        # ComboBox for voice effect choices
        self.effect_combo = QComboBox(self)
        self.effect_combo.addItem("Select Effect")
        self.effect_combo.addItem("Male Voice")
        self.effect_combo.addItem("Female Voice")
        self.effect_combo.addItem("Robot Voice")
        self.effect_combo.addItem("Animal Voice")
        self.layout.addWidget(self.effect_combo)

        # Record Button
        self.record_btn = QPushButton("Record", self)
        self.record_btn.clicked.connect(self.record_audio)
        self.layout.addWidget(self.record_btn)

        # Apply Effect Button
        self.apply_btn = QPushButton("Apply Effect", self)
        self.apply_btn.clicked.connect(self.apply_effect)
        self.layout.addWidget(self.apply_btn)

        # Play Button
        self.play_btn = QPushButton("Play", self)
        self.play_btn.clicked.connect(self.play_audio)
        self.layout.addWidget(self.play_btn)

        # Set layout
        self.setLayout(self.layout)

        # Placeholder for the audio file
        self.audio_file = None

        # Initialize pyo server
        self.s = pyo.Server().boot()
        self.s.start()

    def record_audio(self):
        """Record audio from the microphone"""
        self.audio_file = 'recorded.wav'

        # Set parameters for PyAudio
        RATE = 44100  # Sample rate
        CHUNK = 1024  # Buffer size
        FORMAT = pyaudio.paInt16  # Audio format
        CHANNELS = 1  # Mono audio

        # Initialize PyAudio
        p = pyaudio.PyAudio()

        # Start recording
        print("Recording...")
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
        frames = []

        for _ in range(0, int(RATE / CHUNK * 5)):  # Record for 5 seconds
            data = stream.read(CHUNK)
            frames.append(data)

        # Stop recording
        print("Recording Finished.")
        stream.stop_stream()
        stream.close()
        p.terminate()

        # Save the recorded audio as a .wav file
        with wave.open(self.audio_file, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

    def apply_effect(self):
        """Apply selected voice effect to the recorded audio"""
        if not self.audio_file:
            print("No audio file recorded.")
            return

        effect = self.effect_combo.currentText()

        audio = AudioSegment.from_wav(self.audio_file)

        if effect == "Male Voice":
            # Lower the pitch for a male voice
            audio = self.pitch_shift(audio, -5)
        elif effect == "Female Voice":
            # Raise the pitch for a female voice
            audio = self.pitch_shift(audio, 5)
        elif effect == "Robot Voice":
            # Add distortion to create a robotic voice
            audio = self.add_robot_effect(audio)
        elif effect == "Animal Voice":
            # Speed up and pitch-shift to create an animal-like voice
            audio = self.add_animal_effect(audio)
        else:
            print("Please select an effect.")
            return

        # Save the modified audio
        modified_file = 'modified_audio.wav'
        audio.export(modified_file, format="wav")
        self.audio_file = modified_file
        print(f"Effect applied. Saved as {modified_file}")

    def pitch_shift(self, audio, semitones):
        """Apply pitch shifting using pyo"""
        # Convert pydub audio to numpy array
        samples = np.array(audio.get_array_of_samples(), dtype=np.float32)

        # Use pyo to process the audio
        sound = pyo.Snd(samples, sr=audio.frame_rate)
        shifted = sound.shiftPitch(semitones)

        # Convert back to pydub AudioSegment
        shifted_samples = shifted.getData()
        shifted_audio = AudioSegment(
            shifted_samples.tobytes(),
            frame_rate=audio.frame_rate,
            sample_width=audio.sample_width,
            channels=audio.channels
        )

        return shifted_audio

    def add_robot_effect(self, audio):
        """Apply robot-like effect by distorting the audio"""
        # Example: Add some speed distortion and pitch change
        audio = self.pitch_shift(audio, -3)
        audio = audio.speedup(playback_speed=1.2)
        return audio

    def add_animal_effect(self, audio):
        """Apply animal-like effect by speeding up and pitch shifting"""
        audio = self.pitch_shift(audio, 7)
        audio = audio.speedup(playback_speed=1.5)
        return audio

    def play_audio(self):
        """Play the modified audio"""
        if not self.audio_file:
            print("No audio file to play.")
            return

        audio = AudioSegment.from_wav(self.audio_file)
        print("Playing audio...")
        play(audio)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VoiceChangerApp()
    ex.show()
    sys.exit(app.exec_())
