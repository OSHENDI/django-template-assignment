
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('university_id', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('salary', models.PositiveIntegerField()),
                ('photo', models.FileField(upload_to='photos/')),
            ],
        ),
    ]
