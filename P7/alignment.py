import numpy as np
import open3d as o3d
import argparse
import copy

def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp],
                                      zoom=0.4459,
                                      front=[0.9288, -0.2951, -0.2242],
                                      lookat=[1.6784, 2.0612, 1.4451],
                                      up=[-0.3402, -0.9189, -0.1996])

def main():
    parser = argparse.ArgumentParser(description='Typing Test Option Parser')
    parser.add_argument('--source', type=str, required=True, help='Path to pointcloud file')
    parser.add_argument('--target', type=str, required=True, help='Path to pointcloud file')
    args = parser.parse_args()

    pcd_source = o3d.io.read_point_cloud(args.source)
    pcd_target = o3d.io.read_point_cloud(args.target)
    threshold=1

    #trans_init = np.identity(4)

    trans_init = np.asarray([[0.862, 0.011, -0.507, 0.5],
                             [-0.139, 0.967, -0.215, 0.7],
                             [0.487, 0.255, 0.835, -1.4], [0.0, 0.0, 0.0, 1.0]])

    print(trans_init)

    draw_registration_result(pcd_source, pcd_target, trans_init)

    print("Initial alignment")
    evaluation = o3d.pipelines.registration.evaluate_registration(
    pcd_source, pcd_target, threshold, trans_init)
    print(evaluation)

    print("Apply point-to-point ICP")
    reg_p2p = o3d.pipelines.registration.registration_icp(
        pcd_source, pcd_target, threshold,trans_init, 
        o3d.pipelines.registration.TransformationEstimationPointToPoint(),
        o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=2000))
    print(reg_p2p)
    print("Transformation is:")
    print(reg_p2p.transformation)
    draw_registration_result(pcd_source, pcd_target, reg_p2p.transformation)


if __name__ =="__main__":
        main()