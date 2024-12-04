from waterlevels import get_usgs_water_level

def main():
    data = get_usgs_water_level(start_date="2024-12-01")
    print(data) # quick test

if __name__ == "__main__":
    main()
