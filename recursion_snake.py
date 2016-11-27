def top_triangle(symbol,width,level):
    
    line="|"*(width-level)+symbol*(width-2*(width-level))+"|"*(width-level)
    
    if level>width//2+width%2:
        return [line]+top_triangle(symbol,width,level-1)
    else:
        if width%2:
            return [line]
        else:
            return []
                
        
        
def build_figure(width):
    top=top_triangle(">",width,width)
    bottom=top_triangle("<",width,width)
    bottom.reverse()
    if width%2:
        bottom=bottom[1:]
        
    return top+bottom




def print_figure(figure):
    if len(figure)==0:
        return
    
    print(figure[0])
    print_figure(figure[1:])
    
    
print_figure(build_figure(6))
