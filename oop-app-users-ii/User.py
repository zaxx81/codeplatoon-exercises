class User:
    discussion_thread = {}
    thread_counter = 0
    
    # @classmethod
    def publish():
      print('Publishing all user posts in the thread...')
      print(f'{User.discussion_thread}\n')
      print('Done...\n')

    def __init__(self,name,email):
        print(f"Creating user '{name}'...")
        self.name = name
        self.email = email
        self.posts = {}
        self.post_count = 0
        print('Done...\n')
    
    def add_post(self, text):
      print(f"Adding post by '{self.name}'...")
      self.post_count += 1
      self.posts.update({self.post_count: text})
      
      #Updates Class variables
      print(f"Updating thread...")
      User.thread_counter += 1
      User.discussion_thread.update({f'{self.name}-{self.post_count}' :
        f'Post by {self.name} \n {text}'})
      print('Done...\n')
      
    def del_post(self, key):
      print(f"Deleting post #{key} by '{self.name}'...")
      self.posts.pop(key)
      
      #Updates Class variables
      print(f"Updating thread...")
      User.discussion_thread.pop(f'{self.name}-{key}')
      print('Done...\n')

    def show_posts(self):
      print(f'Showing user posts by {self.name}...')
      print(self.posts)
      print('Done...\n')


angel = User('Angel','angel@email.com')
terrance = User('Terrance','Terrance@email.com')
zack = User('Zack','zack@email.com')


angel.add_post('Hey, guys! This is my first post!')
zack.add_post('Congrats on your first post Angel!')
terrance.add_post('Hey, this is my first post too!')
zack.add_post('Congrats on your first post Terrance!')
zack.show_posts()
User.publish()
zack.del_post(2)
zack.show_posts()
User.publish()
