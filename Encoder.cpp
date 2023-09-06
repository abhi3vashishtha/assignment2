
#include <iostream>
#include<fstream>
#include <vector>
#include <flatbuffers/flatbuffers.h>
#include "include/client_generated.h"

using namespace Clientmessage;

int main()
{

    flatbuffers::FlatBufferBuilder builder;
    
    //Populating Person
    flatbuffers::Offset<Person> person = CreatePerson(builder, builder.CreateString("Ram"), 21, 76.5, Gender_Male);
    
    //Creating Client one
    flatbuffers::Offset<Client> client_one = CreateClient(builder, ClientType_Person, person);

    std::vector<flatbuffers::Offset<flatbuffers::String> > names = { builder.CreateString("Ram"), builder.CreateString("Shyam"), builder.CreateString("Raghuveer")};

    //Creating Group
    flatbuffers::Offset<Group> group = CreateGroup(builder, builder.CreateString("FlightClub"), 24.5, 66, builder.CreateVector(names));

    //Creating Client two
    flatbuffers::Offset<Client> client_two = CreateClient(builder, ClientType_Group, 0, group);

    std::vector<flatbuffers::Offset<Client>> clients = { client_one, client_two };

    //Finishing building the buffer
    builder.Finish(CreateClientCollection(builder, builder.CreateVector(clients)));

    uint8_t* buf = builder.GetBufferPointer();
    int size = builder.GetSize();

    //Storing it in file clientData.bin
    std::ofstream outFile("Decoder/Data/clientData.bin", std::ios::binary);
    if (!outFile) {
        std::cerr << "Failed to open output file." << std::endl;
        return 1;
    }

    outFile.write(reinterpret_cast<const char*>(buf), size);

    outFile.close();
}
