# whileで求めようとしていたが、TLEになるので一般化できるところまでやるのが大事
X,K,D=map(int, input().split())

X=abs(X)

# K回移動しても絶対値が0を超えない
if 0<X-K*D:
    print(abs(X-K*D))

else:
    # 0に限りなく近づくまでの回数 X // D で求められる 
    move_count=K-X//D

    jump_before=X-D*(X//D)
    jump_after=jump_before-D

    if move_count%2==0:
        print(abs(jump_before))
    else:
        print(abs(jump_after))


# ミスったコード
# X, K, D = map(int, input().split())

# currentNum = abs(X)

# count = 0

# while((currentNum - D) > 0 and count != K):
#     currentNum -= D
#     count += 1

# if(count == K):
#     print(abs(currentNum))
# else:
#     if((K - count) % 2 == 0):
#         print(abs(currentNum))
#     else:
#         print(abs(currentNum - D))

