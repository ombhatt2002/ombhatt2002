import win32com.client
 
speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("enter any word")
    s = input()
    speaker.speak(s)