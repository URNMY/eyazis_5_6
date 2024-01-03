import pyttsx3
import webbrowser
import speech_recognition as sr


voice_dict = {
    "Karsten": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_deCH_Karsten",
    "HeddaM": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_deDE_HeddaM",
    "KatjaM": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_deDE_KatjaM",
    "StefanM": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_deDE_StefanM",
    "Michael": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_deAT_Michael"
}
rate_dict = {'Fast': 2, 'Rapid': 1.5, 'Normal': 1, 'Slow': 0.5}
volume_dict = {'Loud': 2, 'Normal': 1, 'Quite': 0.5}
TIME_FOR_SPEECH = 10


def text_to_speech(text, voice_str="Karsten", rate_str="Normal", volume_str="Normal"):
    engine = pyttsx3.init()

    engine.setProperty('voice', voice_dict[voice_str])

    rate = 150
    rate = rate * rate_dict[rate_str]
    engine.setProperty('rate', rate)

    volume = 0.5
    volume = volume * volume_dict[volume_str]
    engine.setProperty('volume', volume)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


def get_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print('Listening ...')
        audio = recognizer.listen(source, 5, TIME_FOR_SPEECH)
        print('Listening stopped')
        answer = recognizer.recognize_google(audio, language='de-DE', show_all=True)
        recognized = answer["alternative"][0]["transcript"].lower() if type(answer) is dict else ""
    return recognized


def recognize_speech():
    recognized = get_speech()

    if "sagen" in recognized:
        recognized = recognized.replace("sagen", "")
        text_to_speech(recognized)
        result = "I hope you have just heard my voice."
    elif "finden" in recognized:
        recognized = recognized.replace("finden", "")
        url = f'https://www.google.com/search?q={recognized}'
        webbrowser.open(url, new=2)
        result = "Text successfully on display."
    elif "zeig mir" in recognized:
        recognized = recognized.replace("zeig mir", "")
        result = "Here is your text: " + recognized
    else:
        result = "No such command, but the text was given: " + recognized

    return result


if __name__ == "__main__":
    pass
