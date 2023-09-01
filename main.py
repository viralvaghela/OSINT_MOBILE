from scripts.swiggy import check_swiggy
from scripts.flipkart import check_flipkart

def main():
    num="1234567890"

    check_swiggy(num)
    check_flipkart(num)
if __name__ == "__main__":
    main()
