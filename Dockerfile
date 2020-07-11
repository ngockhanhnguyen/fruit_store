FROM python:3.6-slim-stretch

ARG app_name=fruitst_api

RUN apt-get update
RUN apt-get install -y gcc python3-dev
RUN apt-get install net-tools

RUN mkdir -p /opt/${app_name}
COPY ./requirements.txt /opt/${app_name}

WORKDIR /opt/${app_name}
RUN pip install --no-cache-dir --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org -r requirements.txt

RUN mkdir -p /opt/${app_name}/logs

COPY ./configs.py /opt/${app_name}
COPY ./logger.conf /opt/${app_name}
ADD ./fruitst /opt/${app_name}/fruitst

CMD ["python", "-m", "fruitst"]