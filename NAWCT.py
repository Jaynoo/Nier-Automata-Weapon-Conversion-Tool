#hi hello :)
import datData as dd
import os
import sys

#so ok this is not really meant to be read so sorry it looks like shit

#sorting
smallSwords = ["wp0003", "wp0013", "wp0020", "wp0040", "wp0030", "wp0050", "wp0060", "wp0070", "wp0071", "wp0080", "wp0090", "wp0075", "wp0076"]
largeSwords = ["wp0203", "wp0213", "wp0220", "wp0230", "wp0240", "wp0250", "wp0260", "wp0261", "wp0270"]
spears = ["wp0400", "wp0420", "wp0430", "wp0440", "wp0450", "wp0460", "wp0470", "wp0471", "wp0480"]
combatBracers = ["wp0640", "wp0630", "wp0610", "wp0620", "wp0621", "wp0650", "wp0655"]
sortedWeapons = [smallSwords, largeSwords, spears, combatBracers]

#mmm inputs
with open('config.ini', mode='r', encoding='utf-8') as configFile:
    #haha copypaste go brrrrrrrrr
    small = configFile.readline().split(":")[1].strip()
    if small not in smallSwords:
        sys.exit("There is no such Small sword")

    large = configFile.readline().split(":")[1].strip()
    if large not in largeSwords:
        sys.exit("There is no such Large sword")

    spear = configFile.readline().split(":")[1].strip()
    if spear not in spears:
        sys.exit("There is no such Spear")
        
    bracer = configFile.readline().split(":")[1].strip()
    if bracer not in combatBracers:
        sys.exit("There is no such Combat Bracer")
    inputWeapons = [small, large, spear, bracer]
configFile.close()

targetPath = "weapons/"
def swapDat(target, mod):
    targetData = dd.DatData(target)
    modData = dd.DatData(mod)
    for i, name in enumerate(modData.fileNames):
        extName = name.decode("utf-8").split(".")[1][:3]
        if extName == "wta":
            targetData.files[i] = modData.files[i]
            break
    targetData.shitaDat(os.path.join(os.path.dirname(mod), os.path.basename(target)))

def swapDtt(target, mod):
    targetData = dd.DatData(target)
    modData = dd.DatData(mod)
    targetWMBindex = -1
    targetWTPindex = -1
    for i, name in enumerate(targetData.fileNames):
        extName = name.decode("utf-8").split(".")[1][:3]
        if extName == "wmb":
            targetWMBindex = i
        if extName == "wtp":
            targetWTPindex = i

    #check if we got the suspects
    if targetWMBindex == -1:
        print("where the fucking wmb")
    if targetWTPindex == -1:
        print("where the fucking wtp")



    for i, name in enumerate(modData.fileNames):
        # print(i,name)
        extName = name.decode("utf-8").split(".")[1][:3]
        if extName == "wmb":
            targetData.files[targetWMBindex] = modData.files[i]
        if extName == "wtp":
            targetData.files[targetWTPindex] = modData.files[i]
        
        # if extName in ["wmb", "wtp"]:
        #     targetData.files[i] = modData.files[i]
    targetData.shitaDat(os.path.join(os.path.dirname(mod), os.path.basename(target)))
    
if __name__ == '__main__':
    args = sys.argv[1:]
    for dirPath in args:
        if not os.path.isdir(dirPath):
            continue
        else:
            for root, dirs, files in os.walk(dirPath, topdown=True):
                for file in files:
                    extensionless = file.split(".")[0]
                    extension = os.path.splitext(file)[1]
                    for i in range(4):
                        if extensionless == inputWeapons[i]:
                            continue
                        if extensionless in sortedWeapons[i]:
                            if extension ==  ".dat":
                                swapDat(os.path.join(targetPath, inputWeapons[i]+".dat"), os.path.join(root, file))
                            elif extension == ".dtt":
                                swapDtt(os.path.join(targetPath, inputWeapons[i]+".dtt"), os.path.join(root, file))
