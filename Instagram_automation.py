from instabot import Bot

bot = Bot()
bot.login(username = "username/phonenumber/gmail", password ="password")
# bot.follow("avalok2023")
# bot.upload_photo("location of file",caption=" write your caption what do you want")
# bot.unfollow("avalok2023")
# bot.send_message('i know you', ['avalok2023', 'av.studios.in'])
# followers = bot.get_user_followers("username")
# for i in followers:
#     print(bot.get_user_info(followers))

following = bot.get_user_following("username")
for j in following:
    print(bot.get_user_info(following))
