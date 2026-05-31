FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install streamlit pandas plotly
EXPOSE 8080
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0", "--server.headless=true"]
