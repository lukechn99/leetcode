(* with n fair coins, all flipped at the same time, only coins that flip heads
   are kept. How many rounds are expected? *)
   
(* stops when there are no coins left, passes the number of rounds to parent 
   uses unflipped as an accumulator *)
let rec coinflip' n round unflipped = 
   match unflipped with
   | x -> if x = 0 then round else 
   let result = Random.int 2 in
   
   
let coinflip n = coinflip' n 0 n

let roundavg