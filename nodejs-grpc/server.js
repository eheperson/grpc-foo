const grpc = require("@grpc/grpc-js")
const protoLoader = require("@grpc/proto-loader")
const packageDef = protoLoader.loadSync("todo.proto", {});
const grpcObject = grpc.loadPackageDefinition(packageDef);
const todoPackage = grpcObject.todoPackage;

const server = new grpc.Server();
server.bindAsync("0.0.0.0:40000",
    grpc.ServerCredentials.createInsecure());

server.addService(
    todoPackage.Todo.service,
    {
        "createTodo": createTodo,
        "readTodos": readTodos,
    },
);

function createTodo(call, callback) {
    console.log(call);
    callback(null, null);
};

function readTodos(call, callback){
    console.log(call);
    callback(null, null);

};