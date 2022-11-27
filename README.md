# BeadsTools
BeadsTools is a python package for treating ADVENTURE IO files on python.
This is created by Hibiya Haraki in 2022.

## Ready for using BeadsTools
## Path to BeadsTools
You need PATH to BeadsTools by adding command in 'sudo vi ~/.bashrc'.
```
$ sudo vi ~/.bashrc
```
Please write following command.
```
export PYTHONPATH=$PATH:${HOME}/path/to/suigetsu_simulation
```

## Install nmslib
In BeadsTools, the script use nmslib library for doing kNN calculation.
```
$ pip install nmslib
```

## Documentation for each functions
### beads_msh.py

1. NumOfElements, Elements, NumOfNodes, Nodes, NumOfVolumes, NumOfElementsInEachVolume, Volumes = **read_msh**(filePath)
    * NumOfElements - Number of Elements included in the .msh file [int]
    * Elements - Element data [list (int)]
    * NumOfNodes - Number of Nodes inluded in the .msh file [int]
    * Nodes - Node data [list (float)]
    * NumOfVolumes - Number of Volume included in the .msh file [int]
    * NumOfElementsInEachVolume - Number of Elements included in each Volume [list (int)]
    * Volumes - Volume Data [list (int)]
    * filePath - Path to the .msh file [string]

2. **write_msh**(filePath,Elements,Nodes,Volumes)
    * filePath - Path to output .msh file [string]
    * Elements - Element data [list (int)]
    * Nodes - Node data [list (float)]
    * Volumes - Volume data [list (int)]

3. gp = **calculate_gravity_point**(Nodes)
    * gp - Coordinate of gravity point [list (float)]
    * Nodes - 3 Nodes data consisted of a triangle

### beads_fgr.py

1. ElementID, FaceID, Elements = **read_fgr**(filePath,surfaceID)
    * ElementID - ID of Elements that includes surface [list (int)]
    * FaeID - ID of face that identify which face is the surface we want to get in a element [list (int)]
    * Elements - Surface element data [list (int)]
    * filePath - Path to the .fgr file [string]
    * surfaceID - ID of surface in a model [list (int)]

2. Elements = **convert_face2node**(FaceID)
    * Elements - ID for identify the nodes that consists of the face [list (int)]
    * FaceID - ID of face in a element [list (int)]

### beads_cnd.py

1. ans = **read_cnd**(filePath,transientID)
    * ans - SurfaceID identified by the transientID [list (int)]
    * filepath - Path to the .cnd file [string]
    * transientID - transientID that you want to get the surface ID [int]

### beads_dat.py

1. dataLabel, NumOfData, Data = **read_dat**(filePath)
    * dataLabel - Label of the .dat file [string]
    * NumOfData - Number of data [int]
    * Data - Data [list (float)]
    * filePath - Path to the .dat file [string]

2. **write_dat**(filePath,dataLabel, Data)
    * filePath - Path to the .dat file [string]
    * dataLabel - Label of the .dat file [string]
    * Data - Data [list (float)]

3. **compare_dat**(InfilePath1, InfilePath2, OutfilePath, method)
    * InfilePath1 - Path to input .dat file [string]
    * InfilePath2 - Path to input .dat file [string]
    * OutfilePath - Path to output .dat file [string]
    * method - 0 is difference, 1 is absolute difference [int]

### beads_pts.py

1. NumOfPoints, PointData = **read_pts**(filePath)
    * NumOfPoints - Number of Points included in the .pts file [int]
    * PointData - Point cloud data [list (float)]
    * filePath - Path to input .pts file [string]

2. **write_pts**(filePath,pointData)
    * filePath - Path to output .pts file [string]
    * pointData - Point cloud data [list (float)]

### beads_atx.py

1. **write_DSC_atx**(filePath,Elements,Nodes,IDs)
    * filePath - Path to the output .atx file [string]
    * Elements - deformed surface element data [list (int)]
    * Nodes - deformed surface node data [list (float)]
    * IDs - the deformed surface ID [list (int)]

2. **write_NVC_atx**(filePath,Elements,faceID,normalVector)
    * filePath - Path to the output .atx file [string]
    * Elements - Element ID that normal vector constraints are attached [list (int)]
    * faceID - Face ID that normal vector constraints are attached [list (int)]
    * normalVector - NVC data

