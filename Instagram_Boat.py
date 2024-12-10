from instabot import Bot

# Initialize bot
bot = Bot()

# Login
bot.login(username="_thesatanicone_", password="Your_Password")

# Perform actions
bot.follow("kimkardashian")

# Uploading Image 
bot.upload_photo("C:/Users/ASUS/Pictures/Python50.png",caption="i love python")

# unfollow 
bot.unfollow("kimkardashian")

# Mass Massage
bot.send_message("hii there",["hriii_05","dutta3516"])

# get all follower name 
followers =  bot.get_user_follower("_thesatanicone_")

for follower in followers:
     print(bot.get_user_info(follower))


# get all the following 
following = bot.get_user_following("_thesatanicone")

for followings in following:
     print(bot.get_user_info(followings))

