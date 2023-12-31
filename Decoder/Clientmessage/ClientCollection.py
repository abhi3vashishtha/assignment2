# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Clientmessage

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ClientCollection(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ClientCollection()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsClientCollection(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ClientCollection
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ClientCollection
    def Clients(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Clientmessage.Client import Client
            obj = Client()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ClientCollection
    def ClientsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ClientCollection
    def ClientsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def ClientCollectionStart(builder):
    builder.StartObject(1)

def Start(builder):
    ClientCollectionStart(builder)

def ClientCollectionAddClients(builder, clients):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(clients), 0)

def AddClients(builder, clients):
    ClientCollectionAddClients(builder, clients)

def ClientCollectionStartClientsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartClientsVector(builder, numElems: int) -> int:
    return ClientCollectionStartClientsVector(builder, numElems)

def ClientCollectionEnd(builder):
    return builder.EndObject()

def End(builder):
    return ClientCollectionEnd(builder)
