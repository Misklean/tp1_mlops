# Use an official Python image as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the necessary dependencies
RUN pip install --no-cache-dir fastapi uvicorn joblib scikit-learn pydantic

# Expose the port that FastAPI will use (use port 8000 inside the container)
EXPOSE 5462

# Command to run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5462", "--reload"]
