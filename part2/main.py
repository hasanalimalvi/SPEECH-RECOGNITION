#Importing Libraries
import sys #This library is used to take arguments  
from  api_communication import *

filename = sys.argv[1] #We will pass second argument to be the path of audio file. argv[0] is default argument for this file's name

audio_url = upload(filename)  
save_transcript(audio_url,filename)


