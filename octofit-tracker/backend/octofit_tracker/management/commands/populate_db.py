from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data in correct order
        for obj in Activity.objects.all():
            if obj.id:
                obj.delete()
        for obj in Leaderboard.objects.all():
            if obj.id:
                obj.delete()
        for obj in Workout.objects.all():
            if obj.id:
                obj.delete()
        for obj in User.objects.all():
            if obj.id:
                obj.delete()
        for obj in Team.objects.all():
            if obj.id:
                obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=400, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Swimming', duration=60, calories=500, date=timezone.now().date())

        # Create workouts
        Workout.objects.create(name='Push Ups', description='Upper body workout', difficulty='Medium')
        Workout.objects.create(name='Squats', description='Lower body workout', difficulty='Easy')
        Workout.objects.create(name='Plank', description='Core workout', difficulty='Hard')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=250)
        Leaderboard.objects.create(team=dc, points=300)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
