color Display Background white
display projection Orthographic
axes location off
display depthcue off

light 0 on
light 1 on
light 2 on
light 3 on

mol modstyle 0 0 CPK 0.0 0.0 1 1
mol selection { atomicnumber 1 or type 1 }
mol color ColorID 28
mol representation CPK 8.0 0.0 40 40
mol material Transparent
mol addrep top

mol selection { atomicnumber 2 or type 2 }
mol color ColorID 24
mol representation CPK 8.0 0.0 40 40
mol material Transparent
mol addrep top

mol selection { all }
mol color ColorID 16
mol representation CPK 1.4 0.0 40 40
mol material Diffuse
mol addrep top

mol selection { all }
mol color ColorID 16
mol representation DynamicBonds 4.5 0.3 40
mol material Diffuse
mol addrep top

pbc box_draw -color black
pbc wrap -all
