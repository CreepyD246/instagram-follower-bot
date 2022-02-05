# Importing all the modules needed
from instapy import InstaPy # To handle all matters relating to Instagram
from instapy import smart_run
import random as r # To add randomness
import schedule # To schedule bot to run specific times
import time # To add delays

# Insert your Instagram username, as well as password below
username = "your_username_here"
password = "your_password_here"

# Function to handle all the actions the bot will take
def bot():
    session = InstaPy(username=username, password=password, headless_browser=False)
    session.login() # Creating and logging into session

    # Searched for a long time trying to figure out what smart_run does.
    # If you know what smart_run does please let me know.
    with smart_run(session):
        session.like_by_tags(["programming"], amount=50) # Specifying tags to search posts for, to ultimately like them.
        session.set_do_follow(True, percentage=r.randint(40, 60)) # Setting percent chance that the bot will follow the user.
        session.set_do_comment(True, percentage=r.randint(10, 30)) # Setting percent chance that the bot will leave a comment on the post.
        session.set_comments(["Great!", "Love this", "Nice", "I like this", "Liked!"]) # Specifying what the actual comments should be if the bot decides to leave them

# Setting the time at which the bot should run each day (as long as the bot is running)
schedule.every().day.at(f"09:46").do(bot)
schedule.every().day.at(f"18:12").do(bot)

# Below loop will check every 15 seconds if there are any pending sessions that the bot needs to do.
while True:
    schedule.run_pending()
    time.sleep(15)