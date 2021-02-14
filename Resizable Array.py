class Resizable_Array:

    def __init__(self):
               #  initializing the pointers
        self.resz_array = [None] * 2   
        self.pointer = 0
        self.lenght_array = len(self.resz_array)

    # __________________________GROWING OF AN ARRAY___________________________________#
             # ===== INSERTING VALUES IN ARRAY  ===== #
    def Insert_Value(self, value):

        if self.pointer == self.lenght_array:
            counter = 0
            self.lenght_array = self.lenght_array * 2
            New_Array = [None] * self.lenght_array

            while counter < (len(self.resz_array)):
                New_Array[counter] = self.resz_array[counter]
                counter += 1
            self.resz_array = New_Array

        self.resz_array[self.pointer] = value
        self.pointer += 1
           #   =====  INSERTING VALUES AT FIRST =====  #
    def Insert_At_First(self, value):

        self.first = len(self.resz_array) + 1
        self.first = [i for i in range(self.first)]
        self.first[0] = value
        r = len(self.resz_array)
        for i in range(1, r + 1):
            self.first[i] = self.resz_array[i - 1]
        self.resz_array = self.first
           #   =====  INSERTING VALUES AT END =====  #
    def Insert_At_End(self, value):

        self.arr_lenght = len(self.resz_array) + 1
        self.End = [i for i in range(self.arr_lenght)]
        r = len(self.resz_array)
        for i in range(0, r):
            self.End[i] = self.resz_array[i]
        self.End[r] = value
        self.resz_array = self.End
          #    ===== CHECK IF THE ARRAY IS EMPTY OR NOT ===== #
        
    def Is_Empty(self):

        if len(self.resz_array) == 0:

            return True

        else:

            return False
          #   =====  DELETE THE VALUE AT FIRST INDEX =====   #   
    def Delete_At_First(self):
                    #  check if the array is empty or not 
        if self.Is_Empty() == True:

            raise "Cannot delete item from empty array!"

        else:
            self.arr_lenght = len(self.resz_array) - 1
            self.After_Del = [i for i in range(self.arr_lenght)]
            r = len(self.After_Del)
            for i in range(0, r):
                self.After_Del[i] = self.resz_array[i + 1]
            self.resz_array = self.After_Del
          #   =====  DELETE THE VALUE AT LAST INDEX =====   # 
    def Delete_At_End(self):
               #  check if the array is empty or not 
        if self.Is_Empty() == True:
                     
            raise "Cannot delete item from empty array!"

        else:
            self.arr_lenght = len(self.resz_array) - 1
            self.After_Del = [i for i in range(self.arr_lenght)]
            for i in range(self.arr_lenght):
                self.After_Del[i] = self.resz_array[i]
            self.resz_array = self.After_Del

    # __________________________SHRINKING OF AN ARRAY___________________________________#

    def Shrink_Array(self):

        length = len(self.resz_array)

        if (length == 1) or (length == 0):
            return " Type Error!"

        halfLen = length / 2
        for i in reversed(range(len(self.resz_array))):

            if self.resz_array[i] != None:
                self.resz_array[i] = None
                break
        if self.resz_array.count(None) == halfLen:
            lst2 = self.resz_array
            self.resz_array = []
            for i in lst2:
                if i != None:
                    self.resz_array = self.resz_array + [i]
                else:
                    break

    def Return_Array(self):

        return self.resz_array


# ____Driver Code________
obj = Resizable_Array()
print("Inserted Values are\n")
obj.Insert_Value(1)
obj.Insert_Value(2)
obj.Insert_Value(3)
obj.Insert_Value(4)
obj.Insert_Value(5)
obj.Insert_Value(6)
obj.Insert_Value(7)
obj.Insert_Value(8)
obj.Insert_Value(9)
print(obj.Return_Array())
# _________________________________________
print("\nShrinking an Array!\n")
obj.Shrink_Array()
obj.Shrink_Array()
obj.Shrink_Array()
obj.Shrink_Array()
obj.Shrink_Array()
print(obj.Return_Array())

# _________________________________________
print("\nInserting value at First\n")
obj.Insert_At_First(0)
print(obj.Return_Array())
# _________________________________________
print("\nInserting value at End\n")
obj.Insert_At_End(6)
print(obj.Return_Array())
# _________________________________________
print("\nDeleting first value\n")
obj.Delete_At_First()
print(obj.Return_Array())
# _________________________________________
print("\nDeleting Last Value\n")
obj.Delete_At_End()
print(obj.Return_Array())