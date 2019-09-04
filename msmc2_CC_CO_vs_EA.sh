cd server/msmc2_runs/cross-coalescence/Comoros_vs_EastAfrica/NCHE_vs_MIR

population01=NCHE
population02=MIR

msmc2 \
-t 15 \
-P 0,0,0,0,1,1,1,1 \
-o "2"$population01"_vs_2"$population02 \
server/multihetseps/cross-coalescence/"2L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"2R_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3R_2"$population01"_vs_2"$population02".txt" &&

cd server/msmc2_runs/cross-coalescence/Comoros_vs_EastAfrica/NCHE_vs_MOY

population01=NCHE
population02=MOY

msmc2 \
-t 15 \
-P 0,0,0,0,1,1,1,1 \
-o "2"$population01"_vs_2"$population02 \
server/multihetseps/cross-coalescence/"2L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"2R_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3R_2"$population01"_vs_2"$population02".txt" &&

cd server/msmc2_runs/cross-coalescence/Comoros_vs_EastAfrica/TNZK_vs_MIR

population01=TNZK
population02=MIR

msmc2 \
-t 15 \
-P 0,0,0,0,1,1,1,1 \
-o "2"$population01"_vs_2"$population02 \
server/multihetseps/cross-coalescence/"2L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"2R_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3R_2"$population01"_vs_2"$population02".txt" &&

cd server/msmc2_runs/cross-coalescence/Comoros_vs_EastAfrica/TNZK_vs_MOY

population01=TNZK
population02=MOY

msmc2 \
-t 15 \
-P 0,0,0,0,1,1,1,1 \
-o "2"$population01"_vs_2"$population02 \
server/multihetseps/cross-coalescence/"2L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"2R_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3R_2"$population01"_vs_2"$population02".txt"
