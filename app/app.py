from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

REQUEST_COUNT = Counter('request_count_total', 'Total Request Count')
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency')

@app.route("/")
def home():
    start = time.time()

    REQUEST_COUNT.inc()
    time.sleep(0.2)   # simulate processing

    REQUEST_LATENCY.observe(time.time() - start)

    return "Hello Monitoring Project!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)