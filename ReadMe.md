

## Setup Protoc Compiler : 

* MacOS: 
```
    $ brew install protobuf
```
* Linux: 
```
    $ curl -O https://github.com/protocolbuffers/protobuf/releases/download/v21.12/protoc-21.12-linux-x86_64.zip
    $ unzip protoc-21.12-linux-x86_64.zip
    $ sudo mv protoc3/bin/* /usr/local/bin/
    $ sudo chown -R [user] /usr/local/include/google
```
* Windows :
```
    # Will be added soon..
```

## How To Use the Compiler : 
* `$ protoc` : display help screen
* `$ protoc --cpp_out=. *.proto` : generate codes for cpp in *./cpp* directory, use proto files from the active directory
* `$ protoc --java_out=. *.proto` : generate codes for java in *./java* directory, use proto files from the active directory
* `$ protoc --java_out=java --python_out=python proto/simple.proto` : generate codes for java in *./java* directory for cpp in *./cpp* directory and use *./proto/simple.proto* file


## Prepare Language Specific Environments:
```
    $ git clone <>
```

* python :
```
    $ git checkout python
    $ python3 -m venv venv
    $ source ./venv/bin/activate
    $ pip install --upgrade pip
    $ pip install -r requirements.txt

    # or just irun this command if you have mac on your dev env : 
    $ make prepare_python
```

make
protoc -Iproto --python_out=proto proto/*.proto