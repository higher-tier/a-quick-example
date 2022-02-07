# C8001 (missing-reverse-migration)
# Generated by Django 3.1.5 on 2021-01-31 18:09

from django.db import migrations


def migrate_unlocks(apps, schema_editor):
    Challenge = apps.get_model("challenge", "Challenge")
    for chall in Challenge.objects.all():
        unlocked_by = Challenge.objects.filter(unlocks__id__exact=chall.id).all()
        chall.unlock_requirements = ' '.join(
            [str(i.id) for i in unlocked_by] + ["OR" for _ in range(len(unlocked_by)-1)]
        )
        chall.save()


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0013_auto_20210130_0114'),
    ]

    operations = [
        migrations.RunPython(migrate_unlocks),
    ]