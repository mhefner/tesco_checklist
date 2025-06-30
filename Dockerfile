FROM python:3.11-slim

WORKDIR /app
COPY tesco_list.py /app/

RUN pip install --no-cache-dir flask pymupdf

EXPOSE 5000
CMD ["python", "tesco_list.py"]
