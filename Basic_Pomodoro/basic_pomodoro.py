import webbrowser
import time
  
url = "https://www.youtube.com/watch?v=npWuDwefXc0"

num = 0
while num < 3:
  time.sleep(7200) # 2 hours
  webbrowser.open(url) # video pra te lembrar de ter um break
  num += 1
