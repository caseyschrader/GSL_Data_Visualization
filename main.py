from water_levels import get_usgs_water_levels

def main():
    data = get_usgs_water_levels(start_date="2024-12-01")
    print(data) # quick test

if __name__ == "__main__":
    main()
