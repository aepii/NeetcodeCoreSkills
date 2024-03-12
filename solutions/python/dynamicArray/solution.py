class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity # Initialize array's capacity.
        self.size = 0 # Array is empty.
        self.array = [0] * self.capacity # Fill array with empty zeros.

    def get(self, i: int) -> int:
        return self.array[i] # Return a element in the array given an index.

    def set(self, i: int, n: int) -> None:
        self.array[i] = n # Set the value of an element in the array with n given an index.

    def pushback(self, n: int) -> None:

        # If the array is full, resize the array.
        if self.size == self.capacity: 
            self.resize()

        # The end of the array is the current size and not the capacity. 
        # Ex. [1 2 0 0]: Array of size 2 with capacity 4, so push onto index 2.
        self.array[self.size] = n # Push element onto the end of the array.
        self.size += 1 # Increase the size by one.

    def popback(self) -> int:
        # Problem says assume array is not empty.
        self.size -= 1 # Decrease the length.

        # We don't need to remove or zero out the element because of the nature of length.
        return self.array[self.size]

    def resize(self) -> None:
        self.capacity *= 2 # Double the capacity.
        new_array = [0] * self.capacity # Fill a new array with empty zeros with the new capacity.
        for index in range(self.size): # Replace the zeros in the new array with existing elements from the old array.
            new_array[index] = self.array[index]
        self.array = new_array # Change the old array with the new one.

    def getSize(self) -> int:
        return self.size # Return the size of the array.
    
    def getCapacity(self) -> int:
        return self.capacity # Return the capacity of the array.