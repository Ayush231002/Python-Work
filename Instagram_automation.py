from instabot import Bot
bot=Bot()
bot.login(username="",password="")
# follow account
bot.follow('Name')
# upload photo
bot.upload_photo("path/image.png",caption="I love python") 
#unfollow account
bot.unfollow("Name")
#send message
bot.send_message("I love Python",["Id Name","Id Name"])
#follower list print 
followers=bot.get_user_followers("Id Name")
for follower in followers:
    print(bot.get_user_info(follower))
#following list print
following=bot.get_user_following("Id Name")
for following in following:
    print(bot.get_user_info(following))
    