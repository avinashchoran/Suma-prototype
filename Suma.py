from customtkinter import *
import customtkinter as ctk
#####summarization####
import tkinter as tk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
######################
from transformers import BartTokenizer, BartForConditionalGeneration

# Load pre-trained BART model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)
adsum_num=3
######################
######audio###########

import gtts
from pygame import mixer
######################
#########selenium#####
from tkinter import Button, Label, filedialog, Text
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
######################

app = CTk()
# ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app.geometry("1200x600+0+0")
app.title("Elevating learning experience")

if getattr(sys, 'frozen', False):
        # If the application is running as a single file, use the _MEIPASS directory.
            bundle_dir = sys._MEIPASS
else:
    # Otherwise, use the regular assets directory.
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
app.icon_path = os.path.join(bundle_dir, "assets", "icon.ico")
app.iconbitmap(app.icon_path)

sum_num=3
fsum=""
file_path=""
# app.state("zoomed")
#############functions##############

def summary(a):
    global input_text
    input_text = ocr_textbox.get("1.0", tk.END)  # Use tk.END instead of "end-1c"
    print(input_text)
    print("entered summary again")
    parser = PlaintextParser.from_string(input_text, Tokenizer("english"))

    # Create an LSA summarizer
    summarizer = LsaSummarizer()

    # Generate the summary
    summary = summarizer(parser.document, sentences_count=a) 
    con = ""
    for sentence in summary:
        con += str(sentence)+ "\n" 
    global fsum
    fsum=con
    sum_textbox.delete("1.0","end")
    sum_textbox.insert(tk.END, con)

def ogsum():
    global sum_num
    summary(sum_num)

def plus_sum():
    global sum_num
    sum_num+=1
    summary(sum_num)

def minus_sum():
    global sum_num
    sum_num-=1
    summary(sum_num)

###### advance summary ######

def estimate_tokens_per_line(tokenizer, text, num_lines=3):
    """
    Estimate the number of tokens per line and calculate the max and min lengths
    based on the desired number of lines.
    """
    # Tokenize the text
    tokens = tokenizer.encode(text)
    # Estimate tokens per line
    tokens_per_line = len(tokens) // text.count('\n')
    # Calculate the max and min lengths based on the desired number of lines
    max_length = int(tokens_per_line * num_lines * 1.2)  # Adding a buffer
    min_length = int(tokens_per_line * num_lines * 0.8)  # Adding a buffer
    return max_length, min_length
