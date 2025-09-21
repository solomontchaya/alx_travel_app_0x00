import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        # Create sample users if none exist
        if not User.objects.exists():
            User.objects.create_user(username='alice', password='password123')
            User.objects.create_user(username='bob', password='password123')

        users = User.objects.all()

        # Create 10 sample listings
        for i in range(1, 11):
            Listing.objects.create(
                title=f"Sample Listing {i}",
                description=f"This is the description for listing {i}.",
                location=f"City {random.randint(1, 10)}",
                price_per_night=random.randint(50, 500),
                host=random.choice(users)
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database!"))
