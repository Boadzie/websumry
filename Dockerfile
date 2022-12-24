FROM python:3.10.6

# create working directory
WORKDIR /code

# copy requirements.txt
COPY ./requirements.txt /code/requirements.txt

# install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy app to app in container app folder
COPY ./ /code

# run the app
CMD ["uvicorn", "app:api", "--host", "0.0.0.0", "--port", "8000"]
