FROM python:3

COPY src/editor.py /app/

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "editor.py"]