FROM registry.access.redhat.com/ubi9/python-39:1-117.1684741281

EXPOSE 8080/tcp
ENV FLASK_PORT=8080
ENV OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
ENV OTEL_EXPORTER_OTLP_TRACES_ENDPOINT="http://tempo-sample.openshift-tempo-operator.svc:4317"
ENV OTEL_SERVICE_NAME=rolldice

# Set the working directory in the container
WORKDIR /projects

# Copy the content of the local src directory to the working directory
COPY . .

# Install any dependencies
RUN \
  if [ -f requirements.txt ]; \
    then pip install -r requirements.txt; \
  elif [ `ls -1q *.txt | wc -l` == 1 ]; \
    then pip install -r *.txt; \
  fi

# Specify the command to run on container start
CMD ["opentelemetry-instrument", "--log_level", "debug", "--logs_exporter", "otlp", "flask", "run", "--debug", "--host", "0.0.0.0", "-p", "8080"]
