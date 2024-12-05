from django.db import models

class Album(models.Model):
    STAR_RATINGS = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]

    album_name = models.CharField(max_length=200)
    musician = models.ForeignKey(
        'musician_app.Musician',
        on_delete=models.CASCADE,
        related_name='albums'
    )
    release_date = models.DateField()
    rating = models.PositiveSmallIntegerField(choices=STAR_RATINGS)

    def __str__(self):
        return self.album_name
