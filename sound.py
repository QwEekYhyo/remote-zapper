from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class Audio:
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = interface.QueryInterface(IAudioEndpointVolume)
        volume_range = self.volume.GetVolumeRange()
        self.min, self.max = volume_range[:2]
        self.initial = self.volume.GetMasterVolumeLevel()

    def current(self):
        return self.volume.GetMasterVolumeLevel()

    def reduce_volume(self):
        target_volume = max(self.min, self.current() - 4)
        self.volume.SetMasterVolumeLevel(target_volume, None)
    
    def increase_volume(self):
        target_volume = min(self.max, self.current() + 4)
        self.volume.SetMasterVolumeLevel(target_volume, None)

    def reset(self):
        self.volume.SetMasterVolumeLevel(self.initial, None)
