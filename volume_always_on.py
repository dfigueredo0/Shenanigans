import comtypes, threading
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
import time

stop_event = threading.Event()

def set_volume_to_maximum():
    comtypes.CoInitialize()

    current_device = AudioUtilities.GetSpeakers()
    interface = current_device.Activate(IAudioEndpointVolume._iid_, comtypes.CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    while not stop_event.is_set():
        if current_device != AudioUtilities.GetSpeakers():
            current_device = AudioUtilities.GetSpeakers()
            interface = current_device.Activate(IAudioEndpointVolume._iid_, comtypes.CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(0.5, None)
        volume.SetMute(0,None)
        time.sleep(10)
    
    comtypes.CoUninitialize()