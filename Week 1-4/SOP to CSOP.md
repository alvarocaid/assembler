```
(*This must be run in wolfram cloud*)
(* Define a function to get minterms from indices *)
mintermsFromIndices[indices_List, vars_List, truthTable_] := Module[{minterms},
    
  (* Convert each index to its corresponding minterm *)
  minterms = Map[
    And @@ (If[#, #2, Not[#2]] & @@@ Transpose[{truthTable[[#]], vars}]) &,
    indices
  ];
  
  minterms
]

(* Define the function to find true indices *)
findTrueIndices[expr_, vars_List, truthTable_] := Module[{evals},
  
  (* Evaluate the expression for each row of the truth table *)
  evals = Map[expr /. Thread[vars -> #] &, truthTable]; (*https://reference.wolfram.com/language/ref/Map.html?q=Map*)
  (*https://reference.wolfram.com/language/ref/ReplaceAll.html*)
  (*https://reference.wolfram.com/language/ref/Thread.html*)
  
  
  (* Extract the indices where the expression evaluates to True *)
   Position[evals, True] // Flatten
   (*==Flatten[Position[evals, True]]*)
  (*https://reference.wolfram.com/language/ref/Position.html*)
  (*https://reference.wolfram.com/language/tutorial/OperatorInputForms.html (e//e)//e*)
]

canonicalSOP[expr_, vars_List] := Module[{truthTable, trueIndices, minterms},
  (* Find the indices where the expression evaluates to True *)
 truthTable = Tuples[{True, False}, Length[vars]]; (*https://reference.wolfram.com/language/ref/Tuples.html*)
  
  trueIndices = findTrueIndices[expr, vars, truthTable];
  
  (* Generate minterms from these indices *)
  minterms = mintermsFromIndices[trueIndices, vars, truthTable];
  
  (* Combine minterms into canonical SOP form *)
 TraditionalForm[ Or @@ minterms]
]
(* Example usage for expression  *)
expr = (A&&!B&&C)||(!A&&!B)||(A&&B&&!C&&D);
vars = {A,B, C, D};

(* Display minterms using TraditionalForm *)
canonicalSOP[expr, vars]
```