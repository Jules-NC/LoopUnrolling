# LoopUnrolling
Automaticly unroll your loops in ANY languages with indexs

### Example
```python
LIGNE = "array(i+1, k-2) = array(i+0, k-2) + array(i+1, k-2) - array(i+3, k-256877845);"
print(deroulage(deroulage(LIGNE, "k", 4), "i", 3, False))
```

**will print**:
```
array(i+1, k-2) = array(i+0, k-2) + array(i+1, k-2) - array(i+3, k-256877845);
array(i+1, k-1) = array(i+0, k-1) + array(i+1, k-1) - array(i+3, k-156877845);
array(i+1, k+0) = array(i+0, k+0) + array(i+1, k+0) - array(i+3, k+056877845);
array(i+1, k+1) = array(i+0, k+1) + array(i+1, k+1) - array(i+3, k+156877845);

array(i+0, k-2) = array(i-1, k-2) + array(i+0, k-2) - array(i+2, k-256877845);
array(i+0, k-1) = array(i-1, k-1) + array(i+0, k-1) - array(i+2, k-156877845);
array(i+0, k+0) = array(i-1, k+0) + array(i+0, k+0) - array(i+2, k+056877845);
array(i+0, k+1) = array(i-1, k+1) + array(i+0, k+1) - array(i+2, k+156877845);

array(i-1, k-2) = array(i-2, k-2) + array(i-1, k-2) - array(i+1, k-256877845);
array(i-1, k-1) = array(i-2, k-1) + array(i-1, k-1) - array(i+1, k-156877845);
array(i-1, k+0) = array(i-2, k+0) + array(i-1, k+0) - array(i+1, k+056877845);
array(i-1, k+1) = array(i-2, k+1) + array(i-1, k+1) - array(i+1, k+156877845);
```

### Parameters of the function
```
deroulage(LINE, "i", 4, False)
```
- **Return** :  a string
- **LINE** : string you want to unroll. Can unroll multiple lines of codes. A LINE can be the result of a precedent unrolling.
- **"i"** : parameter to increase or decrease during the unrolling. all occurences of **i**" must be replaced with **i+0**
- **4**: the number of unrollings of "i"
- **False**: negative or positive unrolling. True = positive unrolling of **i**, False = negative unrolling. True is default behavior

 ##### /!\ Replace all occurences of "i" with "i+0" for a correct unrolling
