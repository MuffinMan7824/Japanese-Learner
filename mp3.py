import requests
import os

kana = ["か", "き", "く", "け", "こ",
    # S row
    "さ", "し", "す", "せ", "そ",
    # T row
    "た", "ち", "つ", "て", "と",
    # N row
    "な", "に", "ぬ", "ね", "の",
    # H row
    "は", "ひ", "ふ", "へ", "ほ",
    # M row
    "ま", "み", "む", "め", "も",
    # Y row
    "や", "ゆ", "よ",
    # R row
    "ら", "り", "る", "れ", "ろ",
    # W row
    "わ", "を",
    # N
    "ん"] 

os.makedirs("audio", exist_ok=True) 
for char in kana:
    url = f"https://www.japanese50sounds.com/audio/kana/seion/{char}.mp3"
    response = requests.get(url)
    
    with open(f"audio/{char}.mp3", "wb") as f:
        f.write(response.content)
    
    print(f"Downloaded {char}")