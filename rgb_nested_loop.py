#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: November 20, 2022
# Displays all the valid RBG values


def main():

    # Iterates through all red values
    for red in range(256):
        # Iterates through all green values
        for green in range(256):
            # Iterates through all blue values
            for blue in range(256):
                # Displays all valid RGB colors
                print(
                    "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                        red,
                        green,
                        blue,
                        "RGB(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                    )
                )


if __name__ == "__main__":
    main()
