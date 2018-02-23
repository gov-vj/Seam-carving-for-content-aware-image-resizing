import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self):
        dp=dict()
        for j in range(self.height):
            for i in range(self.width):
                if j==0: dp[i,j]=self.energy(i,j),None
                elif self.width==1:
                    dp[i,j]=dp[i,j-1][0]+self.energy(i,j),(i,j-1)
                elif i==0:
                    x=min([(dp[i,j-1][0],(i,j-1)),(dp[i+1,j-1][0],(i+1,j-1))])
                    dp[i,j]=x[0]+self.energy(i,j),x[1]
                elif i==self.width-1:
                    x=min([(dp[i,j-1][0],(i,j-1)),(dp[i-1,j-1][0],(i-1,j-1))])
                    dp[i,j]=x[0]+self.energy(i,j),x[1]
                else:
                    x=min([(dp[i,j-1][0],(i,j-1)),(dp[i+1,j-1][0],(i+1,j-1)),(dp[i-1,j-1][0],(i-1,j-1))])
                    dp[i,j]=x[0]+self.energy(i,j),x[1]
        path=[]
        u=min([(dp[i,self.height-1][0],i) for i in range(self.width)])
        x=u[1],self.height-1
        while x is not None:
            path.append(x)
            x=dp[x][1]
        path.reverse()
        return path
        

    def remove_best_seam(self):
        self.remove_seam(self.best_seam())
