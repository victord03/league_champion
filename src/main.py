from classes.champion import Champion


def main():

    yasuo = Champion.create_yasuo()
    print(yasuo.display_info())
    # print("\n", yasuo.r.description)


if __name__ == "__main__":
    main()
