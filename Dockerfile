# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot source code
COPY . .

# Set environment variables (optional)
# ENV DISCORD_TOKEN=your_token_here

# Command to run the bot
CMD ["python", "main.py"]
