#!/bin/bash
#SBATCH --job-name=SimulationsMTandMM
#SBATCH --mail-user=Katrina.Wharam@physik.uni-muenchen.de
#SBATCH --mail-type=FAIL #Alternative: BEGIN END FAIL REQUEUE
#SBATCH --output=/scratch/k/Katrina.Wharam/SimulationsMTandMM/data/main15.log 
#SBATCH --mem=2G
#SBATCH --time=24:00:00

module load python/3.9-2021.11
python3.9 /scratch/k/Katrina.Wharam/SimulationsMTandMM/setup15/buildConfigAndRun.py
