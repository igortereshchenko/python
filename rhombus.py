def get_block(symbol, size,orientation):
    if orientation=='\\':
        set=range(size)
    elif orientation=='/':
        set=range(-(size-1),1,1)
    else:
        print('error with parameter orientation')
    list=[(' '*abs(i)+symbol+' '*(size-abs(i)-1)) for i in set]
    return list


def connect_horizontal_blocks(block_left, block_rigth):
    list=[ block_left[i]+block_rigth[i] for i in range(len(block_left))]
    
    return list
    
def connect_vertical_blocks(block_top, block_bottom):    
    return block_top+block_bottom
    
block_left=get_block('@', 5,'\\')
block_rigth=get_block('@', 5,'\\')

top_part=connect_horizontal_blocks(block_left,block_rigth)

block_left=get_block('@', 5,'/')
block_rigth=get_block('@', 5,'/')

bottom_part=connect_horizontal_blocks(block_left,block_rigth)


figure=connect_vertical_blocks(top_part,bottom_part)


for line in figure:
    print(line)
