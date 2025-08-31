class Human:
    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby
    
    def human_info(self):
        """ Information about the human """
        print(f"Name: {self.name.title()}")
        print(f"Hobby: {self.hobby}")
    
    def greet(self):
        """ Greet 'hello' with the name """
        print(f"{self.name.title()} says hello!")


def main():
    
    human_1 = Human('tristan', 'playing guitar')
    human_1.human_info()
    human_1.greet()

main()
        