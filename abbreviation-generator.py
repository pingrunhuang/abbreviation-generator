class Generator:
    def generator1(self, name):
        self.abbreviation = name[0] + str(len(name)-2) + name[-1]
        return self.abbreviation
    def speak_out_loud(self):
        pass


if __name__ == "__main__":
    gen = Generator()
    name = input()
    print("Start to abbreviate:{}".format(name))
    result = gen.generator1(name)
    print("Result:{}".format(result))
