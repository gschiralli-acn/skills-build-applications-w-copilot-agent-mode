from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.assertEqual(team.name, 'Marvel')

    def test_create_user(self):
        team = Team.objects.create(name='DC', description='DC superheroes')
        user = User.objects.create(name='Superman', email='superman@dc.com', team=team)
        self.assertEqual(user.team.name, 'DC')

    def test_create_activity(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, calories=300, date='2025-11-27')
        self.assertEqual(activity.user.name, 'Iron Man')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Push Ups', description='Upper body workout', difficulty='Medium')
        self.assertEqual(workout.name, 'Push Ups')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.team.name, 'Marvel')
