import json, os, cv2

def get_balloon_dicts():
    json_file = 'submit_example.json'
    with open(json_file) as f:
        imgs_anns = json.load(f)
    print(imgs_anns)

    dataset_dicts = []
    for idx, v in enumerate(imgs_anns.values()):
        record = {}
        print(v)
        filename = v['filename']
        height, width = cv2.imread(filename).shape[:2]

        record['file_name'] = filename
        record['image_id'] = idx
        record['height'] = height
        record['width'] = width

        annos = v['regions']
        objs = []
        for _, anno in annos.items():
            assert not anno['region_attributes']
            anno = anno['shape_attributes']
            px = anno['all_points_x']
            py = anno['all_points_y']
            poly = [(x + 0.5, y + 0.5) for x, y in zip(px, py)]
            poly = [p for x in poly for p in x]

            obj = {
                "bbox": [np.min(px), np.min(py), np.max(px), np.max(py)],
                "bbox_mode": BoxMode.XYXY_ABS,
                "segmentation": [poly],
                "category_id": 0,
            }
            objs.append(obj)
            record['annotations'] = objs
            dataset_dicts.append(record)
    # print(dataset_dicts)
    # get_balloon_dicts()
print(get_balloon_dicts)