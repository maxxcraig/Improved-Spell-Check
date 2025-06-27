def Levenshtein(str1, str2):
    #make a matrix that is the size of the two string with an extra row and col for base cases
    rows, cols = len(str1) + 1, len(str2) + 1
    dp = [[0] * cols for _ in range(rows)]
    
    #fill the extra col with base case of lev dist to an empty string from each point
    for c in range(cols):
        dp[0][c] = c
        
    #same as above but for the first row
    for r in range(rows):
        dp[r][0] = r
        
    #for the submatrix of the actual strings, the lev dist will be the minimum
    #of the sqaure to its left, above, and left above diagonal if there's no edit to be made
    #if an edit needs to be made then same number but add 1
    for r in range(1,rows):
        for c in range(1, cols):
            if str1[r - 1] == str2[c - 1]:
                dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
            else:
                dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                      
    #the bottom right value in the matrix will be the final lev distance
    return dp[rows -1 ][cols -1]
        
    