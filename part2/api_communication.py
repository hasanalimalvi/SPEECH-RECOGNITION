#Importing Libraries
import requests   #This library is used to talk with API
from config import API_KEY_ASSEMBLYAI 
import time


upload_endpoint = 'https://api.assemblyai.com/v2/upload' #This will post request to upload endpoints
transcript_endpoint = "https://api.assemblyai.com/v2/transcript" 
headers = {'authorization': API_KEY_ASSEMBLYAI} #Here we require authentication to use API
def upload(filename):
    def read_file(filename, chunk_size=5242880): #524288=5MB 
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    
    upload_response = requests.post(upload_endpoint,
                            headers=headers,
                            data=read_file(filename))

    audio_url = upload_response.json()['upload_url'] #Extracting audio_url which we will use to transcribe audio file using API

    return audio_url
    



#transcribe 
#Here we will convert audio to textual format 
def transcribe(audio_url):

    json = { "audio_url": audio_url }
    transcribe_response = requests.post(transcript_endpoint, json=json, headers=headers) 
    job_id = transcribe_response.json()['id']
    return job_id 


#poll 
#Here we will ask ASSEMBLY_AI that my transcript is ready or not 



def poll(transcribe_id):
    polling_endpoint = transcript_endpoint + '/' + transcribe_id  
    polling_response = polling_response = requests.get(polling_endpoint,headers=headers) 
    return polling_response.json()

def get_transcription_result_url(audio_url): 
    transcribe_id = transcribe(audio_url)
    while True:  
        data = poll(transcribe_id)
        if data['status']=='completed' : 
            return data, None
        elif data['status']=='error':
            return data, data['error'] 
        
        print("Waiting 30 seconds...") 
        time.sleep(30)



#save 
#To save transcripted file  

def save_transcript(audio_url,filename):
    data,error = get_transcription_result_url(audio_url)
    text_filename = "output.txt" 
    if data:
        with open(text_filename, "w") as f:
            f.write(data['text']) 
        print('Transcription saved!!')  
    elif error:
        print("Error!!",error)  




