from django.shortcuts import render
from musician_app.models import Musician
from album_app.models import Album

def home(request):
    musicians = Musician.objects.all()  # Fetch all musicians
    albums = Album.objects.all()  # Fetch all albums
    data = []

    # Merge musicians and their albums for the table
    for musician in musicians:
        musician_albums = albums.filter(musician=musician)
        for album in musician_albums:
            data.append({
                'id': musician.id,
                'name': f"{musician.first_name} {musician.last_name}",
                'email': musician.email,
                'phone': musician.phone,
                'instrument_type': musician.instrument_type,
                'album_name': album.album_name,
                'release_date': album.release_date,
                'rating': album.rating,
            })

    return render(request, 'home.html', {'data': data})
