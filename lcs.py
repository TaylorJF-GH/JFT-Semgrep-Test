def lcs(X, Y):
    m, n = len(X), len(Y)
    
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(m):
        
        for j in range(n):
            
            if X[i] == Y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
                
    return dp[m][n]
    
print(lcs("AGGTAB","GXTXAYB"))