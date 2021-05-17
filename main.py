from secrets import password, username
from InstagramBot import InstagramBot

instagramBot = InstagramBot(username, password)
instagramBot.openInstagram()
instagramBot.logIn()
instagramBot.closeModals()
instagramBot.acessProfile()
instagramBot.getUnfollowers()
instagramBot.close()