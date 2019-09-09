***Question 9:***

<h2>Level up</h2>

Mr X is playing a game. The game contains several levels. The game has a major setback.
Everytime you lose a level you have to start from the level 1 again. But the points are calculated together for all the times played.
Point Calculation:
    Everytime you pass a new level you get 25 points.
    Everytime you pass a level that you have already passed in the previous rounds you get 1 point.

**Examples:**
```
Input :
    3
    1 2 1
    
Output :
    52
```
Explanation: 
    Mr x played 3 times.
    In his first turn he managed to pass level 1. So he scored 25 points.
    In his second turn he managed to pass level 2(which means he passed both levels 1 and 2). He got 25 points for level 2 and 1 point for level 1
    In his third turn he managed to pass level 1. He got 1 point for that.
    So in total he got 25 + 26 + 1 = 52 points.
```
Input :
    1
    2
    
Output :
    50   

Input:
    3
    2 2 3
    
Output:
    79

```