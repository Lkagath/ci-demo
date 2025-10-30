# Dockerfile - FastAPI app
FROM python:3.11-slim

# avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# set a working directory
WORKDIR /app

# copy requirements first (cache layer)
COPY requirements.txt .

# install dependencies
RUN python -m pip install --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt

# copy the rest of the code
COPY . .

# expose the port the app will run on
EXPOSE 8000

# default command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
