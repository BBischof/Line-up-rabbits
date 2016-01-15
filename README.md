# Line-up-rabbits

## Problem

Given $n$ rabbits of different heights, how many ways can we put them into a line such that we see $l$ from the left, and $r$ from the right.

## Algorithm

The recursive algorithm is as follows:
- Remove the last element of the list this will help us decide where other elements are, this will *always* be seen, as it is the tallest
- partition the remaining into two sets, call the recursive function on both
- **recursive function begins here**
- if the number of elements in the set is 0 or 1, it's a base case
- taking the set, remove the largest element, this will definitely be seen from the left, so again, we use it to partition our left set
- take the remaining left set and partition it into left and right again
- call the recusive function on left and right sides
- **base cases**
- if there is 0 elements, then the previously tallest are the only visible elements, count all the elements hidden and calculate the multiplicity by those numbers factorial, multiplied
- if there is 1 elements, then the previously tallest plus this one are the only visible elements, count all the elements hidden and calculate the multiplicity by those numbers factorial, multiplied


## Usage

For recursive solution: 
```
python rabbitsRecursion.py n l r
```
where n, l, and r are the integers above. I assume l, r >=1 since otherwise the solution is zero. I also assume that n >= l+r because again otherwise the solution is zero.

```
python rabbitsRecursion.py n l r -v
```
is an optional flag for verbose. This prints a ton of output to see the actual patterns and some other nice info.

```
python iteratingRabbitsRecursion.py n
``` 
iterates over all reasonable pairs for l and r and outputs the values in matrix form where the row is the view from the left, the column is the view from the right, and the matrix element is the number of patters with those configurations. Outputs the matrices for n in range 1 to specified. Notice they will be lower triangular and symmetric.

e.g. the matrix for 2 is
```
[[ 0.  1.]
 [ 1.  0.]]
```
which says there is one pattern for (2,0,1) and (2,1,0) which correspond to sequences 12 and 21, the only two possible sequences on two symbols.

## Initial observations

The first thing that one can glean from these matrices is that the diagonals, as n increases, form Pascal's triangle. This and many more interesting sequences are hiding in the matrices, or in the sequence of matrices interpreted correctly. For instance, if we take the superdiagonals from these matrices, make a triangle similar to before, we notice that the far left column is the sequence of triangle numbers.