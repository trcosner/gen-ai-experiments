# Using a miniconda base image (matches the book repository):
FROM continuumio/miniconda3:23.9.0-0

ENV PIP_DEFAULT_TIMEOUT=1000

RUN apt-get update && apt-get install -y pandoc wget build-essential git vim cmake pkg-config libclang-dev && rm -rf /var/lib/apt/lists/*

# Update the environment:
COPY requirements.txt .

# I was sometimes running into errors with hashes:
RUN python -m pip install --upgrade pip && pip cache purge

# This is to avoid getting the GPU torch version. Please remove the index option, if you have a GPU:
RUN pip install torch>=1.11.0 --extra-index-url https://download.pytorch.org/whl/cpu

# Avoid any hash conflicts and extra time compiling:
RUN pip install --prefer-binary --no-cache-dir -r requirements.txt

# Copy requirements.txt to container for runtime validation
COPY requirements.txt /requirements.txt

WORKDIR /src

# Note: All source code including config files will be volume mounted
# No need to copy them at build time

# Start with an interactive bash shell for development
CMD ["bash"]