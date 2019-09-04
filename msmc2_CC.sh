cd server/msmc2_runs/cross-coalescence/Comoros_vs_Comoros/SAL_vs_MIR

population01=SAL
population02=MIR

msmc2 \
-t 15 \
-P 0,0,0,0,1,1,1,1 \
-o "2"$population01"_vs_2"$population02 \
server/multihetseps/cross-coalescence/"2L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"2R_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3R_2"$population01"_vs_2"$population02".txt" &&

cd server/msmc2_runs/cross-coalescence/Comoros_vs_Comoros/SAL_vs_MOY

population01=SAL
population02=MOY

msmc2 \
-t 15 \
-P 0,0,0,0,1,1,1,1 \
-o "2"$population01"_vs_2"$population02 \
server/multihetseps/cross-coalescence/"2L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"2R_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3R_2"$population01"_vs_2"$population02".txt" &&

cd server/msmc2_runs/cross-coalescence/Comoros_vs_Comoros/MIR_vs_MOY

population01=MIR
population02=MOY

msmc2 \
-t 15 \
-P 0,0,0,0,1,1,1,1 \
-o "2"$population01"_vs_2"$population02 \
server/multihetseps/cross-coalescence/"2L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"2R_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3R_2"$population01"_vs_2"$population02".txt" &&

cd server/msmc2_runs/cross-coalescence/EastAfrica_vs_EastAfrica/TNZK_vs_NCHE

population01=TNZK
population02=NCHE

msmc2 \
-t 15 \
-P 0,0,0,0,1,1,1,1 \
-o "2"$population01"_vs_2"$population02 \
server/multihetseps/cross-coalescence/"2L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"2R_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3R_2"$population01"_vs_2"$population02".txt" &&

cd server/msmc2_runs/cross-coalescence/EastAfrica_vs_WestAfrica/NCHE_vs_SELI

population01=NCHE
population02=SELI

msmc2 \
-t 15 \
-P 0,0,0,0,1,1,1,1 \
-o "2"$population01"_vs_2"$population02 \
server/multihetseps/cross-coalescence/"2L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"2R_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3R_2"$population01"_vs_2"$population02".txt" &&

cd server/msmc2_runs/cross-coalescence/Comoros_vs_EastAfrica/SAL_vs_NCHE

population01=SAL
population02=NCHE

msmc2 \
-t 15 \
-P 0,0,0,0,1,1,1,1 \
-o "2"$population01"_vs_2"$population02 \
server/multihetseps/cross-coalescence/"2L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"2R_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3R_2"$population01"_vs_2"$population02".txt" &&

cd server/msmc2_runs/cross-coalescence/WestAfrica_vs_WestAfrica/SELI_vs_FOUN

population01=SELI
population02=FOUN

msmc2 \
-t 15 \
-P 0,0,0,0,1,1,1,1 \
-o "2"$population01"_vs_2"$population02 \
server/multihetseps/cross-coalescence/"2L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"2R_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3L_2"$population01"_vs_2"$population02".txt" \
server/multihetseps/cross-coalescence/"3R_2"$population01"_vs_2"$population02".txt"
