class Restaurant:

    def get_name(self):
        return "This is a restaurant"

    def get_module_name(self):
        return __name__


# The main trick
def main():
    pizza_hut = Restaurant()
    print(pizza_hut.get_module_name())


if __name__ == "__main__":
    main()
