class CommandHandler(object):

    @abstractmethod
    def handle(self, command):
        raise NotImplementedError