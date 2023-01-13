"""Python serial number generator."""

class SerialGenerator:
    def __init__(self, start):
        self.start = start
        """stores the start number for Reset"""
        self.count = start - 1
        """ stores the last serial generated"""

    def generate(self):
        self.count += 1
        """increments the counter before returning"""
        return self.count
         
    def reset(self):
        self.count = self.start -1
        """resets the counter to its original number"""
        
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

serial = SerialGenerator(start=100)
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
serial.reset()
print(serial.generate())
print(serial.generate())