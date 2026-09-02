from shapeMath import PHI
import shapeMath





def main():
    area = shapeMath.rectangle_area(5, 5)
    print(area)

    # If we import the variable itself (the import from line 1)
    print(PHI)

    # if we import the whole file (the import from line 2)
    print(shapeMath.PHI)


if __name__ == "__main__":
    main()