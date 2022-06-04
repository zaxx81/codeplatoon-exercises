from User import User

class FreeUser(User):
    
    def __init__(self, name):
        parent_instance = super()
        parent_instance.__init__(name)
        
        self.is_premium = False
        
    def add_post(self, post):
        if self.post_count >= 2:
            print('Post count limited to 2, upgrade to Premium to post more!\n')
        else:
            super().add_post(post)
    