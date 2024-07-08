"""Утилиты для распознавания картинок."""
import torch
from torchvision import models, transforms
from PIL import Image

# Загрузка предобученной модели Faster R-CNN
model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

# Трансформация изображения для модели
preprocess = transforms.Compose(
    [
        transforms.ToTensor(),
    ]
)


def detect_objects(image_path):
    image = Image.open(image_path)
    image_tensor = preprocess(image)
    image_tensor = image_tensor.unsqueeze(0)

    # Выполняем предсказание
    with torch.no_grad():
        predictions = model(image_tensor)

    # Загрузка классов COCO
    COCO_INSTANCE_CATEGORY_NAMES = [
        "__background__",
        "person",
        "bicycle",
        "car",
        "motorcycle",
        "airplane",
        "bus",
        "train",
        "truck",
        "boat",
        "traffic light",
        "fire hydrant",
        "N/A",
        "stop sign",
        "parking meter",
        "bench",
        "bird",
        "cat",
        "dog",
        "horse",
        "sheep",
        "cow",
        "elephant",
        "bear",
        "zebra",
        "giraffe",
        "N/A",
        "backpack",
        "umbrella",
        "N/A",
        "N/A",
        "handbag",
        "tie",
        "suitcase",
        "frisbee",
        "skis",
        "snowboard",
        "sports ball",
        "kite",
        "baseball bat",
        "baseball glove",
        "skateboard",
        "surfboard",
        "tennis racket",
        "bottle",
        "N/A",
        "wine glass",
        "cup",
        "fork",
        "knife",
        "spoon",
        "bowl",
        "banana",
        "apple",
        "sandwich",
        "orange",
        "broccoli",
        "carrot",
        "hot dog",
        "pizza",
        "donut",
        "cake",
        "chair",
        "couch",
        "potted plant",
        "bed",
        "N/A",
        "dining table",
        "N/A",
        "N/A",
        "toilet",
        "N/A",
        "tv",
        "laptop",
        "mouse",
        "remote",
        "keyboard",
        "cell phone",
        "microwave",
        "oven",
        "toaster",
        "sink",
        "refrigerator",
        "N/A",
        "book",
        "clock",
        "vase",
        "scissors",
        "teddy bear",
        "hair drier",
        "toothbrush",
    ]

    # Получаем результаты
    results = []
    for idx, score in enumerate(predictions[0]["scores"]):
        if score > 0.5:  # Используем порог 0.5 для отбора значимых предсказаний
            label_idx = predictions[0]["labels"][idx].item()
            label = COCO_INSTANCE_CATEGORY_NAMES[label_idx]
            results.append(label)

    return list(set(results))  # Возвращаем уникальные распознанные объекты
