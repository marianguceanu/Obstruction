from UI.ui import UI


def __main__():
    # ui.welcome() returns a convenient 'None' if the players have decided not to play anymore
    ui = UI()
    if ui.welcome() is not None:
        ui.start()


if __name__ == "__main__":
    __main__()
