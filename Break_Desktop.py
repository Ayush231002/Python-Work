from plyer import notification
import time 

if __name__ =='__main__':
    while True:
     notification.notify(
        title = "*** Take Rest ***",
        message="Rest is vital for better  mental health, increase"
        app_icon="C:/Users/91860/OneDrive/Desktop/30 Days/try.ico",
        timeout=5)
     time.sleep(10)
