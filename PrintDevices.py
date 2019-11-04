import pyaudio

p = pyaudio.PyAudio()
for device in range(p.get_device_count()):
    dev = p.get_device_info_by_index(device)
    print(dev)