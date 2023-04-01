import os


def main():
    desktop_path = "C:\\Users\\" + os.getlogin() + "\\Desktop\\"
    print(desktop_path)
    a = open(desktop_path + "For You.txt", "w")
    a.write("I am a HACKER")
    a.close()


if __name__ == "__main__":
    main()
