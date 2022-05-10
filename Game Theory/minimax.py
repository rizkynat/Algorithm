import math

def minimax(currentDepth, indexNode, isMax, score, h):
    #Terminating condition, if leaf node reached
    if(currentDepth==h):
        return score[indexNode]
    #if current move is maximizer, find the maximum value
    if(isMax):
        return max(minimax(currentDepth+1, indexNode*2, False, score, h),
        minimax(currentDepth+1, indexNode*2+1, False, score, h))
    #if current minimizer, find the minimum value
    else:
        return min(minimax(currentDepth+1, indexNode*2, True, score, h),
        minimax(currentDepth+1, indexNode*2+1, True, score, h))

score = [3, 5, 2, 9, 12, 5, 23, 23]
n = len(score)
h = math.log(n,2)
print('Score is ',end="")
print(minimax(0,0,True,score,h))
print(h)