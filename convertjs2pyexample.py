__all__ = ['convertjs2pyexample']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['array1', 'containsCommonItem2', 'array2'])
@Js
def PyJsHoisted_containsCommonItem2_(arr1, arr2, this, arguments, var=var):
    var = Scope({'arr1':arr1, 'arr2':arr2, 'this':this, 'arguments':arguments}, var)
    var.registers(['map', 'arr2', 'j', 'arr1', 'i', 'item'])
    var.put('map', Js({}))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('arr1').get('length')):
        try:
            if var.get('map').get(var.get('arr1').get(var.get('i'))).neg():
                var.put('item', var.get('arr1').get(var.get('i')))
                var.get('map').put(var.get('item'), Js(True))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('j', Js(0.0))
    while (var.get('j')<var.get('arr2').get('length')):
        try:
            if var.get('map').get(var.get('arr2').get(var.get('j'))):
                return Js(True)
        finally:
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
    return Js(False)
PyJsHoisted_containsCommonItem2_.func_name = 'containsCommonItem2'
var.put('containsCommonItem2', PyJsHoisted_containsCommonItem2_)
var.put('array1', Js([Js('a'), Js('b'), Js('c'), Js('x')]))
var.put('array2', Js([Js('z'), Js('y'), Js('a')]))
var.put('array1', Js([Js('a'), Js('b'), Js('c'), Js('x')]))
var.put('array2', Js([Js('z'), Js('y'), Js('a')]))
pass
pass


# Add lib to the module scope
convertjs2pyexample = var.to_python()