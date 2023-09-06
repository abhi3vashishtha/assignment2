import flatbuffers
import Clientmessage.Client as Client
import Clientmessage.ClientCollection as ClientCollection
import Clientmessage.ClientType as ClientType
import Clientmessage.Group as Group
import Clientmessage.Person as Person
import Clientmessage.Gender as Gender

#Conversion to String
str_ClientType = {
    ClientType.ClientType.Person: "Person",
    ClientType.ClientType.Group: "Group"
    }

str_Gender = {
    Gender.Gender.Male : "Male",
    Gender.Gender.Female : "Female"
}

#Function to Print Person
def PrintPerson(client):
    person = client.Person()
    print("===============================================================================")
    print("Client Type   :", str_ClientType[client.ClientType()])
    print("Name          :", person.Name().decode("utf-8"))
    print("Age           :", person.Age())
    print("Weight        :", person.Weight())
    print("Gender        :", str_Gender[person.Gender()])
    print("===============================================================================")

#Function to Print Group
def PrintGroup(client):
    group = client.Group()
    print("===============================================================================")
    print("Client Type   :", str_ClientType[client.ClientType()])
    print("Group Name    :", group.GroupName().decode("utf-8"))
    print("Average Age   :", group.AvgAge())
    print("Average Weight:", group.AvgWeight())
    print("Name List     :", [group.Names(i).decode("utf-8") for i in range(group.NamesLength())])
    print("===============================================================================")


#Function to print client
def PrintClient(client):
    if(client.ClientType() == ClientType.ClientType.Person):
        PrintPerson(client)
    elif(client.ClientType() == ClientType.ClientType.Group):
        PrintGroup(client)
    else:
        print("Client Type Not Valid")
    





buf = open('Data/clientData.bin', 'rb').read()
buf = bytearray(buf)
clientCollection = ClientCollection.ClientCollection.GetRootAs(buf, 0)
size = clientCollection.ClientsLength()


for i in range(size):
    client = clientCollection.Clients(i)
    PrintClient(client)




