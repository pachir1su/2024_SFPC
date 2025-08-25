# Pre_B0
def main() :
    farms = [
        ("SoilRich", 0.65),
        ("BerryPro", 0.73),
        ("CropHub", 0.59),
        ("Strawful", 0.71),
        ("FarmLush", 0.66),
        ("Harvesty", 0.67),
        ("GrowMore", 0.58),
        ("PlantJoy", 0.72),
        ("PureFarm", 0.60),
        ("SweetRed", 0.74)
    ]
    
    sorted_farms = sorted(farms, key=lambda x: x[1], reverse=True)
    
    rank_dict = {}
    for rank, (name, _) in enumerate(sorted_farms, start=1) :
        rank_dict[name] = rank

    output = []
    for name, _ in farms :
        output.append(f"{name} {rank_dict[name]}")
    print(" ".join(output))

if __name__ == "__main__" :
    main()