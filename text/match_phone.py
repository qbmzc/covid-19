import re

valid = re.compile(r'^13[0-3][0-9]{8}$')
num = '13012345678'
num1='13002017331'
print(valid.match(num1))

print(valid.match(num1) is None)

if __name__ == '__main__':
    print("start")