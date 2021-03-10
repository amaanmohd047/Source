# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |________________________________________________________________________________________________________|
# |    Class                         :     Description                                                     |
# |    ----------------------------------------------------------------------------------------------------|
# |    Exception                     :     A base class for most error types                               |
# |    ----------------------------------------------------------------------------------------------------|
# |    AttributeError                :     Raised by syntax obj.foo, if obj has no member named foo        |
# |    ----------------------------------------------------------------------------------------------------|
# |    EOFError                      :     Raised if “end of file” reached for console or file input       |
# |    ----------------------------------------------------------------------------------------------------|
# |    IOError                       :     Raised upon failure of I/O operation (e.g., opening file)       |
# |    ----------------------------------------------------------------------------------------------------|
# |    IndexError                    :     Raised if index to sequence is out of bounds                    |
# |    ----------------------------------------------------------------------------------------------------|
# |    KeyError                      :     Raised if nonexistent key requested for set or dictionary       |
# |    ----------------------------------------------------------------------------------------------------|
# |    KeyboardInterrupt             :     Raised if user types ctrl-C while program is executing          |
# |    ----------------------------------------------------------------------------------------------------|
# |    NameError                     :     Raised if nonexistent identifier used                           |
# |    ----------------------------------------------------------------------------------------------------|
# |    StopIteration                 :     Raised by next(iterator) if no element                          |
# |    ----------------------------------------------------------------------------------------------------|
# |    ValueError                    :     Raised when parameter has invalid value (e.g., sqrt(−5))        |
# |    ----------------------------------------------------------------------------------------------------|
# |    ZeroDivisionError             :     Raised when any division operator used with 0 as division       |
# |________________________________________________________________________________________________________|
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


## RAISING AN EXCEPTION

var1 = input("> ")
var2 = input("> ")
result = 0
try:
    result = float(var1) + float(var2)
    print(result)
except ValueError:
    print("values should be real number")

try:
    with open("sample.txt") as file:
        print(file.read())
except IOError as e:
    print("Cannot open file", e)