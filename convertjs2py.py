import js2py
import convertjs2py
array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'a']

# func = js2py.eval_js(
#     'function containsCommonItem2(arr1, arr2) {  let map={}; for (let i=0; i < arr1.length; i++) {if(!map[arr1[i]]) {      const item=arr1[i];      map[item] = true;}  }')

# func(array1, array2)

js2py.translate_file('convertjs2py.js', 'convertjs2pyexample.py')

convertjs2py.containsCommonItem2(array1, array2)
