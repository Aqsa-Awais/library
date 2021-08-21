FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /library
WORKDIR /library
ADD . /library
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
RUN pipenv install --system --dev
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
