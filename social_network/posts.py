from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.user = None
        if timestamp is None:
            self.timestamp = datetime.now()
        else:
            self.timestamp = timestamp

    def set_user(self, user):
        self.user = user


class TextPost(Post):  
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    def __str__(self):
        return '@' + self.user.first_name + ' ' + self.user.last_name + ':' + ' ' + '"' + self.text + '"' + '\n\t' + '{0:%A}, {0:%b} {0:%d}, {0:%Y}'.format(self.timestamp)

#            '@Kevin Watson: "Sample post text"\n\tTuesday, Jan 10, 2017'



class PicturePost(Post):  
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url
        
    def __str__(self):
        return '@' + self.user.first_name + ' ' + self.user.last_name + ':' + ' ' + '"' + self.text + '"' + '\n\t' + self.image_url + '\n\t' + '{0:%A}, {0:%b} {0:%d}, {0:%Y}'.format(self.timestamp)

#            '@Kevin Watson: "Sample post text"\n\thttp://fake-domain.com/images/sample.jpg\n\tTuesday, Jan 10, 2017'


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude
        
    def __str__(self):
         return '@' + self.user.first_name + ' Checked In: ' + '"' + self.text + '"' + '\n\t'+ str(self.latitude) + ', ' + str(self.longitude) + '\n\t' + '{0:%A}, {0:%b} {0:%d}, {0:%Y}'.format(self.timestamp)


#            '@Kevin Checked In: "Sample post text"\n\t-34.603722, -58.381592\n\tTuesday, Jan 10, 2017'
