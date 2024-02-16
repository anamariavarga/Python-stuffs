a = int(input ('''Welcome tot the right place if you want to know more about triangles :)
First topic: Triangles based on their sides.
Let's see what type is your triangle.
Insert the first triangle side in cm: '''));
b = int(input ('Insert the second triangle side in cm: '));
c = int(input ('Insert the third triangle side in cm: '));
if a <= 0 or b <=  0 or c <= 0:
    print("A triangle must have all the sides positive and different of zero. The sides can't form a triangle! :(")
elif a+b < c or a+c < b or c+b < a:
    print("The sides can't form a triangle! :(")
elif (a**2 + b**2 == c**2) or (a**2 + b**2 == c**2) or (a**2 + b**2 == c**2):
    print('The triangle type = isosceles triangle')
elif a == b == c:
    print('The triangle type = equilateral triangle')
else:
    print('The triangle type = scalene triangle')
print("""
\m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/ \m/

""")
d = int(input ('''Second topic topic: Triangles based on their angles.
Let's see what type is your triangle.
Insert the first triangle angle: '''));
e = int(input ('Insert the second triangle angle: '));
f = int(input ('Insert the third triangle angle: '));
if a <= 0 or b <= 0 or c <= 0:
    print("A triangle must have all the angles positive and different of zero. The angles can't form a triangle! :( ")
elif d + e + f != 180:
    print("The sum of the triangle angles must be 180. In any other case the angles can't form a triangle. :(")
elif (d == 90) or (e == 90) or (f == 90):
    print('The triangle type = right triangle')
elif (d >= 90) or (e >= 90) or (f >= 90):
    print('The triangle type = obtuse triangle')
elif d == e == f:
    print('The triangle type = equilateral triangle')
else:
    print('The triangle type = acute triangle')