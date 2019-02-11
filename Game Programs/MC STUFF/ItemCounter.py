seared_brick = 145
glass = 1

grout = 145

sand = 73
gravel = 73
clay = 14

def bigboi():
    print("\n" * 100)

def main():
    global seared_brick, glass, grout, sand, gravel, clay
    print("SEARED BRICK: %s" % seared_brick)
    print("GLASS:        %s\n" % glass)
    print("GROUT:        %s\n" % grout)
    print("SAND:         %s" % sand)
    print("GRAVEL:       %s" % gravel)
    print("CLAY:         %s\n\n" % clay)

    inp = input("What item did you get?\n")

    if inp == "none" or inp == "":
        bigboi()
        main()

    elif inp == "seared brick":
        inp = int(input("How much did you get?\n"))
        seared_brick = seared_brick - inp
        bigboi()
        main()

    elif inp == "glass":
        inp = int(input("How much did you get?\n"))
        glass = glass - inp
        bigboi()
        main()

    elif inp == "grout":
        inp = int(input("How much did you get?\n"))
        grout = grout - inp
        bigboi()
        main()

    elif inp == "sand":
        inp = int(input("How much did you get?\n"))
        sand = sand - inp
        bigboi()
        main()

    elif inp == "gravel":
        inp = int(input("How much did you get?\n"))
        gravel = gravel - inp
        bigboi()
        main()

    elif inp == "clay":
        inp = int(input("How much did you get?\n"))
        clay = clay - inp
        bigboi()
        main()

main()