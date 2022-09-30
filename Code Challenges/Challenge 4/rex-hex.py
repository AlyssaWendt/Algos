'''
## 2. **RGB To Hex Conversion**

The RGB function is incomplete. Complete it so that passing in RGB decimal 
values will result in a hexadecimal representation being returned. Valid decimal 
values for RGB are 0 - 255. Any values that fall out of that range must be rounded 
to the closest valid value.

**Note**: Your answer should always be 6 characters long, the shorthand with 
3 will not work here.

The following are examples of expected output values:
rgb(255, 255, 255) // returns FFFFFF
rgb(255, 255, 300) // returns FFFFFF
rgb(0,0,0) // returns 000000
rgb(148, 0, 211) // returns 9400D3

'''
#edge case 0 = 0 and >255 = 255
#set a function that takes a value and changes it into 3 digit hex
# run that function through an rgb function changing rgb into the hex values 

def to_hex(value):
    if value < 0:
        value = 0
    if value > 255:
        value = 255

    return '{:0>2}'.format(hex(value)[2:].upper())

def rgb(r,g,b):
    return to_hex(r)+to_hex(g)+to_hex(b) 
    

print(rgb(148, 0, 211))
print(rgb(0,0,0))
print(rgb(255, 255, 300))