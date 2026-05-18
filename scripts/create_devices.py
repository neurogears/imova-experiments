from generate_schemas import CameraDevice
import os

folder = "device_configs"
os.makedirs(folder, exist_ok=True)

def create_camera(idx, name):

    camera = CameraDevice(
        device_idx=idx,
        device_name=f"{name}",
        exposure=1000,
        gain=20
    )

    with open(f"{folder}/{camera.device_name}.json", "w") as f:
        f.writelines(camera.model_dump_json(indent=2))

create_camera(0, "CameraTopLeft")
create_camera(1, "CameraTop")
create_camera(2, "CameraBottomRight")
create_camera(3, "CameraRight")
create_camera(4, "CameraTopRight")
create_camera(5, "CameraCenter")
create_camera(6, "CameraLeft")
create_camera(7, "CameraBottomLeft")