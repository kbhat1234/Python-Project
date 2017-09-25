def add_digits_of_number():
           n=12345
           sum=0;
           while(n>0):
                      r = n%10
                      sum = sum+r
                      n = n/10
           print sum

def main():
           add_digits_of_number()

if __name__ == "__main__":
           main()
