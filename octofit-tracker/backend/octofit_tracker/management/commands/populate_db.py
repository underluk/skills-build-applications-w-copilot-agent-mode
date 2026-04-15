from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# MODELE TESTOWE
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    score = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Usuń stare dane
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Dodaj drużyny
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Dodaj użytkowników
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass', first_name='Peter', last_name='Parker'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='pass', first_name='Diana', last_name='Prince'),
        ]

        # Dodaj aktywności
        Activity.objects.create(name='Bieganie', user='ironman', team='Marvel')
        Activity.objects.create(name='Pływanie', user='spiderman', team='Marvel')
        Activity.objects.create(name='Jazda na rowerze', user='batman', team='DC')
        Activity.objects.create(name='Joga', user='wonderwoman', team='DC')

        # Dodaj leaderboard
        Leaderboard.objects.create(user='ironman', team='Marvel', score=100)
        Leaderboard.objects.create(user='spiderman', team='Marvel', score=80)
        Leaderboard.objects.create(user='batman', team='DC', score=90)
        Leaderboard.objects.create(user='wonderwoman', team='DC', score=95)

        # Dodaj treningi
        Workout.objects.create(name='Trening siłowy', description='Ćwiczenia na siłę', user='ironman')
        Workout.objects.create(name='Trening wytrzymałościowy', description='Ćwiczenia na wytrzymałość', user='spiderman')
        Workout.objects.create(name='Trening szybkościowy', description='Ćwiczenia na szybkość', user='batman')
        Workout.objects.create(name='Trening równowagi', description='Ćwiczenia na równowagę', user='wonderwoman')

        self.stdout.write(self.style.SUCCESS('Baza octofit_db została wypełniona przykładowymi danymi!'))
