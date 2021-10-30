import soundfile as sf
from pedalboard import (
    Pedalboard,
    Compressor,
    Chorus,
    Gain,
    Reverb,
    Limiter,
    LadderFilter,
    Phaser,
)

audio, sample_rate = sf.read('input.wav')

# Make a Pedalboard object, containing multiple plugins:
board = Pedalboard([
    Reverb(room_size=0.25),
    Compressor(threshold_db=-50, ratio=5),
    Gain(gain_db=22),
    Chorus(),
    LadderFilter(mode=LadderFilter.Mode.HPF12, cutoff_hz=150),
    Phaser(),
], sample_rate=sample_rate)

# Pedalboard objects behave like lists, so you can add plugins:
board.append(Reverb(room_size=0.2))
board.append(Compressor(threshold_db=-12, ratio=2))
board.append(Limiter())

# Run the audio through this pedalboard!
effected = board(audio)

# Write the audio back as a wav file:
with sf.SoundFile('./output.wav', 'w', samplerate=sample_rate, channels=len(effected.shape)) as f:
    f.write(effected)

