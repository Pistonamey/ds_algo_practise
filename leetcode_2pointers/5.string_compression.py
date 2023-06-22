class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read=0
        write=0
        cur_char=chars[0]
        cur_car_length=0
        next_index=0
        while(read<len(chars)):
            if(chars[read]!=cur_char):
                chars[write]=cur_char
                if(read-next_index==1):
                    write+=1
                    next_index=read
                    cur_char=chars[read]
                elif(read-next_index>=10):
                        write+=1
                        # char1=str((read-next_index)//10)
                        # char2=str((read-next_index)%10)
                        # chars[write]=char1
                        # write+=1
                        # chars[write]=char2
                        # write+=1
                        # next_index=read
                        # cur_char=chars[read]

                        s=str(read-next_index)
                        for i in range(len(s)):
                            chars[write]=s[i]
                            write+=1
                        next_index=read
                        cur_char=chars[read]
                else:
                        write+=1
                        chars[write]=str(read-next_index)
                        write+=1
                        next_index=read
                        cur_char=chars[read]
            read+=1
        
        chars[write]=cur_char
        if(read-next_index==1):
                    write+=1
                    
        elif(read-next_index>=10):
                write+=1
                # char1=str((read-next_index)//10)
                # char2=str((read-next_index)%10)
                # chars[write]=char1
                # write+=1
                # chars[write]=char2
                # write+=1

                s=str(read-next_index)
                for j in range(len(s)):
                    chars[write]=s[j]
                    write+=1
                
                
        else:
                write+=1
                chars[write]=str(read-next_index)
                write+=1
        return write