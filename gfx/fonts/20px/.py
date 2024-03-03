file = open( "gfx/fonts/20px/.fnt", "wt" )

# Add the symbol positions of the blank symbol slots here.
exclude = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26,
            27, 28, 29, 30, 31, 127, 129, 141, 143, 144, 156, 173, 181]

for x in range( 1, 255 ):
    for y in range(1, 255):
        if x not in exclude:
            if y not in exclude:
                file.write( "kerning first={0}  second={1}  amount=1\n".format( x, y ) )

file.close()