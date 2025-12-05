from screeninfo import get_monitors


def get_screen_size():
    # Gets info about primary monitor
    monitor = get_monitors()[0]

    screen_size = []
    screen_width = monitor.width
    screen_height = monitor.height

    screen_size.append(screen_width)
    screen_size.append(screen_height)

    return screen_size
