

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

brew install protobuf
protoc -Iproto --python_out=proto proto/*.proto