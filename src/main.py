from classes.champion import Champion


def main():

    yasuo = Champion.create_yasuo()
    vi = Champion.create_vi()

    print(yasuo.display_info())
    print(vi.display_info())


if __name__ == "__main__":
    main()
