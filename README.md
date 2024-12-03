# depth_estimation

depth_estimation is a powerful model for recovering 3D geometry from monocular open-domain images. The model consists of a ViT encoder and a convolutional decoder. It directly predicts an affine-invariant point map as well as a mask that excludes regions with undefined geometry (e.g., sky), from which the camera shift, camera focal length and depth map can be further derived. 
