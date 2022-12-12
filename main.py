import os

path = "/Users/nishithshetty/Downloads/vid/"
title1 = "Reddit Compilation #"
title2 = " | Reddit shorts | Redditcasm.mp4"

def main():
        count = 1
        for i in range(1,11):                          # no of folder
            with open("list.txt", 'w') as file:
                cur_path = path + str(i)                   # path + current folder name
                video_list = os.listdir(cur_path)          #list of files names
                if ".DS_Store" in video_list : video_list.remove(".DS_Store")
                for x in video_list:                        # iterate over al file names
                    os.rename( (cur_path + "/" + x), (cur_path + "/" + str(count) + ".mp4"))
                    file.write("file " + cur_path + "/" + str(count) + ".mp4\n")
                    count+=1
                count=1
            #ffmpeg -f concat -safe 0 -i list.txt -c copy /Users/nishithshetty/Downloads/vid/result/output.mp4
            os.system("ffmpeg -f concat -safe 0 -i list.txt -c copy /Users/nishithshetty/Downloads/vid/result/" + str(i) + ".mp4 -y")

if __name__ == "__main__":
    main();