3. numNVC, ElementID, FaceID, NVC = **read_NVC_atx**(filePath)
    * numNVC - Number of NVC included in the .atx file [int]
    * ElementID - Element ID that NVCs are attached [list (int)]
    * FaceID - Face ID that normal vector constraints are attached [list (int)]
    * NVC - Normal Vector constraint data
    * filePath - Path to the input .atx file [string]

4. **write_transientID_atx**(filePath,NodeID, transientID)
    * filePath - Path to the output .atx file
    * NodeID - Node ID of attaching the transient ID
    * transientID - transient temperature ID of attaching the transient ID

### beads_txt.py

1. surfID, surfConst = **read_txt**(filepath)
    * surfID - the surface ID appllying the equation
    * surfConst - the equation for the surface
    * filePath - Input .txt file

### beads_domain.py

1. volume = **calculate_Volume**(Nodes)
    * volume - Volume [int]
    * Nodes - Tetrahedron Node [list (float)]

2. volumeValue = **calculate_Volume_Volume**(Elements,Nodes,Volumes)
    * volumeValue - Volume in each Volume [list (float)]
    * Elements - Element data of the mesh [list (int)]
    * Nodes - Node data of the mesh [list (float)]
    * Volumes - Volume data of the mesh [list (int)]

3. area = **calculate_triangle_area**(Nodes)
    * area - Triangle area [float]
    * Nodes - Triangle area [list (float)]

4. surface_area = **calculate_surface_area**(Elements,Nodes)
    * surface_area - calculated surface area [list (float)]
    * Elements - Element data that consists of a surface [list (int)]
    * Nodes - Node data [list (float)]

### beads_vector.py

1. norm = **vector_norm**(vector,n)
    * norm - Vector Norm [float]
    * vector - Vector [list (float)]
    * n - norm order [int]

2. normalize_vector = **normalize_vector**(vector)
    * normalize_vector - normalized vector [list (float)]
    * vector - input vector [list (float)]

3. cross_product = **cross_product**(vector1,vector2)
    * cross_product - output vector [list (float)]
    * vector1 - input vector [list (float)]
    * vector2 - input vector [list (float)]

4. normal_vector = **normal_vector**(Nodes)
    * normal_vector - output normal vector [list (float)]
    * Nodes - Triangle node vector [list (float)]

5. inner_product = **inner_product**(vector1,vector2)
    * inner_product - Inner product [float]
    * vector1 - Input vector [list (float)]
    * vector2 - Input vector [list (float)]

6. cosine_similarity = **cosine_similarity**(vector1,vector2)
    * cosine_similarity - calculated cosine similarity [float]
    * vector1 - Input vector [list (float)]
    * vector2 - Input vector [list (float)]

7. w,v = **beads_pca**(Nodes)
    * w - Eigen values [list (float)]
    * v - standard vector [list (float)]
    * Nodes - Input Nodes

8. intersection = **calc_perpendicular_leg**(point,Nodes)
    * intersection - coordinate of perpendicular leg [list (float)]
    * point - Input point that the start point of vector [list (float)]
    * Nodes - Input 3 Nodes that consists a plane [lsit (float)]

9. ans = **judge_inout**(point,Nodes)
    * ans - 1 means in, 0 means out [list (int)]
    * point - judging point [list (float)]
    * Nodes - 3 Nodes consists of triangle [list (float)]

### beads_judge.py

1. result = **judge_Nodes**(equation,Nodes)
    * result - 1 is in, 0 is out [int]
    * equation - Equation for judging the Node [string]
    * Nodes - Nodes data that is judged [list (float)]

2. result = **judge_Elements**(equation,Nodes,Elements)
    * result - 1 is in, 0 is out [int]
    * equation - Equation for judging the Element [string]
    * Nodes - Nodes data that is judged [list (float)]
    * Elements - Elements data that is judged [lsit (int)]

### beads_NN.py
This script uses the "nmslib"

1. resultIDs, resultDist = **beads_kNN**(Points,Nodes,Num)
    * resultIDs - Points ID [list (int)]
    * resultDist - Distance [list (float)]
    * Points - Point data [list (float)]
    * Nodes - Node data [list (float)]
    * Num - Number of searching points [int]

### beads_NtS.py

1. NtS_result = **eads_NtS**(Points,Elements,Nodes)
    * NtS_result - Node-to-Surface result [list (int)]
    * Points - Point data [list (float)]
    * Elements - Element data [list (int)]
    * Nodes - Node data [list (float)]

### beads_log.py
This script just do logging

1. logger = read_logger()
    * logger - Create logger in the script
