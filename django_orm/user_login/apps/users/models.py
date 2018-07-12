from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return f'User(first_name = {self.first_name}, last_name = {self.last_name}, email = {self.email}, age = {self.age})'

# Know how to retrieve all users.

    # User.objects.all()

# Know how to get the last user.

    # User.objects.last()

# Create a few records in the users.

    # user1 = User.objects.create(first_name = 'Esha', last_name = 'Aggarwal', email = 'eshatwo@gmail.com', age = 17)
    # user1.save()

    # user2 = User.objects.create(first_name = 'Harry', last_name = 'Styles', email = 'harrystyles@gmail.com', age = 24)
    # user2.save()

    # user3 = User.objects.create(first_name = 'Niall', last_name = 'Horan', email = 'niallhoran@gmail.com', age = 24)
    # user3.save()

# Know how to get the first user.

    # User.objects.first()

# Know how to get the users sorted by their first name (order by first_name DESC)

    # User.objects.order_by('-first_name').values('first_name')

# Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. Know how to do this directly in the console using .get and .save.

    # a = User.objects.get(id=3)
    # a.last_name = 'Haron'
    # a.save()

# Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...).

    # User.objects.get(id=4).delete()