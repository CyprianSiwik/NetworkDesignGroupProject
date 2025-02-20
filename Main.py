#Network Design Phase 2 Programming Project

#imports
import matplotlib.pyplot

#Functions

    #Make_packet function

    #Gives us array of packets - binary chunks of the image file
def make_packet(image_path, packet_size=1024):
    imageData = []
    try:
        with open(image_path, 'rb') as image_file:
            while True:
                packet = image_file.read(packet_size)
                if not packet:
                    break
                imageData.append(packet)
        return imageData
    except FileNotFoundError:
        print("File was not found.")

    #Performance Plots





#main
image_path = str(input("Enter the file name:"))
print(image_path)

while True:
    print("Select the data transfer scenario you wish to choose:")