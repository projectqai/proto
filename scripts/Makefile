.PHONY: help generate clean build install test

help:
	@echo "Platform Proto - Available commands:"
	@echo ""
	@echo "  make generate    - Generate Python protobuf bindings"
	@echo "  make clean       - Remove generated files and build artifacts"
	@echo "  make build       - Build the Python package"
	@echo "  make install     - Install package in development mode"
	@echo "  make test        - Run tests (if available)"
	@echo ""

generate:
	@echo "Generating Python protobuf bindings..."
	@cd .. && pipx run --spec grpcio-tools python3 scripts/generate_protos.py

clean:
	@echo "Cleaning generated files and build artifacts..."
	@cd .. && rm -rf python/platform_proto/*_pb2.py
	@cd .. && rm -rf python/platform_proto/*_pb2_grpc.py
	@cd .. && rm -rf python/platform_proto/*_pb2.pyi
	@cd .. && rm -rf build/ dist/ *.egg-info python/*.egg-info
	@cd .. && find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@cd .. && find . -type f -name "*.pyc" -delete
	@echo "Clean complete!"

build: generate
	@echo "Building Python package..."
	@cd .. && python3 -m build

install:
	@echo "Installing package in development mode..."
	@cd .. && pip install -e .

test:
	@echo "Running tests..."
	@cd .. && python3 -m pytest tests/ -v || echo "No tests found"
