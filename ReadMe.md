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

---

## How To Use the Compiler : 
* `$ protoc` : display help screen
* `$ protoc --cpp_out=. *.proto` : generate codes for cpp in *./cpp* directory, use proto files from the active directory
* `$ protoc --java_out=. *.proto` : generate codes for java in *./java* directory, use proto files from the active directory
* `$ protoc --java_out=java --python_out=python proto/simple.proto` : generate codes for java in *./java* directory for cpp in *./cpp* directory and use *./proto/simple.proto* file

---

## Useful informations
**--decode_raw**
> Read an arbitrary protocol message from standard input and write the raw tag/value pairs in text format to standard output.  No PROTO_FILES should be given when using this flag.
```shell
# example
cd 03-protoc-arguments
cat simple.bin | protoc --decode_raw
```

**--decode**
> Read a binary message of the given type from standard input and write it in text format to standard output.  The message type must be defined in PROTO_FILES or their imports.
```shell
# example usage
cd 03-protoc-arguments
cat simple.bin | protoc --decode=Simple simple.proto > simple.txt
cat simple.bin | protoc --decode=simple.Simple simple.proto > simple.txt
```

**--encode**
> Read a text-format message of the given type from standard input and write it in binary to standard output.  The message type must be defined in PROTO_FILES or their imports.
```shell
cd 03-protoc-arguments
cat simple.txt | protoc --encode=Simple simple.proto > simple.pb
cat simple.txt | protoc --encode=simple.Simple simple.proto > simple.pb
```

---

## List of Protocol Buffers to Explore
* **Main repository examples:** https://github.com/protocolbuffers/protobuf/tree/main/examples
* **Some Google Apis types:** https://github.com/googleapis/googleapis/tree/master/google/type
* *Protocol Buffer itself (may be very complex):* https://github.com/protocolbuffers/protobuf/tree/main/src/google/protobuf