
##code by divagar ##
import instaloader

dc = instaloader.Instaloader()
dn = input("Enter insta user name: ")

dc.download_profile(dn, profile_pic_only=True)


