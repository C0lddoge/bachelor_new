import argparse
import codemodule as cm
parser = argparse.ArgumentParser()
parser.add_argument(
    "--directory",
    type = str,
    required = True
        )
parser.add_argument(
        "--r_c",
        type = float,
        required = True)
parser.add_argument(
        "--flag",
        type = str,
        default = "all")
parser.add_argument(
        "--rho",
        type = float,
        default = "all")

directory = vars(parser.parse_args())["directory"]
r_c = vars(parser.parse_args())["r_c"]
flag = vars(parser.parse_args())["flag"]
rho = vars(parser.parse_args())["rho"]
xyz_path = "{:}/frames.xyz".format(directory)
frames,types = cm.read_xyz(xyz_path,100,3000)
bins,cluster,error = cm.struct_ana(frames,types,rho,r_c,flag)
filename = "{:}_cluster_rc{:}_types_{:}_v2.dat".format(directory,r_c,flag)
print(len(cluster))
cm.write_xy(directory + '/results/' + filename,[bins,cluster,error
    ])





