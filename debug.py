# x = "123"
# y = "321"
# arr = [x+y+str(i) for i in range(10)]
# arr = [f"{x}+{y}+{str(i)}" for i in range(10)]
# print(arr)

class A():
    def pra(self):
        print("Class - A")
    a = "a"
    class B():
        def prb(self):
            print("Class - B")
        b = "b"

class D(A):
    def prd(self):
        print("Class - D")
    d = "d"

# Create instances with different variable names
a_instance = A()
d_instance = D()
b_instance = A.B()  # Access inner class via class A

a_instance.pra()    # Class - A
b_instance.prb()    # Class - B  
d_instance.prd()    # Class - D
#d_instance.B.prb()# A.B.prb() missing 1 required positional argument: 'self'

# To access B from D instance, you need to use the class, not instance
D.B().prb()         # Class - B


