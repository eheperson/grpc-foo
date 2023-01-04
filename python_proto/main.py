import google.protobuf.json_format as json_format

import proto.simple_pb2 as simple_pb2
import proto.complex_pb2 as complex_pb2
import proto.enumerations_pb2 as enumerations_pb2
import proto.oneofs_pb2 as oneofs_pb2
import proto.maps_pb2 as maps_pb2

def simple():
    """simple proto message in python"""
    message = simple_pb2.Simple(
        id=42,
        is_simple=True,
        name="enivicivokki",
        sample_lists=[1,2,4]
    )
    print(message)
    return message

def complex():
    """complex proto message in python"""
    message = complex_pb2.Complex()
    message.one_dummy.id = 42
    message.one_dummy.name = "enivicivokki complex"
    message.multiple_dummies.add(id=43, name="ehe1")
    message.multiple_dummies.add(id=44, name="ehe2")
    message.multiple_dummies.add(id=45, name="ehe3")
    print(message)
    return message

def enumerations():
    """enumerations in python"""
    message = enumerations_pb2.Enumeration(
        eye_color = enumerations_pb2.EYE_COLOR_GREEN
        # eye_color = 1
    )
    print(message)

def oneofs():
    """oneofs in python"""
    message = oneofs_pb2.Result(message="ehe message")
    print(message)

    # when you set a field value and the previous field was already set
    #  the previous field will be cleared
    # and new field will get the value
    message.id = 4
    print(message)

def maps():
    """maps in python"""
    message = maps_pb2.MapExample()

    # if theis key does not exists inside map
    # it will create one
    message.ids["id1"].id = 42
    message.ids["id12"].id = 43
    message.ids["id1"].id = 424
    print(message)

def readWriteToFile_asBinary(message):
    """write to file in python"""
    path = "simple.bin"

    print("writing to file : ")
    print(message)
    with open(path, "wb") as f:
        bytes_as_str = message.SerializeToString()
        f.write(bytes_as_str)

    print("Reading from file :")
    with open(path, "rb") as f:
        t = type(message)
        message2 = t().FromString(f.read())
        print(message2)

def readWriteToFile_asJson(message):
    def to_json(message):
        return json_format.MessageToJson(
            message,
            # indent=None,
            # preserving_proto_field_name=True
        )

    def from_json(json_str, type):
        return json_format.Parse(
            json_str, 
            type(),
            # ignore_unknown_fields=True
        )

    json_str = to_json(message)
    print(json_str)
    print(from_json(json_str, complex_pb2.Complex))

if __name__ == "__main__":
    print("Simple proto message example : ")
    simple()
    print(" - - - ")
    input("Press enter key to continue ...\n")

    print("Complex proto message example : ")
    complex()
    print(" - - - ")
    input("Press enter key to continue ...\n")

    print("Enumerations example : ")
    enumerations()
    print(" - - - ")
    input("Press enter key to continue ...\n")

    print("Oneofs example : ")
    oneofs()
    print(" - - - ")
    input("Press enter key to continue ...\n")

    print("Maps example : ")
    maps()
    print(" - - - ")
    input("Press enter key to continue ...\n")

    print("Write to file example (as binary): ")
    readWriteToFile_asBinary(simple())
    print(" - - - ")
    input("Press enter key to continue ...\n")

    print("Write to file example (as json): ")
    readWriteToFile_asJson(complex())
    print(" - - - ")
    input("Press enter key to continue ...\n")