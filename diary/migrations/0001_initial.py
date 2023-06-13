# Generated by Django 4.2.1 on 2023-06-13 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Note",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="노트이름")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("1", "코랄핑크표지"),
                            ("2", "브라운표지"),
                            ("3", "노랑표지"),
                            ("4", "초록표지"),
                            ("5", "파랑표지"),
                            ("6", "보라표지"),
                            ("7", "그라데이션-블루퍼플"),
                            ("8", "검정표지"),
                            ("9", "그레이블루표지"),
                            ("10", "그라데이션-블루옐로"),
                            ("11", "그라데이션-보라그레이"),
                            ("12", "그라데이션-핑크베이지"),
                        ],
                        default=1,
                        max_length=10,
                        verbose_name="노트표지",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성일"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("0", "활성화"),
                            ("1", "비활성화"),
                            ("2", "강제중지"),
                            ("3", "삭제"),
                        ],
                        default=0,
                        max_length=10,
                        verbose_name="상태",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.usergroup"
                    ),
                ),
            ],
            options={
                "db_table": "note",
            },
        ),
        migrations.CreateModel(
            name="PhotoPage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
                ("location", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("memo", models.CharField(max_length=100, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("0", "활성화"),
                            ("1", "비활성화"),
                            ("2", "강제중지"),
                            ("3", "삭제"),
                        ],
                        default=0,
                        max_length=100,
                    ),
                ),
                ("location_x", models.CharField(max_length=100)),
                ("location_y", models.CharField(max_length=100)),
                (
                    "diary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="diary.note"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stamp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("0", "활성화"),
                            ("1", "비활성화"),
                            ("2", "강제중지"),
                            ("3", "삭제"),
                        ],
                        default=0,
                        max_length=100,
                    ),
                ),
                (
                    "photo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="diary.photopage",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PlanPage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start", models.DateField()),
                ("title", models.CharField(max_length=100)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("time", models.CharField(blank=True, max_length=255, null=True)),
                ("memo", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("0", "활성화"),
                            ("1", "비활성화"),
                            ("2", "강제중지"),
                            ("3", "삭제"),
                        ],
                        default=0,
                        max_length=100,
                    ),
                ),
                (
                    "diary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="diary.note"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.CharField(max_length=256)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("0", "활성화"),
                            ("1", "비활성화"),
                            ("2", "강제중지"),
                            ("3", "삭제"),
                        ],
                        default=0,
                        max_length=100,
                    ),
                ),
                (
                    "photo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="diary.photopage",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
