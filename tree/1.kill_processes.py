# # You have n processes forming a rooted tree structure. You are given two 
# integer arrays pid and ppid, where pid[i] is the ID of the ith process and 
# ppid[i] is the ID of the ith process's parent process.

# # Each process has only one parent process but may have multiple children 
# # processes. Only one process has ppid[i] = 0, which means this process has 
# # no parent process (the root of the tree).

# # When a process is killed, all of its children processes will also be killed.

# # Given an integer kill representing the ID of a process you want to kill, return a 
# # list of the IDs of the processes that will be killed. You may return the answer in any order.

def killProcess( pid, ppid, kill: int):
        tree={}
        for i in range(len(ppid)):
            if ppid[i] in tree:
                tree[ppid[i]].append(pid[i])
            else:
                if(ppid[i]==0):
                    continue
                else:
                    tree[ppid[i]]=[pid[i]]
        res=[]
        queue=[kill]
        while queue:
            current=queue.pop(0)
            res.append(current)
            if(current in tree):
                queue.extend(tree[current])
        
        return res

print(killProcess([1,3,10,5],[3,0,5,3],5))