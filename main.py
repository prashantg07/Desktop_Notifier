import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "**Please Do Excercise Daily!!",
            message = "We know 150 minutes of physical activity each week sounds like a lot, but you don't have to do it all at once. It could be 30 minutes a day, 5 days a week. You can spread your activity out during the week and break it up into smaller chunks of time.",
            app_icon = r"C:\Users\lenovo\OneDrive\Desktop\Desktop_notifier\icon.ico",
            timeout=10
        )
        time.sleep(6)
        #time.sleep(60*60)
