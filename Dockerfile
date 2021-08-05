FROM python:3.9

ADD uploadpicturebot-en.py /tmp

COPY requirements.txt /tmp

WORKDIR /tmp

RUN pip install -r requirements.txt

CMD ["python","/tmp/uploadpicturebot-en.py"]