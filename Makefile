PYTHON_DIR = python_proto
PYTHON_PROTO_DIR = ${PYTHON_DIR}/proto
PYTHON_VENV_DIR = ./venv

python_prepare:
	git checkout python\
	python3 -m venv venv\
	source ${PYTHON_VENV_DIR}/bin/activate\
    pip install --upgrade pip\
    pip install -r requirements.txt\
	# deactivate\

python_generate_protos:
	protoc -I${PYTHON_PROTO_DIR} --python_out=${PYTHON_PROTO_DIR} ${PYTHON_PROTO_DIR}/*.proto

python_run:
	source ${PYTHON_VENV_DIR}/bin/activate && python ${PYTHON_DIR}/main.py && deactivate

python_clean_protos:
	rm ${PYTHON_PROTO_DIR}/*_pb2.py