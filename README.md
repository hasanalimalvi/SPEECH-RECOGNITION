# SPEECH RECOGNITION 
It is ML model which converts data in audio format to textual format. You can call it  basic version of *Google Audio Search* . 

## 1. Read and Write Audio Files 

- In this part we will deal with how to read and write audio files using python module, <code>wave</code>.  

- In <mark>wave_example.py</mark>, I had read all the details of audio file named **harvard.wav**. 
  
- In the same .py file we will copy all the data and paste it in the new file with name **harvard_new.wav**.
  
- Using <code>matplotlib</code> (python library) we will plot whole audio signal in the file <mark>plot_audio.py</mark>.
  
- <code>pydub</code> is the python library used to manipulate audio files.  
  
- I had read **mashup.mp3** in <mark>load_mp3.py</mark>. 
  
- The final **.py** file is <mark>record_mic.py</mark> for recording through your device mic and store in **output.wav** format using <code>pyaudio</code>.  


## 2. Audio To Textual Using API 
- I had used API of *Assembly AI*. First of all, I will make <mark>config.py</mark> in which I will store my authentication key. 
  
- Then I will import this key in the <mark>main.py</main> file. 
  
- There are total 4 steps to convert audio to text using API.  

- I had made function of this 4 steps in <mark>api_communication.py</mark> file, which we will import in the main file. 

- Before proceeding to this 4 steps we need to import <code>respects</code>, a python library helps to talk with API. 

- The first step is to upload audio file to *Assembly AI* portal. 

- In this step we will read audio file using **read_file** function and upload it which in turn will generate **upload_response**. 

- In **upload_response** we will require **audio_url** for the next step. 

- Next step is to transcribe the audio file. This is where audio file is converted to text. 

- We will pass **audio_url** to *Assembly AI* portal through API which will give us **transcribe_response**. 

- **transcribe_response** will help to track the process of transcription.

- Specifically, in **transcribe_response** there is **id** of our work, which we will use in **polling**. 

- **Polling** is the process in which we ask **Assembly AI** about our completion of trascription. 

- Using **id** we got from **transcription** process we will do polling. 

- The last step is to save text file in our directory. 

- During **polling** we will get **polling_response** which contains **text** of the audio file. 

- Using that **text** we will copy the text and paste it into <mark>output.txt</mark>.  

## 3. Transcript of YouTube Video 

- In this part we will use all the function we created in last part. 

- We will use <code>yt_dlp</code>, a python library to extract all information of youtube videos in <mark>yt_extractor.py</mark> file. 

- We want only audio, so we will get **audio_url** under the format section, inside it we will have one section with extension : *m4a*, it is an audio extension, which contains **audio_url** of this youtube video. 

- I had made **get_audio_url** function which returns **audio_url** from **video_information** . 

- In <mark>main.py</mark> I had imported all the functions required from <mark>yt_extractor.py</mark> file and <mark>api</mark> file which connects us with *Assembly AI* through **API**. 

- So, when I run <mark>main.py</mark> we will get one **text** file which contains transcript of that video and other one is **json** file which contains sentiments of each setence of the transcript. 




