# run `vmd -e pe.tcl`
mol load lammpstrj dump.lammpstrj

light 0 on
light 1 on
light 2 on
light 3 on

axes location off
color Display Background white

pbc box_draw -color black -width 5.0
mol modstyle 0 0 CPK 0.0 0.0 1 1

mol selection { type 1 }
mol color ColorID 28
mol representation CPK 2.0 0.0 30 30
mol material Diffuse
mol addrep top

mol selection { type 2 }
mol color ColorID 17
mol representation CPK 2.0 0.0 30 30
mol material Glossy
mol addrep top
