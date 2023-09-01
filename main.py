import argparse
from scripts.swiggy import check_swiggy
from scripts.flipkart import check_flipkart
from scripts.upstox import check_upstox

# Define your ASCII banner
banner = """
888b     d888          888      d8b 888                .d88888b.   .d8888b. 8888888 888b    888 88888888888 
8888b   d8888          888      Y8P 888               d88P" "Y88b d88P  Y88b  888   8888b   888     888     
88888b.d88888          888          888               888     888 Y88b.       888   88888b  888     888     
888Y88888P888  .d88b.  88888b.  888 888  .d88b.       888     888  "Y888b.    888   888Y88b 888     888     
888 Y888P 888 d88""88b 888 "88b 888 888 d8P  Y8b      888     888     "Y88b.  888   888 Y88b888     888     
888  Y8P  888 888  888 888  888 888 888 88888888      888     888       "888  888   888  Y88888     888     
888   "   888 Y88..88P 888 d88P 888 888 Y8b.          Y88b. .d88P Y88b  d88P  888   888   Y8888     888     
888       888  "Y88P"  88888P"  888 888  "Y8888        "Y88888P"   "Y8888P" 8888888 888    Y888     888     
                                                                                                            
                                                                                                            
                                                                                                            
@ViralVaghela https://github.com/viralvaghela/OSINT_MOBILE
"""

# Create a dictionary to map service names to functions
services = {
    "swiggy": check_swiggy,
    "flipkart": check_flipkart,
    "upstox": check_upstox,
}

def main():
    print(banner)  # Print the ASCII banner

    parser = argparse.ArgumentParser(description="Check various services with a phone number.")
    parser.add_argument("phone_number", type=str, help="Phone number to use")
    args = parser.parse_args()
    phone_number = args.phone_number

    # Loop through all available services and call their respective functions
    for service_name, service_function in services.items():
        print(f"Checking {service_name}...")
        service_function(phone_number)
        print()

if __name__ == "__main__":
    main()
