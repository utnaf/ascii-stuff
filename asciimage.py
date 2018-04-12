if __name__ == '__main__':
    import argparse
    import sys
    import os
    from src import to_ascii
    from src import get_image
    from src import Screen
    from src import Options

    parser = argparse.ArgumentParser(
        description="Convert an image into ASCII art")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", help="Local file path")
    group.add_argument("-u", help="Remote url")

    parser.add_argument(
        "-g", help="Show the image in grayscale", action='store_true')
    parser.add_argument(
        "-w", help="To HTML", action="store_true")
    parser.add_argument(
        "-s", help="Save to file")

    args = parser.parse_args()

    try:
        y, x = os.popen('stty size', 'r').read().split()
        to_ascii(get_image(args.f, args.u), Screen((x, y)), Options(args))
        input()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
