def changes(amount, coins):
    
    def count(coins, n, sum):    
        table = [[0 for x in range(n)] for x in range(sum+1)]
        
        for i in range(n):
            table[0][i] = 1
        
        for i in range(1, sum+1):
            for j in range(n):
 
                # Count of solutions including coins[j]
                x = table[i - coins[j]][j] if i-coins[j] >= 0 else 0
     
                # Count of solutions excluding coins[j]
                y = table[i][j-1] if j >= 1 else 0
     
                # total count
                table[i][j] = x + y
 
        return table[sum][n-1]
    
    return count(coins, len(coins), amount)    