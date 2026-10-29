class BloatCipher:
    def __init__(self, key: str):
        self.key = key

    def character_to_value(self, character: str) -> int:
        char_value = ord(character)

        if 65 <= char_value <= 90:
            return char_value - 64
        elif 97 <= char_value <= 122:
            return char_value - 96

        raise ValueError("Invalid character")

    def value_to_character(self, value: int) -> str:
        if 1 <= value <= 26:
            return chr(value + 64)

        raise ValueError("Invalid value")

    def extract_name(self, filepath: str) -> tuple[str, str]:
        i = 0
        latest_slash = 0
        latest_dot = -1
        for c in filepath:
            if c == "/":
                latest_slash = i + 1
            if c == ".":
                latest_dot = i
            i += 1

        directory_path = filepath[:latest_slash]
        if latest_dot == -1:
            filename = filepath[latest_slash:]
        else:
            filename = filepath[latest_slash:latest_dot]

        return directory_path, filename

    def encrypt(self, filepath: str, mode="basic"):
        directory_path, filename = self.extract_name(filepath)
        new_filepath = directory_path + filename + ".bloat"

        message = ""
        with open(filepath, "r") as file:
            message = file.read()

        match mode.lower():
            case "basic":
                with open(new_filepath, "w") as file:
                    for c in message:
                        for _ in range(self.character_to_value(c)):
                            file.write(self.key)
                        file.write("\n")
            case "ascii":
                with open(new_filepath, "w") as file:
                    for c in message:
                        for _ in range(ord(c)):
                            file.write(self.key)
                        file.write("\n")
            case "unicode":
                with open(new_filepath, "w") as file:
                    for c in message:
                        for _ in range(ord(c)):
                            file.write(self.key)
                        file.write("\n")
            case _:
                raise ValueError("Invalid cipher mode")

        print("Encrypted file: " + new_filepath)

    def decrypt(self, filepath: str, mode="basic"):
        directory_path, filename = self.extract_name(filepath)
        new_filepath = directory_path + filename + ".txt"

        message = ""
        with open(filepath, "r") as file:
            message = file.read()

        match mode.lower():
            case "basic":
                with open(new_filepath, "w") as file:
                    i = 0
                    for c in message.replace(self.key, "."):
                        if c == "\n":
                            file.write(self.value_to_character(i))
                            i = 0
                        else:
                            i += 1
            case "ascii":
                with open(new_filepath, "w") as file:
                    i = 0
                    for c in message.replace(self.key, "."):
                        if c == "\n":
                            file.write(chr(i))
                            i = 0
                        else:
                            i += 1
            case "unicode":
                with open(new_filepath, "w") as file:
                    i = 0
                    for c in message.replace(self.key, "."):
                        if c == "\n":
                            file.write(chr(i))
                            i = 0
                        else:
                            i += 1
            case _:
                raise ValueError("Invalid cipher mode")

        print("Decrypted file: " + new_filepath)
