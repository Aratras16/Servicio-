import math


class Vector:
    def __init__(self,x=0,y=0,z=0): # define las coordenadas 
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self): # regresa las coordenadas para que podamos recrear el objeto
        return f"Vector({self.x},{self.y},{self.z})"
    
    def __str__(self): # regresa las coordenadas en usando los vectores unitarios i,j,k
        return f"{self.x}i+{self.y}j+{self.z}k"
    #Queremos ahora hacer a la clase Vector indexable esto para poder hacer cosas del estilo vector[0]
    def __getitem__(self,item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z 
        else:
            raise IndexError("index out of range")
    #Ahora definiremos la suma y resta de vectores
    def __add__(self,other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )
    def __sub__(self,other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )
    #Ahora definiremos la multiplicacion por escalar y el producto punto
    def __mul__(self, other):
        if isinstance(other,Vector): #isinstance checa si other es del tipo vector y regresa un valor booleano
            return(  # producto punto
                self.x * other.x
                + self.y * other.y
                + self.z * other.z
            ) 
        if isinstance(other, (int, float) ): # checamos si other es del tipo int o float 
            return Vector( #producto escalar
                self.x * other,
                self.y * other,
                self.z * other,
            )
        else:
            raise TypeError("operand must be Vector,int or float")  
    #Division escalar
    def __truediv__(self, other):
        if isinstance(other, (int, float) ):
            return Vector(
                self.x / other,
                self.y / other,
                self.z / other,
            )
        else:
            raise TypeError("operand must be int or float") 
    # Magnitud de un vector
    def get_magnitude(self):
        return math.sqrt(self.x**2+ self.y**2 +self.z**2)
    # Normalizacion de un vector
    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude ,
        )


class Vector_dimension:
    def __init__(self,x=0,y=0,z=0,w=0): # define las coordenadas 
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    def __repr__(self): # regresa las coordenadas para que podamos recrear el objeto
        return f"Vector_dimension({self.x},{self.y},{self.z},{self.w})"
    
    def __str__(self): # regresa las coordenadas en usando los vectores unitarios i,j,k
        return f"{self.x}i+{self.y}j+{self.z}k+{self.w}l"
    #Queremos ahora hacer a la clase Vector indexable esto para poder hacer cosas del estilo vector[0]
    def __getitem__(self,item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z 
        elif item == 3:
            return self.w 
        else:
            raise IndexError("index out of range")
    #Ahora definiremos la suma y resta de vectores
    def __add__(self,other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w,
        )
    def __sub__(self,other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.w - other.w,
        )
    #Ahora definiremos la multiplicacion por escalar y el producto punto
    def __mul__(self, other):
        if isinstance(other,Vector): #isinstance checa si other es del tipo vector y regresa un valor booleano
            return(  # producto punto
                self.x * other.x
                + self.y * other.y
                + self.z * other.z
                + self.w * other.w
            ) 
        if isinstance(other, (int, float) ): # checamos si other es del tipo int o float 
            return Vector( #producto escalar
                self.x * other,
                self.y * other,
                self.z * other,
                self.w * other,
            )
        else:
            raise TypeError("operand must be Vector,int or float")  
    #Division escalar
    def __truediv__(self, other):
        if isinstance(other, (int, float) ):
            return Vector(
                self.x / other,
                self.y / other,
                self.z / other,
                self.w / other,
            )
        else:
            raise TypeError("operand must be int or float") 
    # Magnitud de un vector
    def get_magnitude(self):
        return math.sqrt(self.x**2+ self.y**2 +self.z**2+self.w**2)
    # Normalizacion de un vector
    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
            self.w / magnitude,
        )

