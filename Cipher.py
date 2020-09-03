import base64

class B64:
    @staticmethod
    def encode(text):
        return (base64.b64encode(text.encode())).decode()
    @staticmethod
    def decode(code):
        return base64.b64decode(code).decode()

class A1Z26:
    @staticmethod
    def encode(text):
        result = []
        for i in text:
            if i.isalpha():
                result.append(str(ord(i.lower()) - 96))
            else:
                result.append(i)
        return " - ".join(result)

    @staticmethod
    def decode(code):
        result = []
        code = code.split(" - ")
        for i in code:
            if i.isnumeric():
                result.append(chr(int(i) + 96))
            else:
                result.append(i)
        return "".join(result)

class Caesar:
    @staticmethod
    def encode(code, number):
        result = []
        for i in code:
            index = ord(i) + number
            if index > 126:
                index -= 95
            result.append(chr(index))
        return "".join(result)

    @staticmethod
    def decode(code, number):
        result = []
        for i in code:
            index = ord(i) - number
            if index < 32:
                index += 95
            result.append(chr(index))
        return "".join(result)

class Atbash:
    @staticmethod
    def encode(text):
        return text[::-1]
    @staticmethod
    def decode(code):
        return code[::-1]

class Vigenere:
    @staticmethod
    def encode(text, key):
        result = []
        key = (key * (len(text) // len(key))) + key[:len(text) % len(key)]

        for i in range(len(text)):

            if text[i].isalpha() and key[i].isalpha():

                keyCode = ord(key[i].lower()) - 96
                textCode = ord(text[i].lower()) - 96

                ans = textCode + keyCode - 1

                if ans > 26:
                    ans -= 26

                if text[i].isupper():
                    result.append(chr(ans + 96).upper())
                else:
                    result.append(chr(ans + 96))

            else:
                result.append(text[i])

        return "".join(result)

    @staticmethod
    def decode(code, key):
        result = []
        key = (key * (len(code) // len(key))) + key[:len(code) % len(key)]

        for i in range(len(code)):

            if code[i].isalpha() and key[i].isalpha():

                keyCode = ord(key[i].lower()) - 96
                codeCode = ord(code[i].lower()) - 96

                ans = codeCode - keyCode + 1

                if ans < 1:
                    ans += 26

                if code[i].isupper():
                    result.append(chr(ans + 96).upper())
                else:
                    result.append(chr(ans + 96))

            else:
                result.append(code[i])

        return "".join(result)

print(Vigenere.encode("Text! Is Hi", "Key"))
print(Vigenere.decode("Divd! Sw Rm", "Key"))
