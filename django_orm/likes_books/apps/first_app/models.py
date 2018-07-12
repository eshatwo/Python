from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return f'User(first_name = {self.first_name}, last_name = {self.last_name}, email = {self.email})'

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    uploaded_by = models.ForeignKey(User, related_name = 'uploads')
    liked_by = models.ManyToManyField(User, related_name = "books_liked")
    def __repr__(self):
        return f'Book(name = {self.name}, desc = {self.desc})'

# Create 3 different user accounts

    # user1= User.objects.create (first_name = 'Michael' ,last_name = 'Scott' , email = 'mscott@dundermifflin.com')
    # user2= User.objects.create(first_name = 'Jim' ,last_name = 'Halpert' , email = 'jhalpert@dundermifflin.com')
    # user3=User.objects.create(first_name = Dwight,last_name = Schrute, email = dschrute@dundermifflin.com)

# Have the first user create/upload 2 books.

    # book2 = Book.objects.create(name='Sabre', desc='Sabre history',uploaded_by=User.objects.get(id=1))

# Have the second user create/upload 2 other books.

    # book4 = Book.objects.create(name='Bears', desc='Bears and their habitat',uploaded_by=User.objects.get(id=2))
    # book3 = Book.objects.create(name='Life of Beets', desc='History of Beets',uploaded_by=User.objects.get(id=2))

# Have the third user create/upload 2 other books.

    # book5 = Book.objects.create(name='The Receptionist', desc='Office Romance',uploaded_by=User.objects.get(id=3))
    # book6 = Book.objects.create(name='Nigara Falls', desc='Wedding venues',uploaded_by=User.objects.get(id=3))


# Have the first user like the last book and the first book
    # User.objects.get(id=1).books_liked.add(Book.objects.last())
    # User.objects.get(id=1).books_liked.add(Book.objects.first())

# Have the second user like the first book and the third book
    #  User.objects.get(id=2).books_liked .add(Book.objects.first())
    #  User.objects.get(id=2).books_liked .add(Book.objects.get(id=3))

# Have the third user like all books
    # User.objects.get(id=3).books_liked=Book.objects.all()

# Display all users who like the first book
    # Book.objects.first().liked_by.all()

# Display the user who uploaded the first book
    # Book.objects.first().uploaded_by

# Display all users who like the second book
    # Book.objects.get(id=2).liked_by.all()

# Display the user who uploaded the second book
    # Book.objects.get(id=2).uploaded_by