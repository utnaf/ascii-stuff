if __name__ == '__main__':
    import argparse
    import sys
    import os
    from src import main
    from src import get_image

    parser = argparse.ArgumentParser(
        description="Convert an image into ASCII art")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", help="Local file path")
    group.add_argument("-u", help="Remote url")

    parser.add_argument(
        "-g", help="Show the image in grayscale", action='store_true')
    args = parser.parse_args()

    try:
        main(get_image(args.f, args.u), args.g)
        input()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
