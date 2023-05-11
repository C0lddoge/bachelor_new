menu main on
color Display Background white
axes location off
display projection Orthographic

light 0 on
light 1 off
light 2 off
light 3 off

mol modstyle 0 0 CPK 0.0 0.0 1 1

pbc set { 20.0 20.0 20.0 } -all
pbc box_draw -color black
pbc wrap -all

mol selection { atomicnumber 1 }
mol color ColorID 0
mol representation CPK 3.5 0.0 5 5
mol addrep top

mol selection { atomicnumber 2 }
mol color ColorID 1
mol representation CPK 3.5 0.0 5 5
mol addrep top

