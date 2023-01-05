'''
This problem is a solution of
Problem 1 of CodeWithHarry Practice Set!
'''
# This is also a comment just like the above line
import schedule
import time
from datetime import datetime, timedelta,date


def main_driver():
    print('''Twinkle, twinkle, little star,
    How I wonder what you are!
    Up above the world so high,
    Like a diamond in the sky.''')
    return None



print('Starting at:', str(datetime.now())[:19])
schedule.every().day.at("18:28").do(main_driver)
print('Ending at:', str(datetime.now())[:19])

 

while True:
    schedule.run_pending()
    time.sleep(1)  