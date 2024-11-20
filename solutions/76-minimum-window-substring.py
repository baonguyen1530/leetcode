class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t, window = {}, {}

        if len(s) < len(t) or t == "":
            return ""
        
        #count all the characters in t
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have, need = 0, len(count_t)
        res, resLen = [-1,-1], float("infinity")
        l = 0

        for r in range(len(s)):
            
            #store this in variable for readability
            c = s[r]

            #increment the count of the letter at c by 1 in the window map
            window[c] = 1 + window.get(c, 0)

            #increment have by 1 if the letter is in the count_t map
            #and their count is the same 
            if c in count_t and window[c] == count_t[c]:
                have += 1


            #now we will update when have and need are equal to each other
            #whenever have and need are equal to each other, that means we
            #have found one window, but we want to find whether or not there
            #is smaller a window so we have to go through the entire array s
            while have == need:
                
                #first we have update our result
                #check if the current window length is less than our resLen
                #because we are trying to find the smallest window
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = (r - l + 1)

                #after checking we move to the next window
                #decrement the count by 1
                window[s[l]] -= 1
                
                #this check if our have decreases
                #this means we need to exit because we have find a new window
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1     
                    
                l += 1

        l, r = res
        if resLen != float("infinity"):
            return s[l:r+1]
        else:
            return ""