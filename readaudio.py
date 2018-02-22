# -*- coding:utf-8 -*-
import pyaudio

CHUNK=1024
RATE=16000
p=pyaudio.PyAudio()

stream=p.open(	format = pyaudio.paInt16,
		channels = 2,
		rate = RATE,
		frames_per_buffer = CHUNK,
		input = True,
		output = False) # inputとoutputを同時にTrueにする
def read():
    return stream.read(CHUNK)
