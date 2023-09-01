from scripts.swiggy import check_swiggy
from scripts.flipkart import check_flipkart
from scripts.upstox import check_upstox

def main():
    num="7485994073"

    # check_swiggy(num)
    # check_flipkart(num)
    check_upstox(num)
if __name__ == "__main__":
    main()
