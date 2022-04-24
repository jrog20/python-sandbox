FROM python

# base image
RUN pip install flask

# Create and cd into new directory
# WORKDIR ./src

# add onto our image
COPY ./index.py ./index.py

CMD ["python", "index.py"]