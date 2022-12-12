import os

path = input("Enter the path of the folder containing shorts : ")

def main():
        count = 1
        with open( (path + "/list.txt"), 'w') as file:
            shorts_list = os.listdir(path)          #list of files names
            for short in shorts_list:               # iterate over al file names
                if (short.endswith('.mp4')):
                    os.rename( (path + "/" + short), (path + "/" + str(count) + ".mp4"))
                    file.write("file " + path + "/" + str(count) + ".mp4\n")
                    count+=1
        os.system("ffmpeg -f concat -safe 0 -i \"" + path + "/list.txt\" -c copy \"" + path + "/output.mp4\" -y")
        os.remove(path + "/list.txt")
        
if __name__ == "__main__":
    main();
