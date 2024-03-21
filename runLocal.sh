#!/bin/bash

export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT="http://otel.jaeger.svc:4317" 
export OTEL_SERVICE_NAME=rolldice_$(date +'%y%m%d%H%M%S')
opentelemetry-instrument --log_level debug --logs_exporter otlp flask run -p 8080
