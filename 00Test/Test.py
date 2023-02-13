import lupa
from lupa import LuaRuntime
lua = LuaRuntime(unpack_returned_tuples=True)



#python function for lua to call
def pyFunc1( value ):
    print( 'pyFunc1', value );



print( 'lupa ', lupa.__version__ )
print();

print( 'python load lua by string : ' );
lua.execute('''t = load( "print( 'lua print', 123)") ''')
lua.eval('t()')
print();



print( 'python lua.execute : ');
lua.execute('''
    print( 'LUA_VERSION ', _VERSION );

    arch = _VERSION
    if (arch or ""):match"64" then
       print"Your system is 64-bit"
       arch = arch .. ', 64-bit '
    else
       print"Your system is 32-bit"
       arch = arch .. ', 32-bit '
    end

    if( string.pack ~= nil ) then
        if #string.pack("T",0) == 4 then
            print( 'native size 32 bit' )
        end

        if #string.pack("T",0) == 8 then
            print( 'native size 64 bit' )
        end

        if #string.pack("j",0) == 4 then
            print( 'lua_Integer 32 bit' )
        end

        if #string.pack("j",0) == 8 then
            print( 'lua_Integer 64 bit' )
        end
    else
        print( 'string.pack check need lua 5.3?' );
    end

    function _86or64()
        if(0xfffffffff==0xffffffff) then return 32 else return 64 end
    end

    print( 'luacofig.h - define LUA_32BITS : ', _86or64());

    x = load( 'print(456)');
    x();
''');
print();

#load external lua file
print( 'python load external lua file : ' );
lua.execute('t = loadfile( "./Test.lua.js") ')
lua.eval('t()');



#after lua file loaded, and initialised global variable 'window' .
print( 'map python function for lua uses' );
lua_map1 = lua.eval('''
function(f1) 
    window.func1 = f1
end
''')
lua_map1( pyFunc1 );



print( 'python call lua : ' );
lua.execute( 'luaTest()' );
print();

'''
>>> a=[]
>>> a.append(123)
>>> a
[123]
>>> a[0]
123

>>> a['0']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not str

>>> a[123]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range



>>> b = {}
>>> b['1']='nubmer1'
>>> b
{'1': 'nubmer1'}

>>> b[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0

>>> b[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 1

>>> b['1']
'nubmer1'
>>>

'''