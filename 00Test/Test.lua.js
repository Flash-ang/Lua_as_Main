print( 'this is Test.lua.js' );

-- for js (web)
if js ~= nil then
    local js = require "js"
    window = js.global
    -- document = window.document
else 
    -- for python or others
    if window == nil then
        window = {};
    end
end

function luaTest()
    print( 'lua : luaTest()' );
    window.func1( 789 );
end

--[[
a = {}
a[1] = 123
a['1'] = 456
a['x'] = 135
table.insert( a, 789 )

print( a[1] )
print( a[2] )
print( a[3] )
print( a['1'] )
print( a['x'] )
print( a.x )

** result : 

a[1] 123
a[2] 789
a[3] nil
a['1'] 456
a.['x'] 135
a.x 135

]]