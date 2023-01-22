FROM archlinux

COPY src/editor.py /app/
COPY requirements.txt /app/

WORKDIR /app

RUN pacman -Syu --noconfirm python python-pip
RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt

ENV FILE arg1
CMD ["python3", "/app/src/editor.py", "$FILE"]
