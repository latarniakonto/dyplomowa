FROM  python:3.8.13

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /IBFF
WORKDIR /IBFF
COPY . .

RUN rm -rf venv
RUN python -m venv venv
RUN . venv/bin/activate && pip install -r requirements.txt

EXPOSE 8000

RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["sh", "docker-entrypoint.sh"]
