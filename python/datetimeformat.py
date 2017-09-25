from datetime import datetime

def dateTimeFormatFunc():
           now = datetime.now()
           print now.strftime("%Y")

def main():
           dateTimeFormatFunc()

if __name__ == "__main__":
           main()
