# ------------------------------------------------------------ Crack-free Walls --------------------------------------------------------------- #
#                                                                                                                                               #
#       Consider the problem of building a wall out of 2×1 and 3×1 bricks (horizontal×vertical dimensions) such that, for extra strength,       #
#       the gaps between horizontally-adjacent bricks never line up in consecutive layers, i.e. never form a "running crack".                   #
#                                                                                                                                               #
#       For example, the following 9×3 wall is not acceptable due to the running crack shown in red:                                            #
#                                                                                                                                               #
#                                                           * * *|* *|* *|* *                                                                   #                                                           
#                                                           * *|* *|* * *|* *                                                                   #
#                                                           * * *|* * *|* * *                                                                   #                                                           
#                                                                                                                                               #
#       There are eight ways of forming a crack-free 9×3 wall, written W(9,3) = 8.                                                              #
#                                                                                                                                               #
#       Calculate W(32,10).                                                                                                                     #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

def get_legal_layers(l, bricks):
    layers = [[]]

    for i in range(1, l + 1):
        layer_i = []
        
        for b in bricks:
            if i - b == 0:
                layer_i.append([b])
            elif i - b > 0:
                for layer_i_minus_b in layers[i - b]:
                    layer_i.append(layer_i_minus_b + [b])

        layers.append(layer_i)

    return layers[l]

def is_crack_free(l1, l2):
    i1 = 1
    i2 = 1

    s1 = l1[0]
    s2 = l2[0]

    while (i1 < len(l1)) and (i2 < len(l2)):
        if s1 == s2:
            return 0

        if s1 <= s2:
            s1 += l1[i1]
            i1 += 1
        else:
            s2 += l2[i2]
            i2 += 1

    return 1        

def eu215():
    DIMENSIONS = (32, 10)
    BRICKS = [2, 3]
    
    layers = get_legal_layers(DIMENSIONS[0], BRICKS)

    layers_count = len(layers)

    crack_free = [[] for i in range(layers_count)]
    for i in range(layers_count):
        for j in range(i + 1, layers_count):
            if is_crack_free(layers[i], layers[j]):
                crack_free[i].append(j)
                crack_free[j].append(i)

    crack_free_walls = [[0 for j in range(layers_count)] for i in range(DIMENSIONS[1])]
    for j in range(layers_count):
        crack_free_walls[0][j] = 1

    for layer in range(1, DIMENSIONS[1]):
        for top_layer in range(layers_count):
            crack_free_walls[layer][top_layer] = sum([crack_free_walls[layer - 1][t] for t in crack_free[top_layer]])
            
    return sum([w for w in crack_free_walls[DIMENSIONS[1] - 1]])
        
if __name__ == "__main__":
    startTime = time.clock()
    print (eu215())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
