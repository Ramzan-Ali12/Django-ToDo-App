from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# create the profile model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar=models.ImageField(default='avatar.jpg',upload_to='profile_avatars')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # save the profile first
    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        print("Image",img)
        print("Image Height",img.height)
        print("Image Width",img.width)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)

