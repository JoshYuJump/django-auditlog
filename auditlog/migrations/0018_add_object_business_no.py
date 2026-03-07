from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auditlog", "0017_add_actor_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="logentry",
            name="object_business_no",
            field=models.CharField(
                blank=True,
                db_index=True,
                max_length=128,
                null=True,
                verbose_name="object business no",
            ),
        ),
    ]

