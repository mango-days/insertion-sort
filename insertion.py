array = [13, 12, 11, 5]

for index in range ( 1, len(array) ):
    compare_with = array[ index ]
    i = index-1
    
    while ( i >= 0 and compare_with < array[ i ] ) :
        array[ i + 1 ] = array[ i ]
        i -= 1
        
    array[ i + 1 ] = compare_with
    
print ( array )