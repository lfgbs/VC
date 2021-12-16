import numpy as np
import open3d as o3d

def main():

    #loading and showing pcd
    print("Load a ply point cloud, print it, and render it")
    #pcd = o3d.io.read_point_cloud("cloud_bin_0.pcd")
    pcd = o3d.io.read_point_cloud("mid_centry_antiques.ply")
    print(pcd)
    print(np.asarray(pcd.points))
    o3d.visualization.draw_geometries([pcd])

    #print(o3d.__version__)

    #Voxel downsampling
    print("Downsample the point cloud with a voxel of 0.05")
    downpcd = pcd.voxel_down_sample(0.05)
    o3d.visualization.draw_geometries([downpcd])

    #seems like all calculations are already done for you and you only need to press "n" to see them so the normal vectors block seems redundant/unnecessary
    #Normal vectors
    print("Recompute the normal of the downsampled point cloud")
    downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1,max_nn=30))
    print("Print a normal vector of the 0th point")
    print(downpcd.normals[0])
    print("Print the normal vectors of the first 10 points")
    print(np.asarray(downpcd.normals)[:10, :])
    #o3d.visualization.draw_geometries([downpcd])

    #não fiz a secção de crop e paint

if __name__ == "__main__":
    main()
    
