


def input_wrapper():

        counter = 0

        while counter < 5:

            given_input = input("give a number between 0 than 10:  ")

            try:
                given_input = int(given_input)
                if given_input >=10:
                    raise exception_high
                if given_input <0:
                    raise exception_low

                print("your input was correct:", given_input)
                break

            except:
                counter += 1
                print("your number was not in the given range")

            if counter == 5:
                print("You had to many tries")
                break

input_wrapper()


