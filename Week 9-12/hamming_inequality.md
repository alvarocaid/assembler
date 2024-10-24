Wolfram Cloud code
```
getP[d_] := Minimize[{p, 2^p >= p + d + 1 && p > 0}, p, Integers][[2, 1, 2]]

getP[8] (*4*)
```  
