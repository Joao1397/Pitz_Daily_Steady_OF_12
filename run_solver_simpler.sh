#!/bin/bash

foamListTimes -rm
rm log.*
rm *.foam
rm -rf postProcessing

checkMesh -writeSets -meshQuality -overwrite > log.checkMesh 2>&1
decomposePar > log.decomposePar 2>&1
# mpirun -np 8 renumberMesh -overwrite -parallel > log.renumberMesh 2>&1
mpirun -np 2 renumberMesh -overwrite -parallel > log.renumberMesh 2>&1
# mpirun -np 8 foamRun -solver incompressibleFluid -parallel > log.solver 2>&1
mpirun -np 2 foamRun -solver incompressibleFluid -parallel > log.solver 2>&1
reconstructPar > log.reconstructPar 2>&1
# foamPostProcess -solver incompressibleFluid -funcs '(yPlus vorticity 
# PecletNo wallShearStress shearStress CourantNo Q)' > log.postProcess 2>&1
rm -rf process*
# python3 Residuals.py
# touch Pitz_Daily_Steady.foam
# eval "/home/cfd/paraview/ParaView-5.12.1-MPI-Linux-Python3.10-x86_64/bin/paraview Pitz_Daily_Steady.foam &"

# decomposePar >> logdecomposePar where you want to see progress on the terminal and keep a log history
# decomposePar | tee log.decomposePar

# foamToVTK -faceSet nonOrthoFaces | tee log.foamtovtk1
# checkMesh -latestTime | tee log.checkMesh
