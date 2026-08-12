import sounddevice as sd
import numpy as np
import subprocess
from faster_whisper import WhisperModel
import 

class Voice:
    def __init__(self):
        self.sample_rate = 4800
        self.device = 10  # PipeWire
        print("Carregando Sistema de Voz")

        print("Baixando Modelo de Voz")
        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

        print("Whisper carregado!")

    def listen(self):
        audio = sd.rec(
            int(5 * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype="float32",
            device=self.device
        )

        sd.wait()

        audio = audio.flatten()
        #audio = audio/max(np.max(np.abs(audio)),1e-6)
        volume = np.abs(audio).mean()
        pico = np.abs(audio).max()
        
        print(f"Volume médio: {volume:.6f}")
        
        #print(f"Pico: {pico:.6f}")
        
        print("Sending...")

        segments, info = self.model.transcribe(
            audio,
            language="pt",
            vad_filter=True,
            #beam_size=5,
            #temperature=0.0
        )

        text_parts = []

        for segment in segments:
            print(f"Eu: {segment.text}")
            text_parts.append(segment.text)

        return " ".join(text_parts).strip()

    def speak(self, text):
        print(f"Jarvis: {text}")
        subprocess.run(["espeak-ng","-v","pt-br",text])
