class DeliveryDriver:

    def get_name(self):
        return self._firstname

    def __init__(self, firstname):
        self._firstname = firstname


# The main trick
def main():
    sally = DeliveryDriver("Sally")
    print(sally.get_name())


if __name__ == "__main__":
    main()