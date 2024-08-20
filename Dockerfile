# Base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /usr/src/app

#RUN apk update \
#    && apk add postgresql-dev gcc python3-dev zlib-dev jpeg-dev musl-dev ffmpeg libffi-dev libressl-dev openssl-dev  \
#    freetype-dev libjpeg freetype-dev libjpeg-turbo-dev libjpeg-turbo gettext gettext-dev cairo-dev pango-dev fontconfig ttf-dejavu \
#    pango cairo gdk-pixbuf py3-cffi py3-pillow nodejs npm py-pip

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8000", "news_project.wsgi:application"]
