from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return f'Dojo(name = {self.name}, city = {self.city}, state = {self.state})'

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    dojo_name = models.ForeignKey(Dojo, related_name = 'ninjas')
    def __repr__(self):
        return f'Ninja(first_name = {self.first_name}, last_name = {self.last_name})'

# Create 3 dojos

    # d1 = Dojo.objects.create(name = 'CodingDojo Silicon Valley', city = 'Mountain View', state = 'CA')
    # d2 = Dojo.objects.create(name = 'CodingDojo Seattle', city = 'Seattle', state = 'WA')  
    # d3 = Dojo.objects.create(name = 'CodingDojo New York', city = 'New York', state = 'NY')

# Delete the three dojos you created (e.g. Dojo.objects.get(id=1).delete())

    # Dojo.objects.get(id=1).delete()
    # Dojo.objects.get(id=2).delete()
    # Dojo.objects.get(id=3).delete()

# Create 3 additional dojos by using Dojo.objects.create

    # d1 = Dojo.objects.create(name = 'CodingDojo Silicon Valley', city = 'Mountain View', state = 'CA')
    # d2 = Dojo.objects.create(name = 'CodingDojo Seattle', city = 'Seattle', state = 'WA')  
    # d3 = Dojo.objects.create(name = 'CodingDojo New York', city = 'New York', state = 'NY')

# Create 3 ninjas that belong to the first dojo you created.

    # ninja1 = Ninja.objects.create(first_name = 'Rachel', last_name = 'Green', dojo_name = Dojo.objects.first())
    # ninja2 = Ninja.objects.create(first_name = 'Phoebe', last_name = 'Buffay', dojo_name = Dojo.objects.first())
    # ninja3 = Ninja.objects.create(first_name = 'Chandler', last_name = 'Bing', dojo_name = Dojo.objects.first())

# Create 3 more ninjas and have them belong to the second dojo you created.

    # ninja4 = Ninja.objects.create(first_name = 'Joey', last_name = 'Tribbiani', dojo_name = Dojo.objects.get(id=2))
    # ninja5 = Ninja.objects.create(first_name = 'Monica', last_name = 'Geller', dojo_name = Dojo.objects.get(id=2))
    # ninja6 = Ninja.objects.create(first_name = 'Ross', last_name = 'Geller', dojo_name = Dojo.objects.get(id=2))

# Create 3 more ninjas and have them belong to the third dojo you created.

    # ninja7 = Ninja.objects.create(first_name = 'Emily', last_name = 'Waltham', dojo_name = Dojo.objects.get(id=3))
    # ninja8 = Ninja.objects.create(first_name = 'Pete', last_name = 'Becker', dojo_name = Dojo.objects.get(id=3))
    # ninja9 = Ninja.objects.create(first_name = 'Richard', last_name = 'Burke', dojo_name = Dojo.objects.get(id=3))

# Be able to retrieve all ninjas that belong to the first Dojo

    # Dojo.objects.first().ninjas.all()

# Be able to retrieve all ninjas that belong to the last Dojo

    # Dojo.objects.last().ninjas.all()