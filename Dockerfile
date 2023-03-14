FROM python:3.9


# Copy and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

RUN pip install cryptography

# Copy the app code into the container
COPY . /app

# Set the working directory
WORKDIR /app

EXPOSE 5001

CMD ["python", "app.py"]


# docker image build -t coffee_shop .
# docker run -p 5000:5000 -d coffee_shop