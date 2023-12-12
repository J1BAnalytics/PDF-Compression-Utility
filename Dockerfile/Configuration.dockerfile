# Use a base image (for example, Python)
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Command to run the compression script (adjust as needed)
CMD ["python", "scripts/compress_pdf.py"]
