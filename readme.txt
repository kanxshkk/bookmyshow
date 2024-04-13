1. Open the Django shell:
python manage.py shell

2. Run the following commands to create sample movies and show timings:
```python
from datetime import date, datetime
from main.models import Movie, ShowTiming

movie1 = Movie.objects.create(title='Movie 1', language='English', description='Description of Movie 1', release_date=date(2024, 4, 15), duration=120)
movie2 = Movie.objects.create(title='Movie 2', language='French', description='Description of Movie 2', release_date=date(2024, 4, 20), duration=90)
movie3 = Movie.objects.create(title='Movie 3', language='Spanish', description='Description of Movie 3', release_date=date(2024, 4, 25), duration=110)
movie4 = Movie.objects.create(title='Movie 4', language='German', description='Description of Movie 4', release_date=date(2024, 4, 30), duration=100)
movie5 = Movie.objects.create(title='Movie 5', language='Spanish', description='Description of Movie 3', release_date=date(2024, 4, 25), duration=110)
ShowTiming.objects.create(movie=movie1, date=date(2024, 4, 15), time=datetime.strptime('10:00', '%H:%M').time())
ShowTiming.objects.create(movie=movie1, date=date(2024, 4, 15), time=datetime.strptime('14:00', '%H:%M').time())
ShowTiming.objects.create(movie=movie2, date=date(2024, 4, 15), time=datetime.strptime('10:00', '%H:%M').time())
ShowTiming.objects.create(movie=movie2, date=date(2024, 4, 15), time=datetime.strptime('14:00', '%H:%M').time())
ShowTiming.objects.create(movie=movie3, date=date(2024, 4, 25), time=datetime.strptime('12:00', '%H:%M').time())
ShowTiming.objects.create(movie=movie3, date=date(2024, 4, 25), time=datetime.strptime('16:00', '%H:%M').time())
ShowTiming.objects.create(movie=movie4, date=date(2024, 4, 30), time=datetime.strptime('11:00', '%H:%M').time())
ShowTiming.objects.create(movie=movie4, date=date(2024, 4, 30), time=datetime.strptime('15:00', '%H:%M').time())
ShowTiming.objects.create(movie=movie5, date=date(2024, 4, 30), time=datetime.strptime('15:00', '%H:%M').time())