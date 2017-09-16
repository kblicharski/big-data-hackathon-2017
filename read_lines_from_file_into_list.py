with open("/tmp/words.txt", "r") as file:
    lines = file.readlines()
    words = [c.strip() for c in lines]
