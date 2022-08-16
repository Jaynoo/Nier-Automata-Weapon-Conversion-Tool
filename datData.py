import math
import binaryUtils as utils

class DatData:
    #parsing
    def __init__(self, datPath):
        datFile = open(datPath, "rb")
        #header
        self.id = datFile.read(4)
        self.fileNumber = utils.read_uint32(datFile)
        self.fileOffsetsOffset = utils.read_uint32(datFile)
        self.fileExtensionsOffset = utils.read_uint32(datFile)
        self.fileNamesOffset = utils.read_uint32(datFile)
        self.fileSizesOffset = utils.read_uint32(datFile)
        self.hashMapOffset = utils.read_uint32(datFile)

        #fileOffsets
        self.fileOffsets = []
        datFile.seek(self.fileOffsetsOffset)
        for i in range(self.fileNumber):
            self.fileOffsets.append(utils.read_uint32(datFile))
        
        #fileExtensions
        self.fileExtensions = []
        datFile.seek(self.fileExtensionsOffset)
        for i in range(self.fileNumber):
            self.fileExtensions.append(datFile.read(4))
        
        datFile.seek(self.fileNamesOffset)
        #nameLength
        self.nameLength = utils.read_uint32(datFile)

        #fileNames
        self.fileNames = []
        for i in range(self.fileNumber):
            self.fileNames.append(datFile.read(self.nameLength))

        #fileSizes
        self.fileSizes = []
        datFile.seek(self.fileSizesOffset)
        for i in range(self.fileNumber):
            self.fileSizes.append(utils.read_uint32(datFile))
        
        #hashMap
        datFile.seek(self.hashMapOffset)
        self.hashMap = datFile.read(self.fileOffsets[0] - self.hashMapOffset)

        #files
        self.files = []
        for i in range(self.fileNumber):
            datFile.seek(self.fileOffsets[i])
            self.files.append(datFile.read(self.fileSizes[i]))
        
        #
        datFile.close()
    

    #### shitting a file ####
    def shitaDat(self, whereToShit):
        shit = open(whereToShit, "wb")

        self.fileOffsets = []
        
        curOffset = self.hashMapOffset + len(self.hashMap)
        for i in range(self.fileNumber):
            curOffset = (math.ceil(curOffset / 16)) * 16
            self.fileOffsets.append(curOffset)
            curOffset += len(self.files[i])
        
        #header
        shit.write(self.id)
        utils.write_uint32(shit, self.fileNumber)
        utils.write_uint32(shit, self.fileOffsetsOffset)
        utils.write_uint32(shit, self.fileExtensionsOffset)
        utils.write_uint32(shit, self.fileNamesOffset)
        utils.write_uint32(shit, self.fileSizesOffset)
        utils.write_uint32(shit, self.hashMapOffset)

        #fileOffsets
        shit.seek(self.fileOffsetsOffset)
        for i in range(self.fileNumber):
            utils.write_uint32(shit, self.fileOffsets[i])
        
        #fileExtensions
        shit.seek(self.fileExtensionsOffset)
        for i in range(self.fileNumber):
            shit.write(self.fileExtensions[i])

        shit.seek(self.fileNamesOffset)


        #nameLength
        utils.write_uint32(shit, self.nameLength)

        #fileNames
        for i in range(self.fileNumber):
            shit.write(self.fileNames[i])

        #filesizes
        shit.seek(self.fileSizesOffset)
        for i in range(self.fileNumber):
            utils.write_uint32(shit, len(self.files[i]))

        #hashMap
        shit.seek(self.hashMapOffset)
        shit.write(self.hashMap)

        #files
        for i in range(self.fileNumber):
            shit.seek(self.fileOffsets[i])
            shit.write(self.files[i])
        
        #peak fucking math right here
        budgetEOF = (math.ceil(shit.tell() / 16)) * 16
        shit.seek(budgetEOF-1)
        shit.write(b"\x00")
        
        print("shat out here: " + shit.name)
        shit.close()