'''up arrow'''
'''
       * 
      * * 
     * * * 
    * * * * 
   * * * * * 
  * * * * * * 
 * * * * * * * 
* * * * * * * * 
       * 
       * 
       * 
       * 
       * 
       * 
       * 
       * 
'''
n = 8
for i in range (n):
    print(" " * (n - i - 1) + "* " * (i + 1))


for i in range (n):
    print(" " * (n - 1) + "* ")