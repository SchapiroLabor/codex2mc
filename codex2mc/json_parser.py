import json
from pprint import pprint

def main():
    with open("test_data/metadata/experimentV4.json") as f:
        d = json.load(f)

    for region in d["regions"]:
        tile_dict  = {k: dict(list(v.items())[1:]) for k, v in sorted((e["index"], e) for e in region["tiles"])}

        for tile_id, tile_vals in tile_dict.items():
            param_dct = {
                    "position_x": tile_vals["x"],
                    "position_y": tile_vals["y"],
                    "position_x_unit": None,
                    "position_y_unit": None,
                    "physical_size_x": None,
                    "physical_size_x_unit": None,
                    "physical_size_y": None,
                    "physical_size_y_unit": None,
                    "size_x": d["tileWidth_px"],
                    "size_y": d["tileHeight_px"],
                    "type": d["microscopeBitDepth"],  # bit_depth, is this correct?
                    "significant_bits": None,
                    "emission_wavelenght": None,
                    "excitation_wavelenght": None,
                    "emission_wavelenght_unit": None,
                    "excitation_wavelenght_unit": None,
                }


if __name__ == "__main__":
    main()