def ad_summary(a):
    # Input text to be summarized
    global input_text
    input_text = ocr_textbox.get("1.0", tk.END) 

    # Specify the desired number of lines in the summary
    desired_lines = a
    max_length, min_length = estimate_tokens_per_line(tokenizer, input_text, desired_lines)

    # Tokenize and summarize the input text using BART
    inputs = tokenizer.encode("summarize: " + input_text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode and output the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    print(summary)
    sum_textbox.delete("1.0","end")
    sum_textbox.insert(tk.END, summary)
   
def adsum():
    global adsum_num
    ad_summary(adsum_num)

def ad_plus_sum():
    global adsum_num
    adsum_num+=1
    ad_summary(adsum_num)

def ad_minus_sum():
    global adsum_num
    adsum_num-=1
    ad_summary(adsum_num)

######audio##########
def start():
    print("start")
    # fsum="""Rain is water droplets that have condensed from atmospheric water vapor and then fall under gravity. Rain is a major component of the water cycle and is responsible for depositing most of the fresh water on the Earth. It provides water for hydroelectric power plants, crop irrigation, and suitable conditions for many types of ecosystems."""
    # global fsum
    audio_text = sum_textbox.get("1.0", tk.END)
    print(audio_text)
    sound=gtts.gTTS(audio_text,lang = "en")
    sound.save("welcome.mp3")
    mixer.init()
    mixer.music.load('welcome.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play()

def start_digi():
    digi_text = ocr_textbox.get("1.0", tk.END)  # Use tk.END instead of "end-1c"
    sound=gtts.gTTS(digi_text,lang = "en")
    sound.save("digi.mp3")
    mixer.init()
    mixer.music.load('digi.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play()

def pause():
    print("pause")
    mixer.music.pause()
    
def resume():
    print("resume")
    mixer.music.unpause()

##########  summarization  ###############

def open_file():
    """Opens a file dialog and displays content in the text area"""
    global file_path
    file_path = filedialog.askopenfilename()
    
def process_file():
    global file_path
    ocr_textbox.delete(1.0, "end")  # Clear existing text
    ocr_textbox.insert(1.0, "Processing...")
    app.update_idletasks() 
    print(file_path)
    print("processing")
    #Code for processing the file and extracting text
    #For testing purpose I used api or selenium for OCR via web scraping
    x = "some text extracted from the file"
    ocr_textbox.delete(1.0, "end")  # Clear "Uploading File..." message
    ocr_textbox.insert(1.0, x)
    print(x)
    time.sleep(10)
    


######################################


app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
#frame 1
frame_1 = CTkFrame(master=app,border_color="#4158D0",corner_radius=15,border_width=2)

# frame_1.grid(row = 0, column = 0,sticky="nsew")
# frame_1.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
frame_1.pack(side="left", expand="true",fill="x",padx=5)

label = CTkLabel(master=frame_1, text="Open a file", font=("Helvetica", 20))
label.place(relx=0.5, rely=0.2, anchor="n") 

btn = CTkButton(master=frame_1, text="Open", corner_radius=32, fg_color="#4158D0", 
                hover_color="#C850C0", border_color="#FFCC70",command=open_file)

btn.place(relx=0.5, rely=0.5, anchor="n") 

process = CTkButton(master=frame_1, text="Process", corner_radius=32, fg_color="#4158D0", 
                hover_color="#C850C0", border_color="#FFCC70",command=process_file)

process.place(relx=0.5, rely=0.75, anchor="n") 


###############################
frame_2 = CTkFrame(master=app)
frame_2.pack(side="left",fill="both",expand="true",padx=5)
ocr_textbox = CTkTextbox(master=frame_2,corner_radius=10,border_color="#FFCC70", border_width=2)
ocr_textbox.pack(side="top",fill = "both",expand="true")
#grid(row=1,column=0,sticky="w",columnspan="2") 
ocr_label = CTkLabel(master=frame_2, text="Converted Digital notes", fg_color="transparent",font=("Helvetica", 16))
ocr_label.pack(side="bottom")

#####################
summarize_frame=CTkFrame(master=app)
summarize_frame.pack(side="left",padx=5)
sum_btn=CTkButton(master=summarize_frame, text="Summarize",command=ogsum)
sum_btn.grid(row=0,column=0,columnspan=2,sticky="nsew")
plus_btn=CTkButton(master=summarize_frame, text="+",command=plus_sum,width=87)
plus_btn.grid(row=1,column=0)
minus_btn=CTkButton(master=summarize_frame, text="-",command=minus_sum,width=87)
minus_btn.grid(row=1,column=1)

ad_sum_btn=CTkButton(master=summarize_frame, text="Advance Summarize",command=adsum)
ad_sum_btn.grid(row=2,column=0,columnspan=2,sticky="nsew")
ad_plus_btn=CTkButton(master=summarize_frame, text="+",command=ad_plus_sum,width=87)
ad_plus_btn.grid(row=3,column=0)
ad_minus_btn=CTkButton(master=summarize_frame, text="-",command=ad_minus_sum,width=87)
ad_minus_btn.grid(row=3,column=1)
#####################################

frame_3 = CTkFrame(master=app)
# frame_2.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
# frame_2.grid(row = 0, column = 1,sticky="nsew")
frame_3.pack(side="left",expand="true",fill="both",padx=5)
sum_textbox = CTkTextbox(master=frame_3, scrollbar_button_color="#FFCC70", corner_radius=10,
                     border_color="#FFCC70", border_width=2)
sum_textbox.pack(side="top",expand="true",fill = "both")
sum_label = CTkLabel(master=frame_3, text="Summarized Digital notes", fg_color="transparent",font=("Helvetica", 16))
sum_label.pack(side="bottom")
######################################

frame_4 = CTkFrame(master=app,border_color="#4158D0",corner_radius=15,border_width=2)
frame_4.pack(side="left",expand="true",fill="x",padx=5)
audio_label = CTkLabel(master=frame_4, text="Play as Audiobook", fg_color="transparent",font=("Helvetica", 16))
audio_label.pack(pady=10)
button = ctk.CTkButton(master=frame_4, text="Start with summarized notes", command=start,width=220)
button.pack(pady=10)
button4 = ctk.CTkButton(master=frame_4, text="Start with digital notes", command=start_digi,width=220)
button4.pack(pady=10)
button2 = ctk.CTkButton(master=frame_4, text="Pause", command=pause,width=220)
button2.pack(pady=10)
button3 = ctk.CTkButton(master=frame_4, text="Resume", command=resume,width=220)
button3.pack(pady=10)

app.mainloop()