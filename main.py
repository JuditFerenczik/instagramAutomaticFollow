from insta import InstaFollower
from secret import CHROME_DRIVER_PATH


insta = InstaFollower(CHROME_DRIVER_PATH)
insta.login()
buttons_to_click = insta.find_followers()
insta.follow(buttons_to_click)
