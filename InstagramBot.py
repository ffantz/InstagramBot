from selenium import webdriver
from time import sleep

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')

    def openInstagram(self):
        print("Opening instagram...")
        self.driver.get("https://instagram.com")
        sleep(1)

    def logIn(self):
        print("Login...")
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(self.password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
            .click()
        sleep(5)

    def logOut(self):
        print("Logout...")
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[1]")\
            .click()
        self.driver.find_element_by_xpath("//*[@id=\"f16163356daea18\"]")\
            .click()
        sleep(1)

    def close(self):
        print("Closing...")
        self.driver.quit()

    def closeModals(self):
        print("Closing modal 1...")
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
        print("Closing modal 2...")
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

    def acessProfile(self):
        print("Accessing profile...")
        self.driver.get("https://instagram.com/" + self.username)
        sleep(2)

    def getUnfollowers(self):
        followingList = self._getFollowingList()
        followersList = self._getFollowersList()

        notFollowingUsers = [user for user in followingList if user not in followersList]

        self._saveList(notFollowingUsers, 'notFollowing', 'notFollowing.txt')
        self._saveList(followingList, 'following', 'following.txt')
        self._saveList(followersList, 'followers', 'followers.txt')

    def _saveList(self, content, type, fileName):
        print("Saving " + type + " list...")
        fileItem = open(fileName, 'w')
        for item in content:
            fileItem.write(item + "\n")
        fileItem.close()

    def _getFollowersList(self):
        print("Getting followers list...")
        self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]")\
            .click()
        sleep(1)

        scrollBox = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scrollBox)

        links = scrollBox.find_elements_by_tag_name("a")
        names = [name.text for name in links if name.text != '']

        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")\
            .click()

        return names

    def _getFollowingList(self):
        print("Getting following list...")
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]")\
            .click()
        sleep(1)

        scrollBox = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scrollBox)

        links = scrollBox.find_elements_by_tag_name("a")
        names = [name.text for name in links if name.text != '']

        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")\
            .click()

        return names