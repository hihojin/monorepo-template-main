class Logger:
    _instance = None  # Private class variable to hold the single instance

    def init_singleton(self):
        self.messages = []
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.init_singleton()
            print('Logger created exactly once')
        else:
            print('logger already created')
        return cls._instance

    def add_message(self, message):
        self.messages.append(message)


def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
    for i in range(3):
        logger = Logger()
        logger.add_message(f"Adding message number: {i}")


if __name__ == "__main__":
    main()
