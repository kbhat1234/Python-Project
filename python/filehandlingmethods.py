import os

def fileHandlingMethods():
           """print "Renaming the file"
           os.rename("file.txt","file4.txt")"""

           """print "Make the directory"
           os.mkdir("karthik")"""

           """print "Change the directory"
           os.chdir("karthik")"""

           print "Remove/Delete the directory"
           os.rmdir("karthik")

"""           print "Remove/Delete the file"
           os.remove("file4.txt")

           print "Current working directory", os.getcwd()
"""           
def main():
           fileHandlingMethods()

if __name__ == "__main__":
           main()
