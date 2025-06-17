def combine(width, height=10, depth =0, is_3D=False):
        if is_3D:
            return[is_3D,width,height,depth]
        
print(combine(2)[0])