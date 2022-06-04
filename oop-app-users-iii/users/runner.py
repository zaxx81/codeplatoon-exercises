from User import User
from FreeUser import FreeUser
from PremiumUser import PremiumUser

def main():
    # emily = User('Emily')
    # jack = User('Jack')
    # emily.add_post('hello, my name is emily!')
    # emily.add_post('I am 23 years old')
    # emily.add_post('I enjoy long walks on the beach')
    # jack.add_post('Hey guys, im jack')
    # jack.add_post('this is another unique post')
    # print(emily.all_posts)
    # print(jack.all_posts)
    # print(jack.delete_post('Hey guys, im jack'))
    # print(jack.all_posts)
    # print(jack.stored_posts)
    kaleb = FreeUser('Kaleb')
    kaylee = PremiumUser('Kaylee')
    zack = User('Zack')


    kaleb.add_post('Hey, guys! This is my first post!')
    kaleb.add_post('Hey, guys! This is my second post!')
    kaleb.add_post('Hey, guys! This is my third post!')
    kaleb.add_post('Hey, guys! This is my fourth post!')
    kaylee.add_post('Hey, guys! This is my first post!')
    kaylee.add_post('Hey, guys! This is my second post!')
    kaylee.add_post('Hey, guys! This is my third post!')
    # zack.add_post('Congrats on your first post Angel!')
    # kaylee.add_post('Hey, this is my first post too!')
    # zack.add_post('Congrats on your first post Terrance!')
    kaleb.show_posts()
    kaylee.show_posts()
    # User.publish()
    # zack.del_post(2)
    # zack.show_posts()
    # User.publish()
    
if __name__ == '__main__':
    main()