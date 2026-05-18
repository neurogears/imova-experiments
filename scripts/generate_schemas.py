from pydantic import BaseModel, Field
import json
from argparse import ArgumentParser
import os

class CameraDevice(BaseModel):
    device_idx: int = Field(
        default=0,
        ge=0,
    )
    device_name: str = Field(
        default = "Camera0"
    )
    gain: float = Field(
        default = 0,
        ge=0,
    )
    exposure: float = Field(
        default = 1000,
        ge=0
    )
    description: str = Field(
        default = ""
    )

def main():
    parser = ArgumentParser()
    parser.add_argument("--path", type = str, default = "./schemas")
    args = parser.parse_args()
    schema = CameraDevice.model_json_schema()
    output_path = os.path.join(args.path,f"{CameraDevice.__name__}.schema.json" )
    with open(output_path, "w") as f:
        f.write(json.dumps(schema, indent=2))


if __name__ == "__main__":
    main()
