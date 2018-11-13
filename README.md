# LoopUnrolling
Automaticly unroll your loops in ANY languages with indexs

### Example
```python
LIGNE = "array(i+0, k+0) = gamma2*array(i+0, k-2) + array(i+0, k-1) - array(i+0, k-2);"
res = deroulage(deroulage(LIGNE, "k", 8, False), "i", 6)
```
**will print**:
```
array(i+0, k+0) = array(i+0, k-2) + array(i+0, k-1) - array(i+0, k-2);
array(i+0, k+0) = array(i+0, k-2) + array(i+0, k-1) - array(i+0, k-2);
array(i+0, k+0) = array(i+0, k-2) + array(i+0, k-1) - array(i+0, k-2);
array(i+0, k+0) = array(i+0, k-2) + array(i+0, k-1) - array(i+0, k-2);

array(i+1, k+0) = array(i+1, k-2) + array(i+1, k-1) - array(i+1, k-2);
array(i+1, k+0) = array(i+1, k-2) + array(i+1, k-1) - array(i+1, k-2);
array(i+1, k+0) = array(i+1, k-2) + array(i+1, k-1) - array(i+1, k-2);
array(i+1, k+0) = array(i+1, k-2) + array(i+1, k-1) - array(i+1, k-2);

array(i+2, k+0) = array(i+2, k-2) + array(i+2, k-1) - array(i+2, k-2);
array(i+2, k+0) = array(i+2, k-2) + array(i+2, k-1) - array(i+2, k-2);
array(i+2, k+0) = array(i+2, k-2) + array(i+2, k-1) - array(i+2, k-2);
array(i+2, k+0) = array(i+2, k-2) + array(i+2, k-1) - array(i+2, k-2);
```
