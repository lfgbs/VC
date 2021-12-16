import open3d as o3d

def main():
    print("Testing IO for point cloud ...")
    pcd = o3d.io.read_point_cloud("cloud_bin_0.pcd")
    print(pcd)
    o3d.io.write_point_cloud("copy_of_cloud_bin_0.pcd", pcd)

    print("Testing IO for meshes ...")
    mesh = o3d.io.read_triangle_mesh("frag_115.ply")
    print(mesh)
    o3d.io.write_triangle_mesh("copy_of_frag_115.ply", mesh)

    print("Testing IO for images ...")
    img = o3d.io.read_image("lena_color.jpg")
    print(img)
    o3d.io.write_image("copy_of_lena_color.jpg", img)


if __name__ == "__main__":
    main()