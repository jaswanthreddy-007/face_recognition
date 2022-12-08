FROM python:3.7
WORKDIR K:\Hackathon\face_recognition
COPY requirements.txt .
RUN apt update -y
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt install python3 -y
RUN apt-get install -y cmake
RUN pip install --no-cache-dir -r requirements.txt
COPY Elon_Musk_2015.jpg  .
COPY . .

CMD [ "python", "./face_rec.py" ]
