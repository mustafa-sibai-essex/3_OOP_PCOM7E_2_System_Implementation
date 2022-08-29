import abc


class Page(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def start(self):
        pass
