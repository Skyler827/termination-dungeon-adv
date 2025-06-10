class Level:
    width:int = 100
    height:int = 100
    background:Background = 
    objects
    __new__(self, name):
        # parse name as json file
        with open(name+".json", "r") as file:
            content = file.read()
            print(content)
            json.loads(content)
