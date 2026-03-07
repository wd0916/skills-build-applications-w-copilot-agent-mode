import os
import django

def setup_django():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
    django.setup()

setup_django()

from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

# Create Teams
team1 = Team.objects.create(name='Alpha')
team2 = Team.objects.create(name='Beta')

# Create Users
user1 = User.objects.create(username='alice', email='alice@example.com', team=team1)
user2 = User.objects.create(username='bob', email='bob@example.com', team=team2)
user3 = User.objects.create(username='charlie', email='charlie@example.com', team=team1)

# Add members to teams
team1.members.add(user1, user3)
team2.members.add(user2)

# Create Activities
Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2026-03-07')
Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2026-03-07')
Activity.objects.create(user=user3, activity_type='Swimming', duration=20, date='2026-03-07')

# Create Workouts
Workout.objects.create(user=user1, workout_type='Yoga', suggested=True, date='2026-03-07')
Workout.objects.create(user=user2, workout_type='HIIT', suggested=False, date='2026-03-07')
Workout.objects.create(user=user3, workout_type='Pilates', suggested=True, date='2026-03-07')

# Create Leaderboard
Leaderboard.objects.create(team=team1, points=150)
Leaderboard.objects.create(team=team2, points=120)

print('Database populated with sample data.')
