FROM python:3.13.1

WORKDIR /app

# Venv config
ENV VENV_PATH="/opt/venv"
RUN python -m venv ${VENV_PATH}
ENV PATH="${VENV_PATH}/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Set .env
COPY .env .

# Another image
# FROM python:3.13.1

# COPY --from=builder ${VENV_PATH} ${VENV_PATH}

# WORKDIR /app

# ENV PATH="${VENV_PATH}/bin:$PATH"

# Run the app
COPY bot.py .
CMD [ "python", "./bot.py" ]