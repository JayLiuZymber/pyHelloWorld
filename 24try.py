#!/usr/bin/python3
# try except
while True:
    try:
        # x = int(input('輸入數字:'))
        x = 123
        print(x)
        break
    except ValueError:
        print('輸入的不是數字!')

# -----------------------------------------------------------------------------
import sys

try:
    f = open('text.txt')
    s = f.readline()
    i = int(s.strip)
except OSError as err:
    print('OS error: {0}'.format(err))
except ValueError:
    print('Could not convert data to an integer')
except:
    print('Unexpected error:', sys.exc_info()[0])
    
# -----------------------------------------------------------------------------
print('#try except else')
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('Cannot open', arg)
    except:
        print('Unknow error')
    else:
        print(arg, 'has', len(f.readline()), 'lines')
        f.close()

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handing run-time error:', err)

# -----------------------------------------------------------------------------
print('#try finally')
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10/n

try:
    # foo(0) #do except
    foo(1) #do else
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
            print(fnf_error)
finally:
    print('finally over')
    
# -----------------------------------------------------------------------------
print('#raise')
# x = 10 #do raise
x = 2 #pass raise
if x>5:
    raise Exception('x不能大於5. x值: {}'.format(x))

try:
    # raise NameError('HiThere') #do raise
    pass #pass raise
except NameError:
    print('name error!')
    raise

# -----------------------------------------------------------------------------
print('#def except')
class myError(Exception):
    def __init__(self, value): #over write __init__
        self.value = value
    def __str__(self):
        return repr(self.value)
    
try:
    raise myError(2*2)
except myError as e:
    print('my exception, value:', e.value)

# -----------------------------------------------------------------------------
class Error(Exception):
    '''Base class for exception'''
    pass
class InputError(Error):
    '''Exception raised for error in the input
    
    屬性:
        expression = input expression in which the error occurred
        message = explanation of the error
    '''
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    '''Raised when an operation attempts a state transition that's not
    allowed.

    屬性:
        previous = state at beginning of transition
        next = attempted new state
        message = explanation of why the specific transition is not allowed
    '''
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

# -----------------------------------------------------------------------------
def divide(x, y):
    try:
        ans = x / y
    except ZeroDivisionError:
        print('division by zero!')
    except:
        print('unknow error')
    else:
        print('ans is', ans)
    finally:
        print('executing finally over')
divide(2, 1)
divide(2, 0)
divide('2', '1')

try:
    with open('text.txt') as f:
        for line in f:
            print(line, end='')
except:
    print('unknow error')

