# Audio file formats 
# -.mp3 (lossy compression format)
# -.flac (loss less compression format)
# -.wav (uncompressed format) 

import wave 

# Audio signal paramters 
# -number of channels 
# -sample width 
# -framerate/sample_ratev
# -number of frames 
# -values of a frame 

obj = wave.open("harvard.wav", "rb") #rb- read in binary format
print("Number of channels:", obj.getnchannels()) 
print("sample width:", obj.getsampwidth()) 
print("frame rate:", obj.getframerate()) 
print("Number of frames:", obj.getnframes()) 
print("parameters", obj.getparams())  

t_audio = obj.getnframes()/ obj.getframerate()  

print("Total time of audio is", t_audio, "sec") 

frames = obj.readframes(-1) 
print(type(frames), type(frames[0])) 
print(len(frames)/4)  

obj.close()

obj_new = wave.open("harvard_new.wav","wb") #wb - write mode 

obj_new.setnchannels(2) 
obj_new.setsampwidth(2) 
obj_new.setframerate(44100.0) 
obj_new.writeframes(frames) 

obj_new.close()

