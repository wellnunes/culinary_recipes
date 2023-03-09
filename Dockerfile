FROM python:3.11

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["python3"]

RUN python ./manage.py migrate

RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python ./manage.py shell

CMD ["manage.py", "runserver", "0.0.0.0:8000"]