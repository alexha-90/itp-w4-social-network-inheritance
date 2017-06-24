
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []
        

    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post)
        
  
    '''
    john.add_post(text_post)
    
    text_post.user == john  # Important!
    len(john.posts)
    >>> 1
    '''


    def get_timeline(self):
        timeline = []
        
        for friends in self.following:
            for tweet in friends.posts:
                timeline.append(tweet)
        return sorted(timeline, key=lambda tweets: tweets.timestamp, reverse = True)
    '''
    [a list of posts from each user that you are following]
    [user1, user2, user3] <- people your following
    get_timeline()
    [user1post1, user1post2, user2post1, user3post1, user3post2]
    RETURN POSTS SORTED BY TIMESTAMP  -----> https://wiki.python.org/moin/HowTo/Sorting
    
    
    print(john.get_timeline())
    >>> [<TextPost: Post 3>, <TextPost: Post 2>, <TextPost: Post 1> 
    '''


    def follow(self, other):
        self.following.append(other)
   
    