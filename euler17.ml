let dig_to_count x= List.nth [0; 3; 3; 5; 4; 4; 3; 5; 5; 4] x
let teens_count x= List.nth [3; 6; 6; 8; 8; 7; 7; 9; 8; 8] x
let two_dig_to_count x= 
  if (x/10)=1 then teens_count (x mod 10) 
  else dig_to_count(x mod 10) + (List.nth [0; 0; 6; 6; 5; 5; 5; 7; 6; 6] (x/10))

let letter_count x= 
  let rec num_to_count (x, digs) : int= 
    match digs with
    | 4 -> 11
    | 3 -> if x mod 100 = 0 then (dig_to_count (x/100)) + 7 else 
           (dig_to_count (x/100)) + 10 + (two_dig_to_count (x mod 100))
    | 2 -> two_dig_to_count (x mod 100)
    | 1 -> dig_to_count x 
    | _ -> failwith "num of digits is always > 0 & < 5" in
  num_to_count (x, 1+int_of_float(log10(float_of_int x)))

let total_count=
  let rec build_list ls n = if n=1 then 1::ls else n::(build_list ls (n-1)) in
  List.fold_left (fun acc x -> acc + letter_count x) 0 (build_list [] 1000)
