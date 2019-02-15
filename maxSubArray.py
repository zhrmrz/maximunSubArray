class Sol:
    def max_subarray(self,glist):
        for i in range(len(glist)):
            if i==0:
                pass
            else:
                glist[i]=max(glist[i]+glist[i-1],glist[i])
        return max(glist)
if __name__ == '__main__':
    glist=[-2,1,-3,4,-1,2,1,-5,4]
    p1=Sol()
    print(p1.max_subarray(glist))
