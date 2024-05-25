from PIL import Image
import sys
import os

def mergeRow(imgA, imgB): 
    w = imgA.size[0] + imgB.size[0]
    h = max(imgA.size[1],imgB.size[1])
    newImg = Image.new("RGBA", (w, h))

    newImg.paste(imgA)
    newImg.paste(imgB, (imgA.size[0],0))

    return newImg

def mergeGrid(imgs, rows, cols):
    assert len(imgs) == rows*cols

    width, height = imgs[0].size
    newSpriteSheet = Image.new("RGBA", size=(cols * width , rows * height))
    grid_width, grid_height = newSpriteSheet.size

    for i, img in enumerate(imgs):
        newSpriteSheet.paste(img, box=(i%cols*width, i//cols*height))
    return newSpriteSheet 

    
num = len(sys.argv)
print("Total Arguments passed: ", num -1)


print("Directory to load img seq from : " , sys.argv[1])
imgDir = sys.argv[1]
print(imgDir)

print("Total seq num : ", sys.argv[2])
seqNum = sys.argv[2]
print(seqNum)

print("Sprite Column : ", sys.argv[3])
col = sys.argv[3]
print(col)

print("Sprite Row : ", sys.argv[4])
row = sys.argv[4]
print(row)

print("Save Name : ", sys.argv[5])
saveName = sys.argv[5]
print(saveName)


imagesName = []
for imgName in os.listdir(imgDir):
    imagesName.append("./"+ imgDir + "/" + imgName)
print(imagesName)

loadedImages = []

print("=============LOADING=============================")
for i, name in enumerate(imagesName):
    print("index num : " + str(i))
    print("image name : " + name)
    img = Image.open(name)
    loadedImages.append(img)

print("All images Loaded into memory")
print("Merging Images into sprite sheets, please wait... ")
print("================PROCESSING========================")


spriteSheet = mergeGrid(loadedImages, int(row), int(col))
print("=============SAVING... PLEASE WAIT================")
#spriteSheet.show()
spriteSheet.save(saveName)
print("================COMPLETED=========================")



