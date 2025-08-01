from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a default admin user'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin',
                full_name='Super Admin',
                role='admin',
                address='Admin HQ',
                contact_number='7990596833',
                is_approved=True
            )
            self.stdout.write(self.style.SUCCESS('✅ Admin user created'))
        else:
            self.stdout.write(self.style.WARNING('⚠️ Admin user already exists'))