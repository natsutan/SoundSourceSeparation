import wave as wave

wav = wave.open('PT01.wav')

print('sampling freq [Hz]', wav.getframerate())
print('sampling size [byte]', wav.getsampwidth())
print('sampling count', wav.getnframes())
print('channel num', wav.getnchannels())
